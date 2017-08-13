import unittest
import logging
import StringIO
from test.discoverTest import discoverTest
from test.playTest import playTest

logging.basicConfig(level=logging.INFO)

suite = unittest.TestSuite()

# suite.addTest(unittest.TestLoader().loadTestsFromTestCase(discoverTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(playTest))
# suite.addTest(unittest.TestLoader().loadTestsFromTestCase(DirectionTest))
# suite.addTest(unittest.TestLoader().loadTestsFromTestCase(NearbyTest))

unittest.TextTestRunner(verbosity=2).run(suite)
