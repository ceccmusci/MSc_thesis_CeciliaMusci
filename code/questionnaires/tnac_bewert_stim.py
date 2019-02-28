# Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
# Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008


from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                            STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
               sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import pandas as pd
import sys     ##encode utf-8 inklusiv umlaut
reload(sys)
sys.setdefaultencoding("utf-8")


def update(teil_a,teil_b,teil_c,firsttrial,check):

#gui #0
    if check ==0:
        myDlg = gui.Dlg(title=u'Bewertung der gehoerten Stimuli')
        myDlg.addText('A. Gesprochene Saetze')
        myDlg.addField(u'1. Wie viele der eben gehoerten gesprochenen Saetze haben sie inhaltlich verstanden?',choices=[u'keine',u'weniger als 10 (von insgesamt 60)',u'mindestens 10 - weniger als 20 (von insgesamt 60)',u'mindestens 20- weniger als 30 (von insgesamt 60)',u'mindestens 30 der 60 praesentierten Stimuli'],initial=teil_a[0])

        if teil_a[0] == '' or firsttrial==0:
            myDlg.addField(u'2. Geben Sie bitte hier die Sprache(n) an, die Sie bei den gesprochenen Stimuli verstanden haben:',initial=teil_a[1])
        elif teil_a[1] == '' and firsttrial==1:
            myDlg.addField(u'2. Geben Sie bitte hier die Sprache(n) an, die Sie bei den gesprochenen Stimuli verstanden haben:',initial=teil_a[1],color='red')
        else:
            myDlg.addField(u'2. Geben Sie bitte hier die Sprache(n) an, die Sie bei den gesprochenen Stimuli verstanden haben:',initial=teil_a[1])

        # show and return data
        myDlg.show()
        myDlg = myDlg.data
        print(myDlg)

        return myDlg,teil_b,teil_c

#gui #1

    if check ==1:
        myDlg1 = gui.Dlg(title=u'Bewertung der gehoerten Stimuli')
        myDlg1.addText('B. Ausschnitte von Gesaengen')

        myDlg1.addField(u'1. Wie viele der eben gehoerten Gesangsausschnitte haben sie inhaltlich verstanden?',choices=[u'keine',u'weniger als 10 (von insgesamt 60)',u'mindestens 10- weniger als 20 (von insgesamt 60)',u'mindestens 20- weniger als 30 (von insgesamt 60)',u'mindestens 30 der 60 praesentierten Stimuli'],initial=teil_b[0])

        if teil_b[0] == '' or firsttrial==0:
             myDlg1.addField(u'2. Geben Sie bitte hier die Sprache(n) an, die Sie bei den Gesangsausschnitten verstanden haben:',initial=teil_b[1])
        elif teil_b[1] == '' and firsttrial==1:
            myDlg1.addField(u'2. Geben Sie bitte hier die Sprache(n) an, die Sie bei den Gesangsausschnitten verstanden haben:',initial=teil_b[1],color='red')
        else:
             myDlg1.addField(u'2. Geben Sie bitte hier die Sprache(n) an, die Sie bei den Gesangsausschnitten verstanden haben:',initial=teil_b[1])


        myDlg1.addField(u'3. Wie viele der eben gehoerten Gesangsausschnitte kamen Ihnen bekannt vor?',choices=[u'keine',u'weniger als 10 (von insgesamt 60)',u'mindestens 10- weniger als 20 (von insgesamt 60)',u'mindestens 20- weniger als 30 (von insgesamt 60)',u'mindestens 30 der 60 praesentierten Stimuli'],initial=teil_b[2])

        if teil_b[2] == '' or firsttrial==0:
            myDlg1.addField(u'Falls Ihnen etwas bekannt vorkam, bitte erlaeutern Sie:',initial=teil_b[3])
        elif not teil_b[2] == '' and firsttrial==1:
            if (teil_b[2] == 'weniger als 10 (von insgesamt 60)' or teil_b[2] == 'mindestens 10 - weniger als 20 (von insgesamt 60)' or teil_b[2] == 'mindestens 20 - weniger als 30 (von insgesamt 60)' or  teil_b[2] == 'mindestens 30 der 60 praesentierten Stimuli') and teil_b[3] == '':
                myDlg1.addField(u'Falls Ihnen etwas bekannt vorkam, bitte erlaeutern Sie:',initial=teil_b[3],color='red')
            else:
                myDlg1.addField(u'Falls Ihnen etwas bekannt vorkam, bitte erlaeutern Sie:',initial=teil_b[3])

        # show and return data
        myDlg1.show()
        myDlg1 = myDlg1.data
        print(myDlg1)

        return teil_a,myDlg1,teil_c


