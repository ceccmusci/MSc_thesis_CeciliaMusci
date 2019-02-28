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

def update(list_,list_1,list_2,list_3,list_4,list_5,list_6,firsttrial,check):
# function to display Dialogue
    # assign gui to variable and define title

    if check ==0:
        myDlg = gui.Dlg(title=u'Screeningfragebogen zu musikalisch-sprachlichen Aspekten')
        myDlg.addText('Teil A')
        myDlg.addText(u'1. Bitte geben Sie vollstaendig Ihre Sprachkenntnisse an:')

        if not list_[0] == '' or firsttrial==0:
            myDlg.addField(u'Muttersprache:',initial=list_[0])
        else:
            myDlg.addField(u'Muttersprache:',initial=list_[0],color='red')


        myDlg.addField(u'Haben Sie eine oder mehrere Fremdsprachen gelernt?',choices=[u'ja',u'nein'],initial=list_[1])

        if list_[1] == 'nein' or firsttrial==0:
            myDlg.addField(u'Welche Fremdsprache(n):',initial=list_[2])
            myDlg.addField(u'Wann begonnen wurde zu lernen:',initial=list_[3])
            myDlg.addField(u'Wie lange gelernt wurde:',initial=list_[4])

        if list_[1] == 'ja' and firsttrial==1:
            if list_[2]== '':
                myDlg.addField(u'Welche Fremdsprache(n):',initial=list_[2],color='red')
            else:
                myDlg.addField(u'Welche Fremdsprache(n):',initial=list_[2])
            if list_[3] == '':
                myDlg.addField(u'Wann begonnen wurde zu lernen:',initial=list_[3],color='red')
            else:
                myDlg.addField(u'Wann begonnen wurde zu lernen:',initial=list_[3])
            if list_[4] == '':
                myDlg.addField(u'Wie lange gelernt wurde:',initial=list_[4],color='red')
            else:
                myDlg.addField(u'Wie lange gelernt wurde:',initial=list_[4])


        myDlg.addField(u'2. Sind Sie zweisprachig/mehrsprachig aufgewachsen (bitte ankreuzen)?',choices=[u'ja',u'nein'],initial=list_[5])
        if list_[5] == 'nein' or firsttrial==0:
            myDlg.addField(u'Geben Sie bitte die Zweitsprache/weitere Sprache an:',initial=list_[6])

        elif list_[5] == 'ja' and firsttrial==1:
            if list_[6] == '':
                myDlg.addField(u'Geben Sie bitte die Zweitsprache/weitere Sprache an:',initial=list_[6],color='red')
            else:
                myDlg.addField(u'Geben Sie bitte die Zweitsprache/weitere Sprache an:',initial=list_[6])

        myDlg.show()
        myDlg = myDlg.data
        return myDlg,list_1,list_2,list_3,list_4,list_5,list_6

    elif check ==1:
        print(firsttrial)
        myDlg1= gui.Dlg(title=u'Screeningfragebogen zu musikalisch-sprachlichen Aspekten')

        myDlg1.addText(u'3. Wurde bei Ihnen jemals folgendes diagnostiziert (bitte ankreuzen und erlaeutern)?')

        myDlg1.addField(u'Sprachentwicklungsstoerung:',choices=[u'ja',u'nein'],initial=list_1[0])
        if list_1[0] == 'nein' or firsttrial==0:
            myDlg1.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_1[1])

        elif (list_1[0] == 'ja' and list_1[1] == '') and firsttrial==1:
            myDlg1.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_1[1],color='red')
        elif (list_1[0] == 'ja' and not list_1[1]=='') and firsttrial==1:
            myDlg1.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_1[1])


        myDlg1.addField(u'Sprachstoerung:',choices=[u'ja',u'nein'],initial=list_1[2])
        if list_1[2] == 'nein' or firsttrial==0:
            myDlg1.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_1[3])

        elif (list_1[2] == 'ja' and list_1[3] == '') and firsttrial==1:
            myDlg1.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_1[3],color='red')
        elif (list_1[2] == 'ja' and not list_1[3]=='') and firsttrial==1:
            myDlg1.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_1[3])


        myDlg1.addField(u'Leserechtschreibschwaeche/Legasthenie:',choices=[u'ja',u'nein'],initial=list_1[4])
        if list_1[4] == 'nein' or firsttrial==0:
            myDlg1.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_1[5])
        elif (list_1[4] == 'ja' and list_1[5] == '') and firsttrial==1:
            myDlg1.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_1[5],color='red')
        elif (list_1[4] == 'ja' and not list_1[5]=='') and firsttrial==1:
            myDlg1.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_1[5])



        myDlg1.addField(u'Mittelohrentzuendung:',choices=[u'ja',u'nein'],initial=list_1[6])
        if list_1[6] == 'nein' or firsttrial==0:
            myDlg1.addField(u'Wenn ja, bitte erlaeutern Sie (Haeufigkeit, Staerke):',initial=list_1[7])

        elif (list_1[6] == 'ja' and list_1[7] == '') and firsttrial==1:
            myDlg1.addField(u'Wenn ja, bitte erlaeutern Sie (Haeufigkeit, Staerke):',initial=list_1[7],color='red')
        elif (list_1[6] == 'ja' and not list_1[7]=='') and firsttrial==1:
            myDlg1.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_1[7])


        myDlg1.show()
        myDlg1 = myDlg1.data
        return list_,myDlg1,list_2,list_3,list_4,list_5,list_6

    #GUI
    elif check ==2:
        myDlg2= gui.Dlg(title=u'Screeningfragebogen zu musikalisch-sprachlichen Aspekten')

        myDlg2.addText(u'4. Wurde bei Familienangehoerigen von Ihnen jemals folgendes diagnostiziert (Falls bekannt, bitte ankreuzen und erlaeutern)?')

        myDlg2.addField(u'Sprachentwicklungsstoerung:',choices=[u'ja',u'nein'],initial=list_2[0])
        if list_2[0] == 'nein' or firsttrial==0:
            myDlg2.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_2[1])

        elif (list_2[0] == 'ja' and list_2[1] == '') and firsttrial==1:
            myDlg2.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_2[1],color='red')
        elif (list_2[0] == 'ja' and not list_2[1]=='') and firsttrial==1:
            myDlg2.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_2[1])


        myDlg2.addField(u'Sprachstoerung:',choices=[u'ja',u'nein'],initial=list_2[2])
        if list_2[2] == 'nein' or firsttrial==0:
            myDlg2.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_2[3])

        elif (list_2[2] == 'ja' and list_2[3] == '') and firsttrial==1:
            myDlg2.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_2[3],color='red')
        elif (list_2[2] == 'ja' and not list_2[3]=='') and firsttrial==1:
            myDlg2.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_2[3])


        myDlg2.addField(u'Leserechtschreibschwaeche/Legasthenie:',choices=[u'ja',u'nein'],initial=list_2[4])
        if list_2[4] == 'nein' or firsttrial==0:
            myDlg2.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_2[5])
        elif (list_2[4] == 'ja' and list_2[5] == '') and firsttrial==1:
            myDlg2.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_2[5],color='red')
        elif (list_2[4] == 'ja' and not list_2[5]=='') and firsttrial==1:
            myDlg2.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_2[5])


        myDlg2.addField(u'Mittelohrentzuendung:',choices=[u'ja',u'nein'],initial=list_2[6])
        if list_2[6] == 'nein' or firsttrial==0:
            myDlg2.addField(u'Wenn ja, bitte erlaeutern Sie (Haeufigkeit, Staerke):',initial=list_2[7])

        elif (list_2[6] == 'ja' and list_2[7] == '') and firsttrial==1:
            myDlg2.addField(u'Wenn ja, bitte erlaeutern Sie (Haeufigkeit, Staerke):',initial=list_2[7],color='red')
        elif (list_2[6] == 'ja' and not list_2[7]=='') and firsttrial==1:
            myDlg2.addField(u'Wenn ja, bitte erlaeutern Sie:',initial=list_2[7])


        myDlg2.show()
        myDlg2 = myDlg2.data
        return list_,list_1,myDlg2,list_3,list_4,list_5,list_6


