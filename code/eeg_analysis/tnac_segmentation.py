# --- Jose C. Garcia Alanis
# --- utf-8
# --- Python 3.6.2
# --- adapted for tnac
# --- Extract epochs for trial and experimental conditions,
# --- save results

# =================================================================================================
# ------------------------------ Import relevant extensions ---------------------------------------
import os
import glob
# import csv
import re

import pandas as pd
import numpy as np

import mne
from mne import io

# =============================================================================
# --- GLOBAL SETTINGS
# --- path to where file are stored (and output should go to)
# base_path = '/media/josealanis/ceccmusci/ga_trial/'
base_path = '/Volumes/ceccmusci/ga_trial/'

summary_path = '/Volumes/ceccmusci/tnac/mne_tnac_segmentation_summary/'
choice_output_path = '/Volumes/ceccmusci/tnac/mne_tnac_epochs/'

# --- set paths
path_to_subs = base_path + 'data_psychopy/'
subject_paths = sorted(glob.glob(path_to_subs + 'sub*'))

# --- run order
run_order = pd.read_csv(path_to_subs + 'runlist_t.csv')

# --- find events in run files ---
events_x_run = dict()
    for subject in subject_paths[1:]:
        print(subject)

    subject = '/Volumes/ceccmusci/ga_trial/data_psychopy/sub20_date_2018_Aug_07_1021'
    # subject in question
    sub = re.search('sub[0-9][0-9]', os.path.split(subject)[1]).group(0)

    sub_runs = run_order[sub].values.tolist()
    sub_runs = ['run' + str(i) for i in sub_runs]

    # open dictionary for subject within subjects dictionary
    events_x_run['%s' % sub] = dict()
    # open dictionary for runs data
    ind_runs = sorted(glob.glob(os.path.join(subject, 'sub*.csv')))
    for ind in ind_runs:
        run_id = re.search('run[0-9]', os.path.split(ind)[1]).group(0)
        events_x_run[sub]['%s' % run_id] = []
        run_data=pd.read_csv(ind)
        for i in range(0, 180):
            events_x_run[sub]['%s' % run_id].append(run_data['stimuli'][i])

    for key in sub_runs:
        events_x_run[sub][key] = events_x_run[sub].pop(key)


# --- stimuli to be excluded ---
# bad_stims  = ['music/music_50.wav', 'music/music_10.wav', 'music/music_11.wav',
#               'music/music_7.wav', 'music/music_51.wav', 'music/music_32.wav',
#                'voice/voice_12.wav', 'voice/voice_31.wav', 'voice/voice_25.wav',
#               'voice/voice_15.wav', 'voice/voice_20.wav', 'voice/voice_17.wav',
#                'song/song_26.wav', 'song/song_36.wav', 'song/song_44.wav',
#               'song/song_59.wav', 'song/song_33.wav', 'song/song_46.wav']

bad_stims = []

# --- subject files
files = glob.glob(os.path.join(base_path, 'mne_tnac_pruned/*.fif'))

