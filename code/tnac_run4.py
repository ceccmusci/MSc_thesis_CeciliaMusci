#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.3),
    on Tue 26 Jun 2018 03:46:44 PM CEST
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

#from __future__ import absolute_import, division
from psychopy import visual
from psychopy import locale_setup, sound, gui, core, data, event, logging, parallel

import psychopy
psychopy.useVersion('1.85.3')

from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import random
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

## TODO find out port number
p_port=parallel.ParallelPort(address='0xD010') #set up a class
p_port.setData(0) #clear out the pport

#port = parallel.ParallelPort(adress=0x03BC)

# TODO reinstate:
def send_trigger(trg):
    #TODO test if core.wait statements fuck up stimuli intervall
    """Send a trigger :D"""
    p_port.setData(0)
    core.wait(.0025)
    p_port.setData(trg)

    core.wait(0.005)
    p_port.setData(0)

def run4_func(expInfo):
    # main function
# Ensure that relative paths start from the same directory as this script
    _thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
    os.chdir(_thisDir)

# Store info about the experiment session
    expName = u'tnac_exp' # from the Builder filename that created this script
    expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

    trg_dict = {"music": 1,
                "voice": 2,
                "song": 3,
                "sound_off": 100,
                "pause_block": 200,
                "stop_run": 300,
                "start_run": 400,
                "start_block": 500,
                }


    #define path to csvs
    run_var= _thisDir+'/run4.csv'
    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath=None,
        savePickle=True, saveWideText=True,
        dataFileName=filename)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

    endExpNow = False  # flag for 'escape' or other condition => quit the exp

    # Start Code - component code to be run before the window creation

    # Setup the Window
    ## TODO: set window to fullscreen
    win = visual.Window(
        size=[1366, 768], fullscr=True, screen=0,
        allowGUI=True, allowStencil=False,
        monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
        blendMode='avg', useFBO=True)
    # store frame rate of monitor if we can measure it
    expInfo['frameRate'] = win.getActualFrameRate()
    if expInfo['frameRate'] != None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess

    # Initialize components for Routine "trial"
    trialClock = core.Clock()
    stim_1 = sound.Sound('A', secs=-1)
    stim_1.setVolume(1)
    fix_1 = visual.TextStim(win=win, name='fix_1',
        text='+',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
        color='white', colorSpace='rgb', opacity=1,
        depth=-1.0);

    # Initialize components for Routine "run_start"
    run_startClock = core.Clock()
    run_start_msg_screen = visual.TextStim(win=win, name='run_start_msg_screen',
        text=u'Kurze Pause.',
        font='Arial',
        units='norm', pos=[0,0], height=0.12, wrapWidth=2, ori=0,
        color='white', colorSpace='rgb', opacity=1,
        depth=0.0);

    # Initialize components for Routine "run_trigger_sync"
    StartClock = core.Clock()
    run_trigger_syncClock = core.Clock()
    run_start_msg = visual.TextStim(win=win, name='run_start_msg',
        text='Durchgang beginnt!',
        font='Arial',
        units='norm', pos=[0, 0], height=0.15, wrapWidth=2, ori=0,
        color='white', colorSpace='rgb', opacity=1,
        depth=-1.0);
    movie = visual.MovieStim3(
        win=win, name='movie',units='pix',
        noAudio = True,
        # rename path
        filename='C:\Paradigmen\AG_Brain\Peer\TNAC\movies\mov4.mkv',
        ori=0, pos=(0, 0), opacity=1,
        depth=0.0,)

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine


    block_delay = [4,5,6]*12
    random.shuffle(block_delay)
    #print(block_delay)
    # ------Prepare to start Routine "run_start"-------
    t = 0
    run_startClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    run_start_trigger_key = event.BuilderKeyResponse()
    # keep track of which components have finished
    run_startComponents = [run_start_msg_screen, run_start_trigger_key]
    for thisComponent in run_startComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "run_start"-------
    while continueRoutine:
        # get current time
        t = run_startClock.getTime()
        thisExp.addData('start_run',globalClock.getTime())
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *run_start_msg_screen* updates
        if t >= 0.0 and run_start_msg_screen.status == NOT_STARTED:
            # keep track of start time/frame for later
            run_start_msg_screen.tStart = t
            run_start_msg_screen.frameNStart = frameN  # exact frame index
            run_start_msg_screen.setAutoDraw(True)

        # *run_start_trigger_key* updates
        if t >= 0.0 and run_start_trigger_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            run_start_trigger_key.tStart = t
            run_start_trigger_key.frameNStart = frameN  # exact frame index
            run_start_trigger_key.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if run_start_trigger_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['s'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in run_startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "run_start"-------
    for thisComponent in run_startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "run_start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "run_trigger_sync"-------
    t = 0
    run_trigger_syncClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    run_trigger_sync_ = event.BuilderKeyResponse()

    # keep track of which components have finished
    run_trigger_syncComponents = [run_trigger_sync_, run_start_msg]
    for thisComponent in run_trigger_syncComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "run_trigger_sync"-------
    while continueRoutine:
        # get current time
        print('waiting for scanner trigger....')
        t = run_trigger_syncClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *run_trigger_sync_* updates
        if t >= 0.0 and run_trigger_sync_.status == NOT_STARTED:
            # keep track of start time/frame for later
            run_trigger_sync_.tStart = t
            run_trigger_sync_.frameNStart = frameN  # exact frame index
            run_trigger_sync_.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(run_trigger_sync_.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if run_trigger_sync_.status == STARTED:
            theseKeys = event.getKeys(keyList=['t'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                run_trigger_sync_.keys = theseKeys[-1]  # just the last key pressed
                run_trigger_sync_.rt = run_trigger_sync_.clock.getTime()
                # a response ends the routine
                continueRoutine = False

        # *run_start_msg* updates
        if t >= 0.0 and run_start_msg.status == NOT_STARTED:
            # keep track of start time/frame for later
            run_start_msg.tStart = t
            run_start_msg.frameNStart = frameN  # exact frame index
            run_start_msg.setAutoDraw(True)
        frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if run_start_msg.status == STARTED and t >= frameRemains:
            run_start_msg.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in run_trigger_syncComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "run_trigger_sync"-------
    for thisComponent in run_trigger_syncComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if run_trigger_sync_.keys in ['', [], None]:  # No response was made
        run_trigger_sync_.keys=None
    thisExp.addData('run_trigger_sync_.keys',run_trigger_sync_.keys)
    if run_trigger_sync_.keys != None:  # we had a response
        thisExp.addData('run_trigger_sync_.rt', run_trigger_sync_.rt)
    run_start_timestamp = StartClock.getTime()

    send_trigger(400)
    # the Routine "run_trigger_sync" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    start_delay=False
    delay_counter= 0
    #print(block_delay)
    #print(delay_counter)
    # start movie for whole run (loop over trials)
    mov='movies/mov4.mkv'
    #print(mov)
    movie.setMovie(mov)
    if t >= 0.0 and movie.status == NOT_STARTED:
        # keep track of start time/frame for later
        movie.tStart = t
        movie.frameNStart = frameN  # exact frame index
        movie.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left

        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=1, method='sequential',
            extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(run_var),
        seed=None, name='trials')
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        stimuli_played=0

        for thisTrial in trials:
            currentLoop = trials
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial.keys():
                    exec(paramName + '= thisTrial.' + paramName)

            # ------Prepare to start Routine "trial"-------
            t = 0
            trialClock.reset()  # clock
            frameN = -1
            continueRoutine = True

            routineTimer.add(2.000000)
            # update component parameters for each repeat
            stim_1.setSound(stimuli, secs=2)
            #read stimuli into dict and set port value
            abc= stimuli.split('/')[0]
            trg = trg_dict.get(abc, 100)
            # keep track of which components have finished
            trialComponents = [stim_1, fix_1]
            for thisComponent in trialComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "trial"-------
            while continueRoutine and routineTimer.getTime() > 0:


                # get current time
                t = trialClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # start/stop stim_1
                if t >= 0.0 and stim_1.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    stim_1.tStart = t
                    stim_1.frameNStart = frameN  # exact frame index

            ## TODO reinstate: send_trigger(abc)
                    #print(abc)
                    stim_1.play()  # start the sound (it finishes automatically)
                    send_trigger(trg) # send block specific trigger
                    # get time for stimuls start
                    thisExp.addData('stimulus_start_global',globalClock.getTime())
                    thisExp.addData('stimulus_start_routineTimer',routineTimer.getTime())
                    thisExp.addData('stimulus_start_',frameN)
                    #print(stim_1)
                    stimuli_played+=1
                    if stimuli_played%5 == 0:
                        start_delay=True
                    #print('stimuli_nr:'+str(stimuli_played))


                frameRemains = 0.0 + 1.5 - win.monitorFramePeriod * 0.75  # most of one frame period left
                #frameRemainsdelay = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if stim_1.status == STARTED and t >= frameRemains:
                    stim_1.stop()  # stop the sound (if longer than duration)
                    send_trigger(100) # send sound off trigger
                    # get info on stim end
                thisExp.addData('stimulus_end_global',globalClock.getTime())
                thisExp.addData('stimulus_end_routineTimer',routineTimer.getTime())

                # add delay intervall after 5 stimuli
                if stimuli_played %5 == 0 and start_delay and delay_counter != 35:
                    send_trigger(200)
                    delay=block_delay[delay_counter]
                    routineTimer.add(block_delay[delay_counter])
                    #frameRemainsdelay = 0.0 + 1.5 + delay - win.monitorFramePeriod * 0.75  # most of one frame period left
                    #print('delay='+str(delay_counter))
                    delay_counter +=1
                    thisExp.addData('delay_counter',block_delay[delay_counter])
                    thisExp.addData('block_end_global',globalClock.getTime())
                    start_delay=False
                
                if stim_1.status == STARTED and t >= frameRemains:
                    stim_1.stop()  # stop the sound (if longer than duration)
                    send_trigger(100) # send sound off trigger
                    # get info on stim end
                thisExp.addData('stimulus_end_global',globalClock.getTime())
                thisExp.addData('stimulus_end_routineTimer',routineTimer.getTime())
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished

                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()

                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()




            stim_1.stop()  # ensure sound has stopped at end of routine
            thisExp.nextEntry()

            # completed 1 repeats of 'trials'

        thisExp.nextEntry()



        # completed 1 repeats of 'block'

    if stimuli_played == 180:
        movie.setAutoDraw(False)
        send_trigger(300) # END RUN
        thisExp.saveAsWideText(filename+'run4'+'.csv')
        thisExp.saveAsPickle(filename+'run4')
        logging.flush()
        # make sure everything is closed down
        thisExp.abort()  # or data files will save again on exit
        win.close()