###gui
    elif check ==3:
        myDlg3 = gui.Dlg(title=u'Screeningfragebogen zu musikalisch-sprachlichen Aspekten')
        myDlg3.addText('Teil B')
        myDlg3.addText(u'1. Machen Sie im Moment aktiv Musik? Bitte entsprechend ankreuzen und erlaeutern:')

        myDlg3.addField(u'a. Ich spiele ein Instrument/mehrere Instrumente',choices=[u'ja',u'nein'],initial=list_3[0])

        if list_3[0] == 'nein' or firsttrial==0:
            myDlg3.addField(u'Wenn ja, bitte erlaeutern Sie, um welche(s) Instrument(e) es sich handelt:',initial=list_3[1])
            myDlg3.addField(u'wie viele Jahre gelernt wurde:',initial=list_3[2])
            myDlg3.addField(u'und wie haeufig Sie ueben (in Stunden/Woche):',initial=list_3[3])

        elif list_3[0] == 'ja' and firsttrial==1:
            if list_3[1] == '':
                myDlg3.addField(u'Wenn ja, bitte erlaeutern Sie, um welche(s) Instrument(e) es sich handelt:',initial=list_3[1],color='red')
            else:
                myDlg3.addField(u'Wenn ja, bitte erlaeutern Sie, um welche(s) Instrument(e) es sich handelt:',initial=list_3[1])
            if list_3[2] == '':
                myDlg3.addField(u'wie viele Jahre gelernt wurde:',initial=list_3[2],color='red')
            else:
                myDlg3.addField(u'wie viele Jahre gelernt wurde:',initial=list_3[2])
            if list_3[3] == '':
                myDlg3.addField(u'und wie haeufig Sie ueben (in Stunden/Woche):',initial=list_3[3],color='red')
            else:
                myDlg3.addField(u'und wie haeufig Sie ueben (in Stunden/Woche):',initial=list_3[3])


        myDlg3.addField(u'b. Ich singe in einem Chor',choices=[u'ja',u'nein'],initial=list_3[4])

        if list_3[4] == 'nein' or firsttrial==0:
            myDlg3.addField(u'Wenn ja, bitte erlaeutern Sie, seit wie vielen Jahren Sie ueben:',initial=list_3[5])
            myDlg3.addField(u'und wie haeufig Sie ueben (in Stunden/Woche):',initial=list_3[6])

        elif list_3[4] == 'ja' and firsttrial==1:
            if list_3[5] == '': ##added ceci 19.6
                myDlg3.addField(u'Wenn ja, bitte erlaeutern Sie, seit wie vielen Jahren Sie ueben:',initial=list_3[5],color='red')
            else: ##added
                myDlg3.addField(u'Wenn ja, bitte erlaeutern Sie, seit wie vielen Jahren Sie ueben:',initial=list_3[5])
            if list_3[6] == '':
                myDlg3.addField(u'und wie haeufig Sie ueben (in Stunden/Woche):',initial=list_3[6],color='red')
            else:
                myDlg3.addField(u'und wie haeufig Sie ueben (in Stunden/Woche):',initial=list_3[6])

        myDlg3.addField(u'c. anderes',choices=[u'ja',u'nein'],initial=list_3[7])

        if list_3[7] == 'nein' or firsttrial==0:
            myDlg3.addField(u'Wenn ja, bitte erlaeutern Sie andere musikalische Aktivitaeten:',initial=list_3[8])

        elif list_3[7] == 'ja' and firsttrial==1:
            if list_3[8] == '':
                myDlg3.addField(u'Wenn ja, bitte erlaeutern Sie andere musikalische Aktivitaeten:',initial=list_3[8],color='red')
            else:
                myDlg3.addField(u'Wenn ja, bitte erlaeutern Sie andere musikalische Aktivitaeten:',initial=list_3[8])


        myDlg3.show()
        myDlg3 = myDlg3.data
        return list_,list_1,list_2,myDlg3,list_4,list_5,list_6

    ###neue gui
    elif check ==4:
        myDlg4 = gui.Dlg(title=u'Screeningfragebogen zu musikalisch-sprachlichen Aspekten')
        myDlg4.addText(u'2. Haben Sie frueher aktiv Musik gemacht? Bitte entsprechend ankreuzen und erlaeutern:')

        myDlg4.addField(u'a. Ich habe ein Instrument/mehrere Instrumente gespielt',choices=[u'ja',u'nein'],initial=list_4[0])

        if list_4[0] == 'nein' or firsttrial==0:
            myDlg4.addField(u'Wenn ja, bitte erlaeutern Sie, um welche(s) Instrument(e) es sich handelte:',initial=list_4[1])
            myDlg4.addField(u'wie viele Jahre gelernt wurde:',initial=list_4[2])
            myDlg4.addField(u'und wie haeufig Sie geuebt haben (in Stunden/Woche):',initial=list_4[3])

        elif list_4[0] == 'ja' and firsttrial==1:
            if list_4[1] == '':
                myDlg4.addField(u'Wenn ja, bitte erlaeutern Sie, um welche(s) Instrument(e) es sich handelte:',initial=list_4[1],color='red')
            else:
                myDlg4.addField(u'Wenn ja, bitte erlaeutern Sie, um welche(s) Instrument(e) es sich handelte:',initial=list_4[1])
            if list_4[2] == '':
                myDlg4.addField(u'wie viele Jahre gelernt wurde:',initial=list_4[2],color='red')
            else:
                myDlg4.addField(u'wie viele Jahre gelernt wurde:',initial=list_4[2])
            if list_4[3] == '':
                myDlg4.addField(u'und wie haeufig Sie geuebt haben (in Stunden/Woche):',initial=list_4[3],color='red')
            else:
                myDlg4.addField(u'und wie haeufig Sie geuebt haben (in Stunden/Woche):',initial=list_4[3])


        myDlg4.addField(u'b. Ich habe in einem Chor gesungen',choices=[u'ja',u'nein'],initial=list_4[4])

        if list_4[4] == 'nein' or firsttrial==0:
            myDlg4.addField(u'Wenn ja, bitte erlaeutern Sie, wie viele Jahre Sie geuebt haben:',initial=list_4[5])
            myDlg4.addField(u'und wie haeufig Sie geuebt haben (in Stunden/Woche):',initial=list_4[6])
        elif list_4[4] == 'ja' and firsttrial==1:
            if list_4[5] == '':
                myDlg4.addField(u'Wenn ja, bitte erlaeutern Sie, wie viele Jahre Sie geuebt haben:',initial=list_4[5],color='red')
            else:
                myDlg4.addField(u'Wenn ja, bitte erlaeutern Sie, wie viele Jahre Sie geuebt haben:',initial=list_4[5])
            if list_4[6] == '':
                myDlg4.addField(u'und wie haeufig Sie geuebt haben (in Stunden/Woche):',initial=list_4[6],color='red')
            else:
                myDlg4.addField(u'und wie haeufig Sie geuebt haben (in Stunden/Woche):',initial=list_4[6])


        myDlg4.addField(u'c. anderes',choices=[u'ja',u'nein'],initial=list_4[7])

        if list_4[7] == 'nein' or firsttrial==0:
            myDlg4.addField(u'Wenn ja, bitte erlaeutern Sie andere musikalische Aktivitaeten:',initial=list_4[8])
        elif list_4[7] == 'ja' and firsttrial==1:
            if list_4[8] == '':
                myDlg4.addField(u'Wenn ja, bitte erlaeutern Sie andere musikalische Aktivitaeten:',initial=list_4[8],color='red')
            else:
                myDlg4.addField(u'Wenn ja, bitte erlaeutern Sie andere musikalische Aktivitaeten:',initial=list_4[8])

        myDlg4.show()
        myDlg4 = myDlg4.data
        return list_,list_1,list_2,list_3,myDlg4,list_5,list_6

    #GUI
    elif check ==5:
        myDlg5 = gui.Dlg(title=u'Screeningfragebogen zu musikalisch-sprachlichen Aspekten')

        myDlg5.addField(u'3. Erhalten Sie momentan privaten instrumentalen Musikunterricht (z.B. in einer Musikschule)?',choices=[u'ja', u'nein'],initial=list_5[0])

        if list_5[0] == 'nein' or firsttrial==0:
            myDlg5.addField(u'Wenn ja, bitte erlaeutern Sie, seit wie vielen Jahren:',initial=list_5[1])
            myDlg5.addField(u'und wie haeufig (in Stunden/Woche):',initial=list_5[2])
        elif list_5[0] == 'ja' and firsttrial==1:
            if list_5[1] == '':
                myDlg5.addField(u'Wenn ja, bitte erlaeutern Sie, seit wie vielen Jahren:',initial=list_5[1],color='red')
            else:
                myDlg5.addField(u'Wenn ja, bitte erlaeutern Sie, seit wie vielen Jahren:',initial=list_5[1])
            if list_5[2] == '':
                myDlg5.addField(u'und wie haeufig (in Stunden/Woche):',initial=list_5[2],color='red')
            else:
                myDlg5.addField(u'und wie haeufig (in Stunden/Woche):',initial=list_5[2])


        myDlg5.addField(u'4. Haben Sie jemals privaten instrumentalen Musikunterricht erhalten (z.B. in einer Musikschule)?',choices=[u'ja', u'nein'],initial=list_5[3])

        if list_5[3] == 'nein' or firsttrial==0:
            myDlg5.addField(u'Wenn ja, bitte erlaeutern Sie, fuer wie viele Jahre:',initial=list_5[4])
            myDlg5.addField(u'und wie haeufig (in Stunden/Woche):',initial=list_5[5])
        elif list_5[3] == 'ja' and firsttrial==1:
            if list_5[4] == '':
                myDlg5.addField(u'Wenn ja, bitte erlaeutern Sie, fuer wie viele Jahre:',initial=list_5[4],color='red')
            else:
                myDlg5.addField(u'Wenn ja, bitte erlaeutern Sie, fuer wie viele Jahre:',initial=list_5[4])
            if list_5[5] == '':
                myDlg5.addField(u'und wie haeufig (in Stunden/Woche):',initial=list_5[5],color='red')
            else:
                myDlg5.addField(u'und wie haeufig (in Stunden/Woche):',initial=list_5[5])

        myDlg5.show()
        myDlg5 = myDlg5.data

        return list_,list_1,list_2,list_3,list_4,myDlg5,list_6


