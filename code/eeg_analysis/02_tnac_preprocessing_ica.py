# --- Jose C. Garcia Alanis
# --- utf-8
# --- Python 3.6.2
#
# --- EEG prepossessing - DPX TT
# --- Version Jul 2018
#
# --- ICA decomposition, ICA summary,
# --- save results

# =================================================================================================
# ------------------------------ Import relevant extensions ---------------------------------------
import glob
import os
import mne
from mne import io
from mne.preprocessing import ICA

# =============================================================================
# --- GLOBAL SETTINGS
# --- path to where file are stored (and output should go to)
# base_path = '/media/josealanis/ceccmusci/ga_trial/'
base_path = '/Volumes/ceccmusci/ga_trial/'

# Threshold for plotting
clip = None

files = glob.glob(os.path.join(base_path, 'mne_tnac_raws/*-raw.fif'))

# === LOOP THROUGH FILES AND RUN PRE-PROCESSING ==========================
for file in files[0:1]:

    # --- 1) Set up paths and file names -----------------------
    filepath, filename = os.path.split(file)
    filename, ext = os.path.splitext(filename)
    print('Ready for ' + filename)
    # --- 2) READ IN THE DATA ----------------------------------
    # Import preprocessed data.
    raw = io.read_raw_fif(file, preload=True)
    # Check info
    print(raw.info)
    # --- 3) GET EVENT INFORMATION -----------------------------
    # Get events
    # evs = mne.find_events(raw,
    #                       stim_channel='Stim',
    #                       output='onset',
    #                       min_duration=0.002)

    # --- 2) ICA DECOMPOSITION --------------------------------
    # ICA parameters
    n_components = 15
    method = 'extended-infomax'
    # decim = None
    reject = dict(eeg=3e-4)

    # Pick electrodes to use
    picks = mne.pick_types(raw.info,
                           eeg=True,
                           ecg=False,
                           meg=False,
                           eog=False,
                           stim=False)

    # ICA parameters
    ica = ICA(n_components=n_components,
              method=method)

    # Fit ICA
    ica.fit(raw.copy().filter(1, 50),
            picks=picks,
            reject=reject)

    ica.save(base_path + 'mne_tnac_ica/' + filename.split('-')[0] + '-ica.fif')

    # --- 3) PLOT RESULTING COMPONENTS ------------------------
    # Plot components
    ica_fig = ica.plot_components(picks=range(0, 15), show=False)
    ica_fig.savefig(base_path + 'prepro_summary/' + filename.split('-')[0] + '_ica.pdf')