#gui #2
    if check ==2:
        myDlg2 = gui.Dlg(title=u'Bewertung der gehoerten Stimuli')
        myDlg2.addText('C. Ausschnitte von Musikstuecken')

        myDlg2.addField(u'3. Wie viele der eben gehoerten Ausschnitte von Musikstuecken kamen Ihnen bekannt vor?',choices=[u'keine',u'weniger als 10 (von insgesamt 60)',u'mindestens 10 - weniger als 20 (von insgesamt 60)',u'mindestens 20 - weniger als 30 (von insgesamt 60)',u'mindestens 30 der 60 praesentierten Stimuli'],initial=teil_c[0])

        if teil_c[0] == '' or firsttrial==0:
            myDlg2.addField(u'Falls Ihnen etwas bekannt vorkam, bitte erlaeutern Sie:',initial=teil_c[1])
        elif not teil_c[0] == '' and firsttrial==1:
            if (teil_c[0] == 'weniger als 10 (von insgesamt 60)' or teil_c[0] == 'mindestens 10 - weniger als 20 (von insgesamt 60)' or teil_c[0] == 'mindestens 20 - weniger als 30 (von insgesamt 60)' or  teil_c[0] == 'mindestens 30 der 60 praesentierten Stimuli') and teil_c[1] == '':
                myDlg2.addField(u'Falls Ihnen etwas bekannt vorkam, bitte erlaeutern Sie:',initial=teil_c[1],color='red')
            else:
                myDlg2.addField(u'Falls Ihnen etwas bekannt vorkam, bitte erlaeutern Sie:',initial=teil_c[1])

        # show and return data
        myDlg2.show()

        myDlg2 = myDlg2.data
        print(myDlg2)
        return teil_a,teil_b,myDlg2


def savecvs(teil_a,teil_b,teil_c, filename,num_items,num_items_1,num_items_2):
    # function to add data to experiment handler and save as csv
    # add column + data

        keys = [''] * num_items
        keys1 = ['']*num_items_1
        keys2 = ['']*num_items_2

        keys[0] = 'Saetze verstanden'
        keys[1] = 'S Sprache(n) verstanden'

        keys1[0] = 'Gesangsausschnitte verstanden'
        keys1[1] = 'GA Sprache(n) verstanden'
        keys1[2] = 'GA bekannt'
        keys1[3] = 'GA bekannt erlaeutern'

        keys2[0] = 'Ausschnitte von Musikstuecken bekannt'
        keys2[1] = 'AM bekannt erlaeutern'


        file_open = open(filename + '.csv','w')
        for i in range(num_items):
            file_open.write(keys[i]+',')

        for i in range(num_items_1):
            file_open.write(keys1[i]+',')

        for i in range(num_items_2):
            file_open.write(keys2[i]+',')
        file_open.write('\n')


        for i in range(len(teil_a)):
            teil_a[i] = teil_a[i].replace(',',':')
            file_open.write(teil_a[i]+',')

        for i in range(len(teil_b)):
            teil_b[i] = teil_b[i].replace(',',':')
            file_open.write(teil_b[i]+',')

        for i in range(len(teil_c)):
            teil_c[i] = teil_c[i].replace(',',':')
            if i == len(teil_c)-1:
                file_open.write(teil_c[i]+',')
            else:
                file_open.write(teil_c[i]+',')

        file_open.close()

def check_values(teil_a,teil_b,teil_c,check):


    if check==0:
        if teil_a[1] == '':
            return 0
        else:
            return 1

    elif check==1:
        if teil_b[1] == '':
            return 1
        elif not teil_b[2] == 'keine' and teil_b[3] == '':
            return 1
        else:
            return 2

    elif check==2:
        if not teil_c[0] == 'keine' and teil_c[1] == '':
            return 2
        else:
            return 3


def bewertung_stimuli_func():
    # main function
# Ensure that relative paths start from the same directory as this script
    _thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
    os.chdir(_thisDir)
    expInfo = {'participant':'', 'session':'001'}
    dlg = gui.DlgFromDict(dictionary=expInfo, title='Questionnaire')
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    expInfo['date'] = data.getDateStr()  # add a simple timestamp


# Store info about the experiment session
    expName = u'bewertung_stimuli' # from the Builder filename that created this script

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    #filename = _thisDir + os.sep + u'data/%s' %(expName)
    filename = _thisDir + os.sep + u'%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
# An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='', runtimeInfo=None,
      originPath=None,
      savePickle=True, saveWideText=True,
      dataFileName=filename)
# save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

    # create empty list to store data and help determine status of question
    num_items = 2
    teil_a = [''] * num_items
    print teil_a

    num_items_1 = 4
    teil_b = [''] * num_items_1
    print teil_b

    num_items_2 = 2
    teil_c = [''] * num_items_2
    print teil_c

    # create variable which ensures that the first run of the test has now questions marked as unanswered
    firsttrial=0
    # create variable to check if question has been answered
    check = 0

    temp_Dlg = []
    # while loop calls update function, then checks for missing values, then update trialstatus and call save func
    while check <3:
        temp_Dlg = update (teil_a,teil_b,teil_c,firsttrial,check)
        temp_check = check
        print(temp_check)
        check = check_values(temp_Dlg[0],temp_Dlg[1],temp_Dlg[2],check)
        print(check)
        if temp_check == check:
           firsttrial=1
        else:
            firsttrial=0

        teil_a = temp_Dlg[0]
        print(teil_a)
        teil_b = temp_Dlg[1]
        print(teil_b)
        teil_c = temp_Dlg[2]
        print(teil_c)
    savecvs(teil_a,teil_b,teil_c,filename,num_items, num_items_1, num_items_2)
        # make sure everything is closed down
    thisExp.abort()  # or data files will save again on exit

bewertung_stimuli_func()