###gui
    elif check ==6:
        myDlg6 = gui.Dlg(title=u'Screeningfragebogen zu musikalisch-sprachlichen Aspekten')

        myDlg6.addField(u'5. Erhalten Sie momentan privaten Gesangsunterricht?',choices=[u'ja', u'nein'],initial=list_6[0])

        if list_6[0] == 'nein' or firsttrial==0:
            myDlg6.addField(u'Wenn ja, bitte erlaeutern Sie, seit wie vielen Jahren:',initial=list_6[1])
            myDlg6.addField(u'und wie haeufig (in Stunden/Woche):',initial=list_6[2])
        elif list_6[0] == 'ja' and firsttrial==1:
            if list_6[1] == '':
                myDlg6.addField(u'Wenn ja, bitte erlaeutern Sie, seit wie vielen Jahren:',initial=list_6[1],color='red')
            else:
                myDlg6.addField(u'Wenn ja, bitte erlaeutern Sie, seit wie vielen Jahren:',initial=list_6[1])
            if list_6[2] == '':
                myDlg6.addField(u'und wie haeufig (in Stunden/Woche):',initial=list_6[2],color='red')
            else:
                myDlg6.addField(u'und wie haeufig (in Stunden/Woche):',initial=list_6[2])


        myDlg6.addField(u'6. Haben Sie jemals privaten Gesangsunterricht erhalten?',choices=[u'ja', u'nein'],initial=list_6[3])
        if list_6[3] == 'nein' or firsttrial==0:
            myDlg6.addField(u'Wenn ja, bitte erlaeutern Sie, fuer wie viele Jahre:',initial=list_6[4])
            myDlg6.addField(u' und wie haeufig (in Stunden/Woche):',initial=list_6[5])
        elif list_6[3] == 'ja' and firsttrial==1:
            if list_6[4] == '':
                myDlg6.addField(u'Wenn ja, bitte erlaeutern Sie, fuer wie viele Jahre:',initial=list_6[4],color='red')
            else:
                myDlg6.addField(u'Wenn ja, bitte erlaeutern Sie, fuer wie viele Jahre:',initial=list_6[4])
            if list_6[5] == '':
                myDlg6.addField(u' und wie haeufig (in Stunden/Woche):',initial=list_6[5],color='red')
            else:
                myDlg6.addField(u' und wie haeufig (in Stunden/Woche):',initial=list_6[5])

        myDlg6.show()
        myDlg6 = myDlg6.data

        return list_,list_1,list_2,list_3,list_4,list_5,myDlg6

