import unittest

"""
Import test modules
"""
# Import Data Retrieval
import test_retrieveData


# Import Technical Analysis
import test_technicalAnalysis_trends
import test_technicalAnalysis_momentum
import test_technicalAnalysis_volatility
import test_technicalAnalysis_volume

# Import Portfolio Management
# Import Strategies

# Initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Add tests to the suite
suite.addTest(loader.loadTestsFromModule(test_retrieveData))
#suite.addTest(loader.loadTestsFromModule(test_technicalAnalysis_trends))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)