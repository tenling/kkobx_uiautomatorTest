# encoding: utf-8
import os
import logging
import time
import commControl as commControl
from uiautomator import Device 

d = Device("192.168.1.67:5555")

def gotoplay():
	logging.info("Random select Music...")
	d(className="android.widget.ImageView").wait.exists(timeout=20)
	d(className="android.widget.ImageView").click()
	play = d(text="播放")
	play.click()
	time.sleep(2)
	logging.info("going page...")
	target = d(className="android.widget.RelativeLayout",focusable="true")
	title = d(className="android.widget.RelativeLayout",focusable="true").child(className="android.widget.TextView").text
	target.click()
	return title
	pass

def gotoDiscoverpage():
	logging.info("goto discover page")
	ranking = d(className="android.widget.TextView",text="精選")
	if not (ranking.exists):
		commControl.openSidebar();
		commControl.gotoDiscover();
	ranking.click()
	pass

def pauseMusic():
	d(description=u"暫停播放").click()
	pass

def startMusic():
	d(description=u"開始播放").click()
	pass

def getNowPlayTime():
	return d(className="android.widget.SeekBar").sibling(className="android.widget.TextView").text


def getSongName():
	return d(className="android.widget.LinearLayout",instance=4).child(className="android.widget.TextView").text
	pass