def savecvs(list_,list_1,list_2,list_3,list_4,list_5,list_6,filename,num_items,num_items_1,num_items_2,num_items_3,num_items_4,num_items_5,num_items_6):
    # function to add data to experiment handler and save as csv
    # add column + data

        keys = ['']*num_items
        keys1 = ['']*num_items_1
        keys2 = ['']*num_items_2
        keys3 = ['']*num_items_3
        keys4 = ['']*num_items_4
        keys5 = ['']*num_items_5
        keys6 = ['']*num_items_6

        keys[0] = 'Muttersprache'
        keys[1] = 'Fremdsprache(n)'
        keys[2] = 'Welche(n) FS'
        keys[3] = 'Wann FS begonnen'
        keys[4] = 'Wie lange FS'
        keys[5] = 'Zweitsprache'
        keys[6] = 'ZS erlaeutern'

        keys1[0] = 'Sprachentwicklungsstoerung'
        keys1[1] = 'SES erlaeutern'
        keys1[2] = 'Sprachstoerung'
        keys1[3] = 'SS erlaeutern'
        keys1[4] = 'Leserechtschreibschwaeche/Legasthenie'
        keys1[5] = 'LL erlaeutern'
        keys1[6] = 'Mittelohrentzuendung'
        keys1[7] = 'MOZ erlaeutern (Haeufigkeit - Staerke)'

        keys2[0] = 'Familie Sprachentwicklungsstoerung'
        keys2[1] = 'Fam SES erlaeutern'
        keys2[2] = 'Familie Sprachstoerung'
        keys2[3] = 'Fam SS erlaeutern'
        keys2[4] = 'Familie Leserechtschreibschwaeche/Legasthenie'
        keys2[5] = 'Fam LL erlaeutern'
        keys2[6] = 'Familie Mittelohrentzuendung'
        keys2[7] = 'Fam MOZ erlaeutern (Haeufigkeit - Staerke)'

        keys3[0] = 'Instrument spielen'
        keys3[1] = 'Welches Instrument'
        keys3[2] = 'I Jahre gelernt'
        keys3[3] = 'I Haeufigkeit ueben'
        keys3[4] = 'Chor singen'
        keys3[5] = 'C seit Jahren'
        keys3[6] = 'C Haeufigkeit ueben'
        keys3[7] = 'anderes'
        keys3[8] = 'anderes was'

        keys4[0] = 'Frueher Instrument spielen'
        keys4[1] = 'Fr welches Instrument'
        keys4[2] = 'Fr Jahre gelernt'
        keys4[3] = 'Fr Haeufigkeit geuebt'
        keys4[4] = 'Frueher Chor gesungen'
        keys4[5] = 'Fr C Jahre'
        keys4[6] = 'Fr C Haeufigkeit ueben'
        keys4[7] = 'anderes'
        keys4[8] = 'anderes was'

        keys5[0] = 'Momentan Musikunterricht'
        keys5[1] = 'MU seit Jahren'
        keys5[2] = 'MU Haeufigkeit ueben'
        keys5[3] = 'Frueher Musikunterricht'
        keys5[4] = 'Fr MU Jahre'
        keys5[5] = 'Fr Haeufigkeit geuebt'

        keys6[0] = 'Momentan Gesangsunterricht'
        keys6[1] = 'GU seit Jahren'
        keys6[2] = 'GU Haeufigkeit ueben'
        keys6[3] = 'Frueher Gesangsunterricht'
        keys6[4] = 'Fr GU Jahre'
        keys6[5] = 'Fr GU Haeufigkeit geuebt'

        file_open = open(filename + '.csv','w')
        for i in range(num_items):
            if i == num_items-1:
                file_open.write(keys[i]+',')
            else:
                file_open.write(keys[i]+',')

        for i in range(num_items_1):
            if i == num_items_1-1:
                file_open.write(keys1[i]+',')
            else:
                file_open.write(keys1[i]+',')

        for i in range(num_items_2):
            if i == num_items_2-1:
                file_open.write(keys2[i]+',')
            else:
                file_open.write(keys2[i]+',')

        for i in range(num_items_3):
            if i == num_items-1:
                file_open.write(keys3[i]+',')
            else:
                file_open.write(keys3[i]+',')

        for i in range(num_items_4):
            if i == num_items_1-1:
                file_open.write(keys4[i]+',')
            else:
                file_open.write(keys4[i]+',')

        for i in range(num_items_5):
            if i == num_items_2-1:
                file_open.write(keys5[i]+',')
            else:
                file_open.write(keys5[i]+',')

        for i in range(num_items_6):
            if i == num_items_2-1:
                file_open.write(keys6[i]+',')
            else:
                file_open.write(keys6[i]+',')
        file_open.write('\n')



        for i in range(len(list_)):
            list_[i] = list_[i].replace(',',':')
            if i == len(list_)-1:
                file_open.write(list_[i]+',')
            else:
                file_open.write(list_[i]+',')

        for i in range(len(list_1)):
            list_1[i] = list_1[i].replace(',',':')
            if i == len(list_1)-1:
                file_open.write(list_1[i]+',')
            else:
                file_open.write(list_1[i]+',')

        for i in range(len(list_2)):
            list_2[i] = list_2[i].replace(',',':')
            if i == len(list_2)-1:
                file_open.write(list_2[i]+',')
            else:
                file_open.write(list_2[i]+',')

        for i in range(len(list_3)):
            list_3[i] = list_3[i].replace(',',':')
            if i == len(list_3)-1:
                file_open.write(list_3[i]+',')
            else:
                file_open.write(list_3[i]+',')

        for i in range(len(list_4)):
            list_4[i] = list_4[i].replace(',',':')
            if i == len(list_4)-1:
                file_open.write(list_4[i]+',')
            else:
                file_open.write(list_4[i]+',')

        for i in range(len(list_5)):
            list_5[i] = list_5[i].replace(',',':')
            if i == len(list_5)-1:
                file_open.write(list_5[i]+',')
            else:
                file_open.write(list_5[i]+',')

        for i in range(len(list_6)):
            list_6[i] = list_6[i].replace(',',':')
            if i == len(list_6)-1:
                file_open.write(list_6[i]+',')
            else:
                file_open.write(list_6[i]+',')

        file_open.close()


