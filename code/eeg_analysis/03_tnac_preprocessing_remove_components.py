# --- Jose C. Garcia Alanis
# --- utf-8
# --- Python 3.6.2
#
# --- EEG prepossessing - DPX TT
# --- Version Sep 2018
#
# --- Inspect ICA components, remove bad components,
# --- save results

# =================================================================================================
# ------------------------------ Import relevant extensions ---------------------------------------
import glob
import os
import mne
from mne import io
from mne.preprocessing import create_ecg_epochs

# =============================================================================
# --- GLOBAL SETTINGS
# --- path to where file are stored (and output should go to)
# base_path = '/media/josealanis/ceccmusci/ga_trial/'
base_path = '/Volumes/ceccmusci/ga_trial/'

# Threshold for plotting
clip = None

files = glob.glob(os.path.join(base_path, 'mne_tnac_raws/*-raw.fif'))

for file in files:

    # --- 1) Set up paths and file names -----------------------
    filepath, filename = os.path.split(file)
    filename, ext = os.path.splitext(filename)
    print(filename)

    # --- 2) Read in the data ----------------------------------
    raw = io.read_raw_fif(file,
                          preload=True)

    # raw.drop_channels(['EXG1', 'EXG2'])

    # Check info
    print(raw.info)

    # --- 3) Get event information -----------------------------
    # stimulus events
    event_id = {"S  1": 1, "S  2": 2, 'S  3': 3}  # must be specified for str events
    events = mne.events_from_annotations(raw, event_id)[0]

    # --- 4) Import ICA weights --------------------------------
    ica = mne.preprocessing.read_ica(base_path + 'mne_tnac_ica/' + filename.split('-')[0] + '-ica.fif')


    # Select bad components for rejection
    ica.plot_sources(raw, title=str(filename),
                     exclude=None,
                     picks=range(0, 15),  # set number of components
                     block=True)

    # --- 5) Plot components time series -----------------------
    # Picks to plot
    picks = mne.pick_types(raw.info,
                           meg=False,
                           eeg=True,
                           eog=False,
                           stim=True)

    # find ecg artifacts
    ecg_epochs = create_ecg_epochs(raw, tmin=-.5, tmax=.5)
    ecg_inds, scores = ica.find_bads_ecg(ecg_epochs, method='ctps')
    ica.plot_properties(ecg_epochs, picks=ecg_inds, psd_args={'fmax': 50.})
    ica.exclude.extend(ecg_inds)

    # Save bad components
    bad_comps = ica.exclude.copy()

    # --- 4) Remove bad components -----------------------------
    ica.apply(raw)

    # --- 5) Remove pruned data --------------------------------
    # Plot to check data
    clip = None
    raw.plot(n_channels=32, title=str(filename),
             scalings=dict(eeg=5e-5),
             events=events,
             bad_color='red',
             clipping=clip,
             block=True)

    # --- 6) Write summary about removed components ------------
    name = str(filename.split('-')[0]) + '_ica_summary'
    file = open(base_path + 'prepro_summary/' + '%s.txt' % name, 'w')
    # Number of Trials
    file.write('bad components\n')
    for cp in bad_comps:
        file.write('%s\n' % cp)
    # Close file
    file.close()

    # --- 7) Save raw file -----------------------------------
    # Pick electrode to use
    picks = mne.pick_types(raw.info,
                           meg=False,
                           eeg=True,
                           ecg=False,
                           eog=False,
                           stim=False)

    # Save pruned data
    raw.save(base_path + 'mne_tnac_pruned/' + filename.split('-')[0] + '_pruned-raw.fif',
             picks=picks,
             overwrite=True)
