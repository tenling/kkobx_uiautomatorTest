# encoding: utf-8
import os
import logging
import time
from uiautomator import Device 

d = Device("192.168.1.67:5555")

def setup():
	logging.info("reset adb connect")
	print os.popen('adb kill-server').read()
	print os.popen('adb devices').read()

def getString(target):
	logging.info("getString...")
	return target.child(className="android.widget.TextView").text

def installAPP():
	logging.info("InstallAPP")
	print os.popen('adb devices').read()
	print os.popen('adb install "com.skysoft.kkbox.android.apk"').read()

def unstallAPP():
	logging.info("UninstallAPP")
	print os.popen("adb uninstall com.skysoft.kkbox.android").read()

def openSidebar():
	logging.info("Open SideBar")
	sidebar = d(className="android.widget.ImageButton",description="打開主選單")
	while not (sidebar.exists) :
		logging.info("Not found SideBar...")
		d.press.back()
		time.sleep(1);
	sidebar.click()

def gotoDiscover():
	logging.info(u"Goto 探索")
	target = d(className="android.widget.TextView",text="發現")
	target.click()
	pass

def gotoMusicblock():
	logging.info(u"Goto 我的音樂庫")
	target = d(className="android.widget.TextView",text="我的音樂庫")
	target.click()
	pass

def reopenApp():
	logging.info("reopen app...")
	d.press.home()
	d(text="KKOBX").click()
	pass

def function():
	pass

# def openAPP():
# 	logging.info("OpenAPP")
# 	apps=d(className="android.widget.TextView",description="所有應用程式")
# 	apps.click()
# 	taipei_bus=d(text="台北等公車")
# 	taipei_bus.click.wait()

# def returnHome():
# 	logging.info("Returning Homepage...")
# 	logging.debug(d(resourceId="nexti.android.bustaipei:id/action_bar").child(text="台北等公車").exists)
# 	if not d(resourceId="nexti.android.bustaipei:id/action_bar").child(text="台北等公車").exists:
# 		logging.info("In Wrong Page, Returnning")
# 		while not d(text = "台北等公車").exists:
# 			d.press.back()
# 			time.sleep(2)

# def gotoSearchBus():
# 	logging.info("gotoSearchBus...")
# 	returnHome()
# 	d(resourceId="nexti.android.bustaipei:id/button_search").click.wait()

# def gotoNearBy():
# 	logging.info("gotoNearBy...")
# 	returnHome()
# 	d(resourceId="nexti.android.bustaipei:id/button_nearby").click.wait()

# def gotoDirctions():
# 	logging.info("gotoDirctions...")
# 	returnHome()
# 	d(resourceId="nexti.android.bustaipei:id/button_directions").click.wait()

# def gotoFavorites():
# 	logging.info("gotoFavorites...")
# 	returnHome()
# 	d(resourceId="nexti.android.bustaipei:id/button_favorites").click.wait()

# def clickYes():
# 	logging.info("click yes...")
# 	d(text="是").click.wait()

# def clickSure():
# 	logging.info("click Sure...")
# 	d(test="確定").click.wait()

# def findText(target):
# 	logging.info("Find Target: "+str(target)+" "+str(d(text=target).exists))
# 	return d(text=target).exists

# def getPopupTitle():
# 	logging.info("Getting Popup Title...")
# 	return d(resourceId="nexti.android.bustaipei:id/alertTitle").text

def clickTarget(target):
	target.click()
