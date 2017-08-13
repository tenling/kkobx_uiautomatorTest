import unittest
import logging
from lib.HTMLTestRunner import HTMLTestRunner
from test.discoverTest import discoverTest
import StringIO


logging.basicConfig(level=logging.INFO)

suite = unittest.TestSuite()

#suite.addTest(unittest.TestLoader().loadTestsFromTestCase(SearchTest))
#suite.addTest(unittest.TestLoader().loadTestsFromTestCase(FavoriteTest))
#suite.addTest(unittest.TestLoader().loadTestsFromTestCase(DirectionTest))
#suite.addTest(unittest.TestLoader().loadTestsFromTestCase(NearbyTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(discoverTest))


filePath = "TestResult.html"
fp = file(filePath,'wb')
runner = HTMLTestRunner(stream=fp,title='Taipei Bus Tracer',description="")

runner.run(suite)