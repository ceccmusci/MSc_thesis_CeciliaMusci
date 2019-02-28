

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import random as rd
import copy
import os

def check_list(input_list):
    check_ok = True
    for i in range(len(input_list)-1):
        if input_list[i] == input_list[i+1]:
            check_ok = False
            return check_ok
    return check_ok

def generate_conter_list():
    block_list = 12*['song','music','voice']
    rd.shuffle(block_list)
    balanced = False
    while not balanced:
        #check
        balanced = check_list(block_list)
        #if not ok reshuffle
        if not balanced:
            rd.shuffle(block_list)
    return block_list


def gen_runfiles():

   # set variable for a relative directory (comparable "folder"-directory)
   # create stimulus-lists for voice, song and music each (will later be replaced with stim_files from angulo-perkins)
   stim_voice = np.arange(60)
   stim_song = np.arange(60)
   stim_music = np.arange(60)

   # 3 fictive (randomized) block-sequences, will be replaced with neuropowertool-generated sequences
   block_seq = 12*['voice','song','music']
   block_seq1 = generate_conter_list()#copy.deepcopy(block_seq)
   print('block done')
   block_seq2 = generate_conter_list()
   print('block done')
   block_seq3 = generate_conter_list()
   print('block done')
   block_seq4 = generate_conter_list()
   print('block done')
   #rd.shuffle(block_seq1)
   #rd.shuffle(block_seq2)
   #rd.shuffle(block_seq3)
   #rd.shuffle(block_seq4)
   # experiment-array for one participant (3 runs, 36 blocks each)
   # the order of block_seq-presentation in the runs is also randomized, this is already implemented in the psychopy-experiment-script
   sequences = [block_seq1] + [block_seq2] + [block_seq3] + [block_seq4]

   # set counter for runfiles (1, 2, 3)
   counter = 1

   for x in sequences:
       # randomize the stimulus-order
       rd.shuffle(stim_voice)
       rd.shuffle(stim_song)
       rd.shuffle(stim_music)

       # sort randomized stimuli into blocks of same modalities (5 stimuli/block, 12 blocks for each modality in total)
       blocks_voice = np.split(stim_voice, 12)
       blocks_song = np.split(stim_song, 12)
       blocks_music = np.split(stim_music, 12)

       # set indices
       voice_index = 0
       song_index = 0
       music_index = 0

       # create a csv-file
       ofile = open('run%i.csv' % counter, 'w')
       ofile.write('run,stimuli,block\n')
       counterbalance = 4
       # sort the block_modalities (blocks_voice, blocks_song, blocks_music) by the sequences for the 3 runs
       # write information about run, stimuli, blocks into csv-file
       # the delay-sequences between blocks are separately implemented within the psychopy-script
       for y in range(len(x)):
           if x[y] == 'voice':
               temp = blocks_voice[voice_index]
               for number in temp:
                   ofile.write('%s,"voice/voice_%s.wav","block_%s"\n' % (counter, number, x[y]))
               #ofile.write('%s,"pause:%s"\n' % (counter, inter_block_delay[y]))
               voice_index = voice_index +1
               print('voice',voice_index)
           elif x[y] == 'song':
               temp = blocks_song[song_index]
               for number in temp:
                   ofile.write('%s,"song/song_%s.wav","block_%s"\n' % (counter, number, x[y]))
               #ofile.write('%s,"pause:%s"\n' % (counter, inter_block_delay[y]))
               song_index = song_index +1
               print('song',song_index)
           elif x[y] == 'music':
               temp = blocks_music[music_index]
               for number in temp:
                   ofile.write('%s,"music/music_%s.wav","block_%s"\n' % (counter, number, x[y]))
               #ofile.write('%s,"pause:%s"\n' % (counter, inter_block_delay[y]))
               music_index = music_index +1
               print('music',music_index)

       ofile.close()
       counter = counter + 1
       
#gen_runfiles()