def check_values(list_,list_1,list_2,list_3,list_4,list_5,list_6,check):

    if check ==0:
        if list_[0] == '':
            return 0
        elif list_[1] == 'ja' and (list_[2] == '' or list_[3] == '' or list_[4] == ''):
            return 0
        elif list_[5] == 'ja' and list_[6] == '':
            return 0
        else:
            return 1


    elif check==1:
        print(list_1)
        if list_1[0] == 'ja' and list_1[1] == '':
            print('a')

            return 1
        elif list_1[2] == 'ja' and list_1[3] == '':
            print(list_1[2])
            print(list_1[3])

            print('b')
            return 1
        elif list_1[4] == 'ja' and list_1[5] == '':
            print('c')
            return 1
        elif list_1[6] == 'ja' and list_1[7] == '':
            print('d')
            return 1
        else:
            return 2

    elif check==2:
        if list_2[0] == 'ja' and list_2[1] == '':
            return 2

        elif list_2[2] == 'ja' and list_2[3] == '':
            return 2

        elif list_2[4] == 'ja' and list_2[5] == '':
            return 2

        elif list_2[6] == 'ja' and list_2[7] == '':
            return 2

        else:
            return 3

####update

    elif check==3:
        if list_3[0] == 'ja' and (list_3[1] == '' or list_3[2] == '' or list_3[3] == ''):
            return 3

        elif list_3[4] == 'ja' and (list_3[5] == '' or list_3[6] == ''):
            return 3

        elif list_3[7] == 'ja' and list_3[8] == '':
            return 3

        else:
            return 4

    elif check==4:
        if list_4[0] == 'ja' and (list_4[1] == '' or list_4[2] == '' or list_4[3] == ''):
            return 4

        elif list_4[4] == 'ja' and (list_4[5] == '' or list_4[6] == ''):
            return 4

        elif list_4[7] == 'ja' and list_4[8] == '':
            return 4

        else:
            return 5
