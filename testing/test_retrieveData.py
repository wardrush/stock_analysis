import unittest
from retrieve_data import retrieve_data


class RetrieveDataTest(unittest.TestCase):
    """
    Test for data retrieval from implemented sources
    """

    def test_real_ticker_default(self):
        retrieve_data('AAPL')

    def test_real_ticker_robinhood(self):
        retrieve_data('AAPL', lookup='robinhood')

    def test_real_ticker_morningstar(self):
        retrieve_data('AAPL', lookup='morningstar')

    def test_lowecase_ticker_default(self):
        retrieve_data('aapl')

    def test_mixedcase_ticker_default(self):
        retrieve_data('AaPl')

    # Use invalid string ticker inputs
    @unittest.skip("Timeout functionality not yet added")
    @unittest.expectedFailure
    def test_false_str_ticker_default(self):
        retrieve_data('jzys')

    @unittest.expectedFailure
    def test_non_str_ticker_default(self):
        retrieve_data([1,2,3,4])

    @unittest.skip
    @unittest.expectedFailure
    def test_false_str_ticker_morningstar(self):
        retrieve_data('jjzys', lookup='morningstar')

    @unittest.skip
    @unittest.expectedFailure
    def test_false_str_ticker_robinhood(self):
        retrieve_data('jzys', lookup='robinhood')

    # Use non-implemented datasources
    @unittest.expectedFailure
    def test_other_real_datasource(self):
        retrieve_data('AAPL', lookup='iex')

    @unittest.expectedFailure
    def test_other_false_str_datasource(self):
        retrieve_data('AAPL', lookup='jere')

    @unittest.expectedFailure
    def test_other_false_nonstr_datasource(self):
        retrieve_data('AAPL', lookup=[1,2,3,4])


if __name__ == '__main__':
    unittest.main