# === LOOP THROUGH FILES AND EXTRACT EPOCHS =========================
for file in files:

    # --- 1) Set up paths and file names ----------------------------
    filepath, filename = os.path.split(file)
    filename, ext = os.path.splitext(filename)
    print(filename)

    # subject id
    sub = re.search('sub[0-9][0-9]', filename).group(0)

    # stimuli codes for subject in question
    stimuli = [i for run in events_x_run[sub] for i in events_x_run[sub][run]]

    # index epoch if a bad stimulus was presented
    bad_epochs = []
    for i, stim in enumerate(stimuli):
        if stim in bad_stims:
            if i < 719:
                bad_epochs.append(i+1)

    # --- 2) Read in the data ----------------------------------
    raw = io.read_raw_fif(file,
                          preload=True)
    # # Check info
    # print(raw.info)

    # --- 3) RECODE EVENTS -----------------------------------------
    #  Get events
    # stimulus events
    event_id = {"S  1": 1, "S  2": 2, 'S  3': 3}  # must be specified for str events
    events = mne.events_from_annotations(raw, event_id)[0]

    # # Copy of events
    # sound_evs = evs[evs[:, 2] <= 3]
    #
    # # Recode reactions
    # for trial in range(sound_evs[:, 2].size):
    #     print(trial)
    #     if trial not in bad_epochs:
    #         if sound_evs[:, 2][trial] == 1:
    #             sound_evs[:, 2][trial] = 111
    #         elif sound_evs[:, 2][trial] == 2:
    #             sound_evs[:, 2][trial] = 112
    #         elif sound_evs[:, 2][trial] == 3:
    #             sound_evs[:, 2][trial] = 113
    #     else:
    #         continue


    # --- 5) EXTRACT EPOCHS ------------------------------------
    # Set event ids
    event_id = {'music': 1, 'voice': 2, 'song': 3}

    # channels to include in epochs structure
    picks=mne.pick_types(raw.info,
                         eeg=True,
                         eog=False,
                         stim=False,
                         ecg=False)

    reject = dict(eeg=300e-6)
    tnac_epochs = mne.Epochs(raw, events, event_id,
                             on_missing='ignore',
                             tmin=-.2,
                             tmax=2.,
                             baseline=(-.2, 0.),
                             preload=True,
                             reject_by_annotation=False,
                             reject=reject,
                             picks=picks)

    # sample down
    tnac_epochs.resample(sfreq=256)

    # tnac_epochs.plot(scalings=dict(eeg=100e-6))

    from matplotlib import pyplot as plt

    tnac_epochs['music'].average().plot_joint()
    plt.savefig('sub20_music.pdf')
    tnac_epochs['voice'].average().plot_joint()
    plt.savefig('sub20_voice.pdf')
    tnac_epochs['song'].average().plot_joint()
    plt.savefig('sub20song.pdf')



#
#
# # annotation?
#     # ------------------------------------------------------------
#
#     # Extract choice epochs
#     reject = dict(eeg=250e-6)
#     choice_epochs = mne.Epochs(raw, stims, event_id,
#                                on_missing='ignore',
#                                tmin=-5.,
#                                tmax=,
#                                baseline=None,
#                                preload=True,
#                                reject_by_annotation=False,
#                                picks=picks,
#                                reject=reject)
#
#     # Clean epochs
#     clean_choices = choice_epochs.selection+1
#     bads = [x for x in set(list(range(0, trial)))
#             if x not in set(choice_epochs.selection)]
#     bads = [x+1 for x in bads]
#
#     # --- 6) WRITE SUMMARY -------------------------------------
#     # Write summay file
#     name = filename.split('_')[0] + '_epochs_summary'
#     # Open summary file
#     sum_file = open(summary_path + '%s.txt' % name, 'w')
#
#     sum_file.write('Too soon epochs are ' + str(len(too_soon)) + ':\n')
#     for t in too_soon:
#         sum_file.write('%s \n' % t)
#
#     sum_file.write('Miss epochs are ' + str(len(miss)) + ':\n')
#     for m in miss:
#         sum_file.write('%s \n' % m)
#
#     sum_file.write('Rejected epochs are ' + str(len(bads)) + ':\n')
#     for b in bads:
#         sum_file.write('%s \n' % b)
#
#     sum_file.write('Extracted epochs are ' + str(len(clean_choices)) + ':\n')
#     for c in clean_choices:
#         sum_file.write('%s \n' % c)
#     # Close summary file
#     sum_file.close()
#
#     # --- 7) RESAMPLE EPOCHS -----------------------------------
#     choice_epochs.resample(sfreq=256)
#
#     # --- 8) SAVE EPOCHS ---------------------------------------
#     choice_epochs.save(choice_output_path + filename.split('_')[0] + '_tnac_epo.fif')
