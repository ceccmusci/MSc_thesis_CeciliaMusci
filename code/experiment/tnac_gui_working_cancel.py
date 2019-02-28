''' main gui - displays and updates list of runs'''
from __future__ import absolute_import, division
import psychopy
psychopy.useVersion('1.85.3')
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

import sys
reload(sys)
sys.setdefaultencoding('utf8')


import instruction
import tnac_run1
import tnac_run2
import tnac_run3
import tnac_run4
import gen_runfiles
import gen_subdir




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)
expInfo = {'participant':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title='questionaire')
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp



# defines layout of gui and updates status of runs after each run
def update(field1,field2,field3,field4,field5,field6,field7):
    # creates starting gui
    myDlg = gui.Dlg(title=u'questionaires')
    myDlg.addText(u'status: o = noch ausstehend  x = erledigt\n')
    # prompts static text field showing the status of each run
    myDlg.addText(field1 + '\tgenerate run files')
    myDlg.addText(field2 + '\tInstruction')
    myDlg.addText(field3 + '\trun 1')
    myDlg.addText(field4 + '\trun 2')
    myDlg.addText(field5 + '\trun 3')
    myDlg.addText(field6 + '\trun 4')
    myDlg.addText(field7 + '\tcreate praticipant directory')

    # create empty list to append to
    list_ = []
    # check status of each run and add still open runs to drop down men
    if field1 == 'o':
        list_.append('generate run files')
    if field2 == 'o':
        list_.append('Instruction')
    if field3 == 'o':
        list_.append('run 1')
    if field4 == 'o':
        list_.append('run 2')
    if field5 == 'o':
        list_.append('run 3')
    if field6 == 'o':
        list_.append('run 4')
    if field7 == 'o':
        list_.append('create praticipant directory')

    # prompt message when all runs are done, else print basic prompt and create drop down menu
    if len(list_) == 0 :
        myDlg.addText(u'\n Danke, sie sind nun fertig.')
    else:
        myDlg.addText(u'\n   Waehlen Sie die gewuenschte aus:')
        myDlg.addField(u'',choices=list_)
    myDlg.show()
    if myDlg.OK == False:
        core.quit()  # user pressed cancel
    return myDlg

# main func - defines starting values of each run and feeds the run modules into the gui
def questionaires_func():
    # create status icons/values for each run
    field1 = 'o'
    field2 = 'o'
    field3 = 'o'
    field4 = 'o'
    field5 = 'o'
    field6 = 'o'
    field7 = 'o'
    # call update function and add runs to menu
    myDlg = update(field1,field2,field3,field4,field5,field6,field7)

    # while loop allows updating the gui
    while not field1 == 'x' or not field2 == 'x' or not field3 == 'x' or not field4 == 'x'or not field5 == 'x'or not field6 == 'x'or not field7 == 'x':
        
        for i in myDlg.data:
            if 'generate run files' in myDlg.data:
                # generate run files for this session
                gen_runfiles.gen_runfiles()
                field1='x'
                myDlg = update(field1,field2,field3,field4,field5,field6,field7)
            elif 'Instruction' in myDlg.data:
                instruction.instruction(expInfo)
                field2= 'x'
                myDlg = update(field1,field2,field3,field4,field5,field6,field7)

            elif 'run 1' in myDlg.data:
                tnac_run1.run1_func(expInfo)
                field3= 'x'
                myDlg = update(field1,field2,field3,field4,field5,field6,field7)
            elif 'run 2' in myDlg.data:
                tnac_run2.run2_func(expInfo)
                field4= 'x'
                myDlg = update(field1,field2,field3,field4,field5,field6,field7)
            elif 'run 3' in myDlg.data:
                tnac_run3.run3_func(expInfo)
                field5= 'x'
                myDlg = update(field1,field2,field3,field4,field5,field6,field7)
            elif 'run 4' in myDlg.data:
                tnac_run4.run4_func(expInfo)
                field6= 'x'
                myDlg = update(field1,field2,field3,field4,field5,field6,field7)
            elif 'create praticipant directory' in myDlg.data:
                gen_subdir.gen_subdir(expInfo)
                field7= 'x'
                myDlg = update(field1,field2,field3,field4,field5,field6,field7)




#  call function

questionaires_func()
core.quit()
