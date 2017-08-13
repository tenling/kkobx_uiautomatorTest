# -*- coding: utf8 -*-
import unittest
import control.commControl as commControl
import control.discoverControl as discoverControl
import time
import logging

class discoverTest(unittest.TestCase):
	def setUp(self):
		commControl.openSidebar()
		commControl.gotoDiscover()
		time.sleep(2)
		pass

	def test_discoverPage(self):
		self.assertEqual(discoverControl.getTitle(), u"發現")
		pass

	def test_RankkingList(self):
		discoverControl.testRankingList()
		self.assertEqual(discoverControl.getRankingListTitle(), u"綜合新歌日榜 Top 100")
		discoverControl.gotoRankingList(u"綜合新歌日榜 Top 100")
		self.assertEqual(discoverControl.getPlayListTitle(), u"綜合新歌日榜 Top 100")
		pass

	if __name__ == '__main__':
		unittest.main()