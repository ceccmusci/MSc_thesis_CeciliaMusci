import os
import glob
import wave
import contextlib

# calculate length of sounds

#all sounds; in categories (see results in commented lines below)
path = '/home/ceccmusci/cecilia/uni/msc_kis/tnac/stimuli/stimuli_categorized/voice/'

fnames = glob.glob(os.path.join(path, '*.wav'))

durs = []
names = []
for fname in fnames:
    with contextlib.closing(wave.open(fname, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        names.append(os.path.split(fname)[1])
        durs.append(duration)

max(durs) #alltogether = 1.9586621315192745  ;  music = 1.7829931972789115   ; voice = 1.9586621315192745   ; song = 1.9407936507936507
min(durs) #alltogether  = 0.9261451247165533 ;  music =  1.2448526077097506  ; voice = 0.9758730158730159   ; song = 0.9261451247165533

# ----------------------------------------------------------------------------
#one single stimulus:

fname = '/home/ceccmusci/cecilia/uni/msc_kis/tnac/stimuli/stimuli_categorized/voice/voice_47.wav'
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    print(duration)