#####UPDATEN
    elif check==5:
        if list_5[0] == 'ja' and (list_5[1] == '' or list_5[2] == ''):
            return 5

        elif list_5[3] == 'ja' and (list_5[4] == '' or list_5[5] == ''):
            return 5

        else:
            return 6

    elif check==6:
        if list_6[0] == 'ja' and (list_6[1] == '' or list_6[2] == ''):
            return 6

        elif list_6[3] == 'ja'and (list_6[4] == '' or list_6[5] == ''):
            return 6

        else:
            return 7


def ling_music_func():
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
    expName = u'ling_music' # from the Builder filename that created this script


    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + u'data/%s' %(expName)

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='', runtimeInfo=None,
      originPath=None,
      savePickle=True, saveWideText=True,
      dataFileName=filename)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file


    # create empty list to store data and help determine status of question
    num_items = 7
    list_ = [''] * num_items
    print list_
#gui
    num_items_1 = 8
    list_1 = [''] * num_items_1
    print list_1
#GUI
    num_items_2 = 8
    list_2 = [''] * num_items_2
    print list_2
#gui
    num_items_3 = 9
    list_3 = [''] * num_items_3
    print list_3
#GUI '#neue gui wird die 4, die 4 wird 5 uns so weitere
    num_items_4 = 9
    list_4 = [''] * num_items_4
    print list_4
