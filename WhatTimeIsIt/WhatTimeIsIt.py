##############################################################
# Assetto Corsa App - What Time Is It
#
# Author: Christian Hiob
#
# www.subsonicpulse.de
#############################################################

#AC Documentation
#https://docs.google.com/document/d/13trBp6K1TjWbToUQs_nfFsB291-zVJzRZCNaTYt4Dzc/pub

import ac
from datetime import datetime
 
#called on plugin initialisation
#return plugin name
def acMain(ac_version):
	global appWindow, timeLabel
	appWindow=ac.newApp("Time")
	ac.setTitle(appWindow,"Time")
	ac.setSize(appWindow,160,60)
	ac.drawBorder(appWindow,0)
	ac.setBackgroundOpacity(appWindow,0)
	theTime=datetime.now()
	timeLabel=ac.addLabel(appWindow, "{}".format(theTime.strftime("%H:%M")))
	ac.setPosition(timeLabel,70,30)
	ac.addRenderCallback(appWindow , onFormRender)
	return "Time"

#update function
def onFormRender(deltaT):
	global timeLabel
	theTime=datetime.now()
	ac.setText(timeLabel, "{}".format(theTime.strftime("%H:%M")))
	

	
	
	
	




