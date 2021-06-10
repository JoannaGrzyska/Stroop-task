#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on czerwiec 10, 2021, at 17:23
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'stroop'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\atwa2\\Desktop\\STROOP TASK\\stroop.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
instrbox = visual.TextBox2(
     win, text='INSTRUKCJA WYKONANIA ZADANIA\n\nW zadaniu, które za chwilę wykonasz, na ekranie pojawiać się będą nazwy kolorów (NIEBIESKI, ZIELONY, ŻÓŁTY, CZERWONY) w różnych kolorach czcionki. Twoim zadaniem będzie wskazanie KOLORU CZCIONKI danego słowa, ignorując przy tym znaczenie tego słowa.\nWskazanie koloru będzie polegało na naciśnięciu klawisza na klawiaturze, odpowiadającemu danemu kolorowi:\n\n„z” dla koloru niebieskiego\n„x” dla koloru zielonego\n„n” dla koloru żółtego\n„m” dla koloru czerwonego\n\nPRZYKŁAD: Jeśli zobaczysz słowo CZERWONY (którego kolor czcionki będzie zielony), naciśnij klawisz „x” dla koloru zielonego, niezależnie od tego, co oznacza wyświetlone słowo.\nNIEBIESKI - naciśnij klawisz „z” dla koloru niebieskiego (bo kolor czcionki jest niebieski)\nŻÓŁTY - naciśnij klawisz „m” dla koloru czerwonego (bo kolor czcionki jest czerwony)\nOprócz słów, czasem na ekranie pojawiać będą się litery w różnych kolorach. Twoje zadanie w takim przypadku jest takie samo – wskazanie jakiego koloru są litery poprzez naciśnięcie odpowiedniego klawisza na klawiaturze (poszczególne kolory odpowiadają tym samym klawiszom, co w przypadku wyświetlanych słów)\nPostaraj się odpowiadać poprawnie i jak najszybciej, gdyż mierzony będzie czas Twojej reakcji.\n\nZanim rozpocznie się sesja eksperymentalna, zostaniesz poddany sesji treningowej, która ułatwi Ci zrozumienie zadania. W trakcie sesji treningowej, po każdej udzielonej odpowiedzi zostaniesz poinformowany o tym, czy Twoja odpowiedź była poprawna czy błędna. Informacja o poprawności nie będzie się pojawiać w sesji eksperymentalnej.\n\n\nAby rozpocząć, naciśnij spację.', font='Open Sans',
     pos=(0, 0),     letterHeight=0.02,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor='#ffffff',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='instrbox',
     autoLog=True,
)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "reminder"
reminderClock = core.Clock()
remind = visual.TextStim(win=win, name='remind',
    text='Zadanie zaraz się rozpocznie.\n\nUmieść środkowy i wskazujący palec lewej ręki na klawiszach „z” i „x” oraz środkowy i wskazujący palec prawej ręki na klawiszach „n” i „m”.\nSkup swój wzrok na znaku „+” i pamiętaj by udzielać odpowiedzi jak najszybciej.\n\nGdy będziesz gotowy/a naciśnij spację.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
target = visual.TextStim(win=win, name='target',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
response = keyboard.Keyboard()
key_remind = visual.TextStim(win=win, name='key_remind',
    text='z = niebieski   x = zielony   n = żółty   m = czerwony',
    font='Open Sans',
    pos=(0, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
win.mouseVisible = False
# Initialize components for Routine "reminder"
reminderClock = core.Clock()
remind = visual.TextStim(win=win, name='remind',
    text='Zadanie zaraz się rozpocznie.\n\nUmieść środkowy i wskazujący palec lewej ręki na klawiszach „z” i „x” oraz środkowy i wskazujący palec prawej ręki na klawiszach „n” i „m”.\nSkup swój wzrok na znaku „+” i pamiętaj by udzielać odpowiedzi jak najszybciej.\n\nGdy będziesz gotowy/a naciśnij spację.',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
target = visual.TextStim(win=win, name='target',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
response = keyboard.Keyboard()
key_remind = visual.TextStim(win=win, name='key_remind',
    text='z = niebieski   x = zielony   n = żółty   m = czerwony',
    font='Open Sans',
    pos=(0, 0.3), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "END"
ENDClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='To już koniec eksperymentu. Serdecznie dziękujemy za udział w badaniu!',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instructionComponents = [instrbox, key_resp]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrbox* updates
    if instrbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrbox.frameNStart = frameN  # exact frame index
        instrbox.tStart = t  # local t and not account for scr refresh
        instrbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrbox, 'tStartRefresh')  # time at next scr refresh
        instrbox.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instrbox.started', instrbox.tStartRefresh)
thisExp.addData('instrbox.stopped', instrbox.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "reminder"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
reminderComponents = [remind, key_resp_2]
for thisComponent in reminderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
reminderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "reminder"-------
while continueRoutine:
    # get current time
    t = reminderClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=reminderClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *remind* updates
    if remind.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        remind.frameNStart = frameN  # exact frame index
        remind.tStart = t  # local t and not account for scr refresh
        remind.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(remind, 'tStartRefresh')  # time at next scr refresh
        remind.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in reminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "reminder"-------
for thisComponent in reminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('remind.started', remind.tStartRefresh)
thisExp.addData('remind.stopped', remind.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "reminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stroop colors.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    target.setColor(color, colorSpace='rgb')
    target.setText(word)
    response.keys = []
    response.rt = []
    _response_allKeys = []
    # keep track of which components have finished
    trialComponents = [target, fix, response, key_remind]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target* updates
        if target.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        if target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                target.tStop = t  # not accounting for scr refresh
                target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
                target.setAutoDraw(False)
        
        # *fix* updates
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                fix.setAutoDraw(False)
        
        # *response* updates
        waitOnFlip = False
        if response.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            response.frameNStart = frameN  # exact frame index
            response.tStart = t  # local t and not account for scr refresh
            response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response.status == STARTED and not waitOnFlip:
            theseKeys = response.getKeys(keyList=['x', 'z', 'n', 'm'], waitRelease=False)
            _response_allKeys.extend(theseKeys)
            if len(_response_allKeys):
                response.keys = _response_allKeys[-1].name  # just the last key pressed
                response.rt = _response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *key_remind* updates
        if key_remind.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_remind.frameNStart = frameN  # exact frame index
            key_remind.tStart = t  # local t and not account for scr refresh
            key_remind.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_remind, 'tStartRefresh')  # time at next scr refresh
            key_remind.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('target.started', target.tStartRefresh)
    trials_2.addData('target.stopped', target.tStopRefresh)
    trials_2.addData('fix.started', fix.tStartRefresh)
    trials_2.addData('fix.stopped', fix.tStopRefresh)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
    trials_2.addData('response.keys',response.keys)
    if response.keys != None:  # we had a response
        trials_2.addData('response.rt', response.rt)
    trials_2.addData('response.started', response.tStartRefresh)
    trials_2.addData('response.stopped', response.tStopRefresh)
    trials_2.addData('key_remind.started', key_remind.tStartRefresh)
    trials_2.addData('key_remind.stopped', key_remind.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# ------Prepare to start Routine "reminder"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
reminderComponents = [remind, key_resp_2]
for thisComponent in reminderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
reminderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "reminder"-------
while continueRoutine:
    # get current time
    t = reminderClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=reminderClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *remind* updates
    if remind.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        remind.frameNStart = frameN  # exact frame index
        remind.tStart = t  # local t and not account for scr refresh
        remind.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(remind, 'tStartRefresh')  # time at next scr refresh
        remind.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in reminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "reminder"-------
for thisComponent in reminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('remind.started', remind.tStartRefresh)
thisExp.addData('remind.stopped', remind.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "reminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=10.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stroop colors.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    target.setColor(color, colorSpace='rgb')
    target.setText(word)
    response.keys = []
    response.rt = []
    _response_allKeys = []
    # keep track of which components have finished
    trialComponents = [target, fix, response, key_remind]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target* updates
        if target.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        if target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                target.tStop = t  # not accounting for scr refresh
                target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
                target.setAutoDraw(False)
        
        # *fix* updates
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                fix.setAutoDraw(False)
        
        # *response* updates
        waitOnFlip = False
        if response.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            response.frameNStart = frameN  # exact frame index
            response.tStart = t  # local t and not account for scr refresh
            response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response.status == STARTED and not waitOnFlip:
            theseKeys = response.getKeys(keyList=['x', 'z', 'n', 'm'], waitRelease=False)
            _response_allKeys.extend(theseKeys)
            if len(_response_allKeys):
                response.keys = _response_allKeys[-1].name  # just the last key pressed
                response.rt = _response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *key_remind* updates
        if key_remind.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_remind.frameNStart = frameN  # exact frame index
            key_remind.tStart = t  # local t and not account for scr refresh
            key_remind.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_remind, 'tStartRefresh')  # time at next scr refresh
            key_remind.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('target.started', target.tStartRefresh)
    trials.addData('target.stopped', target.tStopRefresh)
    trials.addData('fix.started', fix.tStartRefresh)
    trials.addData('fix.stopped', fix.tStopRefresh)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
    trials.addData('response.keys',response.keys)
    if response.keys != None:  # we had a response
        trials.addData('response.rt', response.rt)
    trials.addData('response.started', response.tStartRefresh)
    trials.addData('response.stopped', response.tStopRefresh)
    trials.addData('key_remind.started', key_remind.tStartRefresh)
    trials.addData('key_remind.stopped', key_remind.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 10.0 repeats of 'trials'


# ------Prepare to start Routine "END"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
ENDComponents = [end_text]
for thisComponent in ENDComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ENDClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "END"-------
while continueRoutine:
    # get current time
    t = ENDClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ENDClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ENDComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "END"-------
for thisComponent in ENDComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_text.started', end_text.tStartRefresh)
thisExp.addData('end_text.stopped', end_text.tStopRefresh)
# the Routine "END" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