##gUI
    num_items_5 = 6
    list_5 = [''] * num_items_5
    print list_5
#gUI
    num_items_6 = 6
    list_6 = [''] * num_items_6
    print list_6

    # create variable which ensures that the first run of the test has now questions marked as unanswered
    firsttrial=0
    # create variable to check if question has been answered
    check = 0

    temp_Dlg = []
    # while loop calls update function, then checks for missing values, then update trialstatus and call save func
    while check <7:
        temp_Dlg = update (list_,list_1,list_2,list_3,list_4,list_5,list_6,firsttrial,check)
        temp_check = check
        print(temp_check)
        check = check_values(temp_Dlg[0],temp_Dlg[1],temp_Dlg[2],temp_Dlg[3],temp_Dlg[4],temp_Dlg[5],temp_Dlg[6],check)
        print(check)
        if temp_check == check:
            firsttrial=1
        else:
            firsttrial=0
        list_ = temp_Dlg[0]
        list_1= temp_Dlg[1]
        list_2= temp_Dlg[2]
        list_3= temp_Dlg[3]
        list_4= temp_Dlg[4]
        list_5= temp_Dlg[5]
        list_6= temp_Dlg[6]

      # ganz am ende
    savecvs(list_,list_1,list_2,list_3,list_4,list_5,list_6,filename,num_items,num_items_1,num_items_2,num_items_3,num_items_4,num_items_5,num_items_6)
      # make sure everything is closed down

    thisExp.abort()  # or data files will save again on exit

ling_music_func()
