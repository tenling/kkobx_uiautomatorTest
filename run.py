# encoding: utf-8
import os,logging
import time
import control.commControl as commControl
import control.discoverControl as discoverControl
import control.playControl as playControl

#define device
logging.basicConfig(level=logging.DEBUG)
# commControl.openSidebar()
# commControl.gotoDiscover()

# discoverControl.testRankingList()
# discoverControl.gotoRankingList()
#print discoverControl.getPlayListTitle()

print playControl.getSongName()