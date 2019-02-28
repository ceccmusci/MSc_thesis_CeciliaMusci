import os
import pandas as pd
from scipy.stats import norm
import numpy as np
import csv
import glob

# where to store the analysed data
output_path = '/home/ceccmusci/cecilia/uni/msc_kis/tnac/data/data_questionnaires/data_met/analysed_met/%s_analysed.csv'
#  find csv files in the current directory
paths = glob.glob('/home/ceccmusci/cecilia/uni/msc_kis/tnac/data/data_questionnaires/data_met/*.csv')


for path in paths:
    print(path)
    subject = os.path.split(path)[1].split(sep='_')[0]

    df = pd.read_csv(path)

    # ANALYSIS
    answers_melody = df[['phrases_sounds','reaction_mel_key.keys','target_mel','reaction_mel_key.corr', 'reaction_mel_key.rt']][0:52]
    answers_rhythm = df[['rhythm_sounds','reaction_rhy_key.keys','target_rhy','reaction_rhy_key.corr', 'reaction_rhy_key.rt']][52:104]

    answers_melody_corr = answers_melody['reaction_mel_key.corr'].sum()
    melody1_corr_percent = answers_melody_corr/52
    answers_rhythm_corr = answers_rhythm['reaction_rhy_key.corr'].sum()
    rhythm_corr_percent = answers_rhythm_corr/52
    print(answers_melody_corr)
    print(answers_melody)

    hit_melody = 0
    falsealarm_melody=0
    for i in range(0,0 + len(answers_melody['target_mel'])):
        if answers_melody['target_mel'][i] == 'n' and answers_melody['reaction_mel_key.keys'][i] == 'n':
            hit_melody += 1
        elif answers_melody['target_mel'][i] == 'j' and answers_melody['reaction_mel_key.keys'][i] == 'n':
            falsealarm_melody += 1
    # positive answers relative to all positive targets - correctly answered positive ansers
    hitrate_melody = hit_melody/26.0
    # amount of negative answers given for positive targets - falsely positive evaluated objects
    falsealarmrate_melody = falsealarm_melody/26.0
    # d' = Z(hit rate) − Z(false alarm rate
    answers_mel_dprime = norm.ppf(hitrate_melody)-norm.ppf(falsealarmrate_melody)
    answers_mel_dprime_c = -0.5*(norm.ppf(hitrate_melody)+norm.ppf(falsealarmrate_melody))

    hit_rhythm = 0
    falsealarm_rhythm=0
    for i in range(52,52 + len(answers_rhythm['target_rhy'])):
        if answers_rhythm['target_rhy'][i] == 'n' and answers_rhythm['reaction_rhy_key.keys'][i] == 'n':
            hit_rhythm += 1
        elif answers_rhythm['target_rhy'][i] == 'y' and answers_rhythm['reaction_rhy_key.keys'][i] == 'n':
            falsealarm_rhythm += 1
    # positive answers relative to all positive targets - correctly answered positive ansers
    hitrate_rhythm = hit_rhythm/26.0
    # amount of negative answers given for positive targets - falsely positive evaluated objects
    falsealarmrate_rhythm = falsealarm_rhythm/26.0
    # d' = Z(hit rate) − Z(false alarm rate
    answers_rhy_dprime = norm.ppf(hitrate_rhythm)-norm.ppf(falsealarmrate_rhythm)
    answers_rhy_dprime_c = -0.5*(norm.ppf(hitrate_rhythm)+norm.ppf(falsealarmrate_rhythm))


    # either write to new csv (looks way cleaner) or append to existing data
    file_open = open(output_path % subject, 'a')

    keys= ['answers_melody_corr','hit_melody','falsealarm_melody','hitrate_melody','falsealarmrate_melody','answers_mel_dprime','answers_mel_dprime_c',
                    'answers_rhythm_corr','hit_rhythm','falsealarm_rhythm','hitrate_rhythm','falsealarmrate_rhythm','answers_rhy_dprime','answers_rhy_dprime_c']
    values=[answers_melody_corr,hit_melody,falsealarm_melody,hitrate_melody,falsealarmrate_melody,answers_mel_dprime,answers_mel_dprime_c,answers_rhythm_corr,hit_rhythm,falsealarm_rhythm,hitrate_rhythm,falsealarmrate_rhythm,answers_rhy_dprime,answers_rhy_dprime_c]

    for i in range(len(keys)):
        if i == len(keys) - 1:
            file_open.write(keys[i])
        else:
            file_open.write(keys[i]+',')

    file_open.write('\n')

    for i in range(len(values)):
        if i == len(values) - 1:
            file_open.write(str(values[i]))
        else:
            file_open.write(str(values[i])+',')

    file_open.close()
