# ------------------------------ Import relevant extensions ---------------------------------------

import mne
import glob
import os
import pandas as pd

# ========================================================================
# --- GLOBAL SETTINGS
# --- SET PATH TO .bdf-files, summary files and output
data_path = '/Users/Josealanis/Desktop/tnac_ga/'
summary_path = '/Users/Josealanis/Desktop/tnac_eeg/mne_tnac_summary/'
output_path = '/Users/Josealanis/Desktop/tnac_eeg/mne_tnac_raws/'

# Channels to be ignored during artifact detection procedure
ignore_ch = {'Fp1', 'Fpz', 'Fp2', 'AF7', 'AF3', 'AFz', 'AF4', 'AF8'}
# Threshold for plotting
clip = None

# === LOOP THROUGH FILES AND RUN PRE-PROCESSING ==========================
subs = glob.glob(data_path + '*[0-9]')
for subpath in subs[-1:]:
    # --- 1) Set up subject in question  -----------------------
    sub = os.path.split(subpath)[1]
    # Set up paths to runs data
    run1 = glob.glob(os.path.join(subpath, '*run1*.set'))[0]
    run2 = glob.glob(os.path.join(subpath, '*run2*.set'))[0]
    run3 = glob.glob(os.path.join(subpath, '*run3*.set'))[0]
    run4 = glob.glob(os.path.join(subpath, '*run4*.set'))[0]

    # --- 2) READ IN THE DATA ----------------------------------
    # Set EEG arrangement
    montage = mne.channels.read_montage(kind='standard_1005')
    # Import raw data
    raw1 = mne.io.read_raw_eeglab(run1, event_id_func='strip_to_integer',
                                  montage=montage, preload=True)
    raw2 = mne.io.read_raw_eeglab(run2, event_id_func='strip_to_integer',
                                  montage=montage, preload=True)
    raw3 = mne.io.read_raw_eeglab(run3, event_id_func='strip_to_integer',
                                  montage=montage, preload=True)
    raw4 = mne.io.read_raw_eeglab(run4, event_id_func='strip_to_integer',
                                  montage=montage, preload=True)

    # --- 3) Concatenate individual runs -----------------------
    # Concatenate block data
    raw = mne.concatenate_raws([raw1, raw2, raw3, raw4])

    # --- 4) Create custom info for new raw object -------------
    # Note the sampling rate of recording
    sfreq = raw.info['sfreq']
    # and Buffer size ???
    # bsize = raw.info['buffer_size_sec']
    # nr of eeg chans
    n_eeg = 31
    # names
    chans = raw.info['ch_names'][0:n_eeg]
    # extend by ecg and stimulus channel
    chans.extend(['ECG', 'Stim'])
    # channel types
    chan_types = ['eeg', 'eeg', 'eeg', 'eeg', 'eeg',
                  'eeg', 'eeg', 'eeg', 'eeg', 'eeg',

                  'eeg', 'eeg', 'eeg', 'eeg', 'eeg',
                  'eeg', 'eeg', 'eeg', 'eeg', 'eeg',

                  'eeg', 'eeg', 'eeg', 'eeg', 'eeg',
                  'eeg', 'eeg', 'eeg', 'eeg', 'eeg',

                  'eeg', 'ecg', 'stim']
    # custom data information
    info_custom = mne.create_info(chans, sfreq, chan_types, montage)
    # Add description / name of experiment
    info_custom['description'] = 'TNAC combined'

    # Replace the mne info structure with the customized one
    # which has the correct labels, channel types and positions.
    raw.info = info_custom
    # raw.info['buffer_size_sec'] = bsize

    # Get events
    events = mne.find_events(raw,
                             stim_channel='Stim',
                             output='onset',
                             shortest_event=1)

    # --- 5) GET EVENTS THAT REPRESENT CUE STIMULI -------------
    # Cue events
    evs = events[(events[:, 2] >= 1) & (events[:, 2] <= 3), ]

    # --- 5) Select channels and apply filter ------------------
    # EEG channels
    picks_eeg = mne.pick_types(raw.info, eeg=True,
                               ecg=False,
                               meg=False,
                               eog=False,
                               stim=False)
    # ECG channel
    picks_ecg = mne.pick_types(raw.info, ecg=True,
                               eeg=False,
                               meg=False,
                               eog=False,
                               stim=False)
    # All channels
    picks_all = mne.pick_types(raw.info, eeg=True, ecg=True,
                               meg=False,
                               eog=False,
                               stim=True)

    # Filter the data
    raw.filter(0.1, 50, fir_design='firwin', picks=picks_eeg)
    raw.filter(0.1, 50, fir_design='firwin', picks=picks_ecg)

    # --- 6) Specify offline reference to mastoids --------------
    raw.set_eeg_reference(ref_channels=['TP9', 'TP10'])

    # --- 7) FIND DISTORTED SEGMENTS IN DATA ------------------
    # Copy of data
    x = raw.get_data()

    # Channels to be checked by artifact detection procedure
    ch_ix = [k for k in range(len(raw.info['ch_names'])) if
             raw.info['ch_names'][k] not in ignore_ch and k < n_eeg]

    # Detect artifacts (i.e., absolute amplitude > 500 microV)
    times = []
    annotations_df = pd.DataFrame(times)
    onsets = []
    duration = []
    for j in range(0, len(x[0])):
        if len(times) > 0:
            if j <= (times[-1] + int(2 * sfreq)):
                continue
        t = []
        for i in ch_ix:
            t.append(abs(x[i][j]))
        if max(t) >= 5e-4:
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
        raw.annotations = annotations

    # ======================================================================
    # --- 8) CHECK FOR INCONSISTENCIES ------------------------------------
    # Alert
    os.system('say "Ich möchte diesen Teppich nicht kaufen"')
    # Plot
    raw.plot(n_channels=32,
             scalings=dict(eeg=100e-6),
             events=evs,
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
                if j <= (times[-1] + int(2 * sfreq)):
                    continue
            t = []
            for i in ch_ix:
                t.append(abs(x[i][j]))
            if max(t) >= 5e-4:
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
            raw.annotations = annotations

        # --- PLOT TO CHECK
        # Alert
        os.system('say "Ich möchte diesen Teppich nicht kaufen"')
        # Plot
        raw.plot(n_channels=31,
                 scalings=dict(eeg=100e-6),
                 events=evs,
                 bad_color='red',
                 block=True,
                 clipping=clip)

    # --- 9) WRITE PRE-PROCESSING SUMMARY ----------------------
    name = str(sub) + '_mne_prepro_summary'
    file = open(summary_path + '%s.txt' % name, 'w')
    # Number of Trials
    file.write('number of trials\n')
    file.write(str(len(evs)) + '\n')
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
    file.write(str(sum(duration / evs[-1][0])))
    # Close file
    file.close()

    # --- 10) SAVE RAW FILE -----------------------------------
    # Save segmented data
    raw.save(output_path + sub + '-raw.fif',
             picks=picks_all,
             overwrite=True)
