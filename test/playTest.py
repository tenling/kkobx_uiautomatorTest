# -*- coding: utf8 -*-
import unittest
import control.commControl as commControl
import control.playControl as playControl
import time
import logging

class playTest(unittest.TestCase):
	def setUp(self):
		playControl.gotoDiscoverpage()
		title = playControl.gotoplay()
		pass

	def tearDown(self):
		if d(description=u"暫停播放").exists:
			playControl.pauseMusic
		commControl.openSidebar()

	def test_playitem(self):
		self.assertEqual(title, playControl.getSongName)

	def test_playtime(self):
		starttime = playControl.getNowPlayTime()
		playControl.startMusic()
		time.sleep(5)
		playControl.pauseMusic()
		endtime = playControl.getNowPlayTime()
		self.assertTrue(starttime < endtime)

	def test_pageout(self):
		playControl.pauseMusic()
		starttime = playControl.getNowPlayTime()
		p.press.back()
		target = d(className="android.widget.RelativeLayout",focusable="true").click
		endtime = playControl.getNowPlayTime()
		self.assertTrue(starttime == endtime)

	def test_outKKBOX(self):
		playControl.pauseMusic()
		starttime = playControl.getNowPlayTime()
		commControl.reopenApp()
		endtime = playControl.getNowPlayTime()
		self.assertTrue(starttime == endtime)

	def test_play_pause_playtime(self):
		starttime = playControl.getNowPlayTime()
		playControl.startMusic()
		time.sleep(5)
		playControl.pauseMusic()
		endtime = playControl.getNowPlayTime()
		playControl.startMusic()
		time.sleep(5)
		playControl.pauseMusic()
		endtime2 = playControl.getNowPlayTime()
		self.assertTrue(starttime < endtime < endtime2d)


	if __name__ == '__main__':
		unittest.main()