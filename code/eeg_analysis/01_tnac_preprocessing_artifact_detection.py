# --- Jose C. Garcia Alanis
# --- utf-8
# --- Python 3.6.2
#
# --- EEG prepossessing - DPX TT
# --- Version Jul 2018
#
# --- Artifact detection, interpolate bad channels, extract block data,
# --- filtering, re-referencing.

# ==================================================================================================
# ---------------------------------- Import relevant extensions ------------------------------------
import glob
import os
import re

import pandas as pd
import mne

# =============================================================================
# --- GLOBAL SETTINGS
# --- path to where file are stored (and output should go to)
# base_path = '/media/josealanis/ceccmusci/ga_trial/'
base_path = '/Volumes/ceccmusci/ga_trial/'


# Channels to be ignored during artifact detection procedure
ignore_ch = {'Fp1', 'Fpz', 'Fp2', 'AF7', 'AF3', 'AFz', 'AF4', 'AF8', 'ECG'}
# Threshold for plotting
clip = None
# list of subjects
subs = glob.glob(os.path.join(base_path, 'subjects/') + '*[0-9]')
events_found = []

# === LOOP THROUGH FILES AND RUN PRE-PROCESSING ===============================
for subpath in subs[0]:
    print(subpath)
    # --- 1) Set up subject in question  ----------------------------
    sub = os.path.split(subpath)[1]
    # Set up paths to runs data
    run1 = glob.glob(os.path.join(subpath, '*run1*.set'))[0]
    run2 = glob.glob(os.path.join(subpath, '*run2*.set'))[0]
    run3 = glob.glob(os.path.join(subpath, '*run3*.set'))[0]
    run4 = glob.glob(os.path.join(subpath, '*run4*.set'))[0]

    # --- 2) READ IN THE DATA ---------------------------------------
    # Set EEG arrangement
    montage = mne.channels.read_montage(kind='standard_1005')

    # Import raw data
    raw1 = mne.io.read_raw_eeglab(run1,
                                  montage=montage,
                                  preload=True,
                                  stim_channel=False)
    raw2 = mne.io.read_raw_eeglab(run2,
                                  montage=montage,
                                  preload=True,
                                  stim_channel=False)
    raw3 = mne.io.read_raw_eeglab(run3,
                                  montage=montage,
                                  preload=True,
                                  stim_channel=False)
    raw4 = mne.io.read_raw_eeglab(run4,
                                  montage=montage,
                                  preload=True,
                                  stim_channel=False)

    # --- 3) Concatenate individual runs ----------------------------
    # Concatenate block data
    raw = mne.concatenate_raws([raw1, raw2, raw3, raw4])
    # make space in memory
    del raw1, raw2, raw3, raw4

    # --- 4) Create custom info for mne-raw structure ---------------
    # sampling rate
    sfreq = raw.info['sfreq']

    # all channels in raw
    chans = raw.info['ch_names']
    # channels in montage
    montage_chans = montage.ch_names
    # nr of eeg channels
    n_eeg = len([chan for chan in chans if chan in montage_chans])
    # channel types
    types = ['ecg' if re.match('ECG|ecg', chan) else 'eeg' for chan in chans]

    # custom data information
    info_custom = mne.create_info(chans, sfreq, types, montage)
    # Add description / name of experiment
    info_custom['description'] = 'TNAC_combined'
    # Replace the mne info structure with the customized one
    # which has the correct labels, channel types and positions.
    raw.info = info_custom

    # --- 5) Lower the sample rate of the eeg recording -------------
    # resample the data to 2000 Hz
    raw.resample(2000, npad='auto')

    # stimulus events
    event_id = {"S  1": 1, "S  2": 2, 'S  3': 3}  # must be specified for str events
    events = mne.events_from_annotations(raw, event_id)[0]

    # clean up annotations
    raw_annotations = raw.annotations.description.tolist()
    drops = [x for x, i in enumerate(raw_annotations) if i in {'Sync On', 'R128', 'boundary'}]
    raw.annotations.delete(drops)

    # events found for each subject
    events_found.append([sub, len(events)])

    # --- 5) Select channels and apply filter ------------------
    # EEG channels
    picks = mne.pick_types(raw.info,
                           eeg=True,
                           ecg=True,
                           meg=False,
                           eog=False,
                           stim=False)

    # Filter the data
    raw.filter(0.1, 50, fir_design='firwin', picks=picks)

    # --- 6) Specify offline reference to mastoids --------------
    raw.set_eeg_reference(ref_channels=['TP9', 'TP10'])

    # --- 7) FIND DISTORTED SEGMENTS IN DATA ------------------
    # Copy of data
    x = raw.get_data()

    # Channels to be checked by artifact detection procedure
    ch_ix = [chan for chan in range(len(raw.info['ch_names'])) if
             raw.info['ch_names'][chan] not in ignore_ch and chan < n_eeg]

    # Detect artifacts (i.e., absolute amplitude > 500 microV)
    sfreq = raw.info['sfreq']
    times = []
    annotations_df = pd.DataFrame(times)
    onsets = []

    duration = []
    for j in range(0, len(x[0])):
        if len(times) > 0:
            if j <= (times[-1] + int(1 * sfreq)):
                continue
        t = []
        for i in ch_ix:
            t.append(abs(x[i][j]))
        if max(t) >= 3e-4:
            times.append(float(j))
    # If artifact found create annotations for raw data
    if len(times) > 0:
        # Save onsets
        annotations_df = pd.DataFrame(times)
        annotations_df.columns = ['Onsets']
        # Include one second before artifact onset
        onsets = (annotations_df['Onsets'].values / sfreq) - 1
        # Merge with previous annotations
        duration = [2] * len(onsets) + list(raw.annotations.duration)
        labels = ['Bad'] * len(onsets) + list(raw.annotations.description)
        onsets = list(onsets)
        # Append onsets of previous annotations
        for i in range(0, len(list(raw.annotations.onset))):
            onsets.append(list(raw.annotations.onset)[i])
        # Create new annotation info
        annotations = mne.Annotations(onsets, duration, labels)
        raw.set_annotations(annotations)

    # ======================================================================
    # --- 8) CHECK FOR INCONSISTENCIES ------------------------------------
    # Alert
    os.system('say "Ich möchte diesen Teppich nicht kaufen"')
    # Plot
    raw.plot(n_channels=32,
             scalings=dict(eeg=100e-6),
             events=events,
             bad_color='red',
             block=True,
             clipping=clip)

    # Save bad channels
    bad_ch = raw.info['bads']

    # --- IF BAD CHANNELS FOUND:
    # --- INTERPOLATE CHANNELS, RE-RUN PRE-PROCESSING STEPS
    if len(bad_ch) >= 1:
        # INTERPOLATE BAD CHANNELS
        raw.interpolate_bads(reset_bads=True,
                             verbose=False,
                             mode='accurate')

        # Copy of data, detect artifacts
        x = raw.get_data()
        # Detect artifacts (i.e., absolute amplitude > 500 microV)
        times = []
        annotations_df = pd.DataFrame(times)
        onsets = []
        duration = []
        for j in range(0, len(x[0])):
            if len(times) > 0:
                if j <= (times[-1] + int(1 * sfreq)):
                    continue
            t = []
            for i in ch_ix:
                t.append(abs(x[i][j]))
            if max(t) >= 3e-4:
                times.append(float(j))
        # If artifact found create annotations for raw data
        if len(times) > 0:
            # Save onsets
            annotations_df = pd.DataFrame(times)
            annotations_df.columns = ['Onsets']
            # Include one second before artifact onset
            onsets = (annotations_df['Onsets'].values / sfreq) - 1
            # Merge with previous annotations
            duration = [2] * len(onsets) + list(raw.annotations.duration)
            labels = ['Bad'] * len(onsets) + list(raw.annotations.description)
            onsets = list(onsets)
            # Append onsets of previous annotations
            for i in range(0, len(list(raw.annotations.onset))):
                onsets.append(list(raw.annotations.onset)[i])
            # Create new annotation info
            annotations = mne.Annotations(onsets, duration, labels)
            raw.set_annotations(annotations)

        # --- PLOT TO CHECK
        # Alert
        os.system('say "Ich möchte diesen Teppich nicht kaufen"')
        # Plot
        raw.plot(n_channels=31,
                 scalings=dict(eeg=100e-6),
                 events=events,
                 bad_color='red',
                 block=True,
                 clipping=clip)

    # --- 9) WRITE PRE-PROCESSING SUMMARY ----------------------
    name = str(sub) + '_mne_prepro_summary'
    file = open(os.path.join(base_path, 'prepro_summary/') + '%s.txt' % name, 'w')
    # Number of Trials
    file.write('number of trials\n')
    file.write(str(len(events)) + '\n')
    # Interpolated channels
    file.write('interpolated Channels\n')
    for ch in bad_ch:
        file.write('%s\n' % ch)
    # Artifacts detected
    file.write('annotated times\n')
    for on in onsets:
        file.write('%s\n' % str(round(on, 3)))
    # Total distorted time
    file.write('total annotated time (s)\n')
    file.write(str(sum(duration)) + '\n')
    file.write('Percent annotated \n')
    file.write(str(sum(duration / events[-1][0])))
    # Close file
    file.close()

    # --- 10) SAVE RAW FILE -----------------------------------
    # Save segmented data
    raw.save(os.path.join(base_path, 'mne_tnac_raws/') + sub + '-raw.fif',
             picks=picks,
             overwrite=True)

    del raw