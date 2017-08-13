# encoding: utf-8
import os
import logging
import time
import commControl as commControl
from uiautomator import Device 

d = Device("192.168.1.67:5555")

def testRankingList():
	logging.info("goto ranking list")
	ranking = d(className="android.widget.TextView",text="排行榜")
	if not (ranking.exists):
		commControl.openSidebar();
		commControl.gotoDiscover();
	ranking.click()
	pass

def gotoRankingList(titlename):
	logging.info("clicking list")
	ranking = d(className="android.widget.TextView",text=titlename)
	ranking.click()
	time.sleep(5)
	pass

def getTitle():
	logging.info("get Title...")
	target = d(className="android.view.View").child(className="android.widget.TextView")
	return target.text
	pass

def getRankingListTitle():
	logging.info("get ViewTitle...")
	target = d(className = "android.support.v7.widget.RecyclerView").child(className="android.widget.TextView")
	return target.text

def getPlayListTitle():
	logging.info("get List Title...")
	target = d(className="android.widget.FrameLayout").child(className="android.widget.ImageButton").sibling(className="android.widget.TextView")
	return target.text
	pass