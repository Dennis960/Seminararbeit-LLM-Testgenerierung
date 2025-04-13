import unittest
from solution import analyze_data_transfers

class TestAnalyzeDataTransfersAdditional(unittest.TestCase):

    def test_no_transfers(self):
        transfers = []
        expected = []
        self.assertEqual(analyze_data_transfers(transfers), expected)

    def test_multiple_sources(self):
        transfers = [
            ("192.168.1.1", "192.168.1.2", 500),
            ("192.168.1.2", "192.168.1.3", 300)
        ]
        expected = [("192.168.1.1", 500), ("192.168.1.2", 300)]
        self.assertEqual(analyze_data_transfers(transfers), expected)

    def test_duplicate_transfers(self):
        transfers = [
            ("192.168.1.1", "192.168.1.2", 500),
            ("192.168.1.1", "192.168.1.2", 500)
        ]
        expected = [("192.168.1.1", 1000)]
        self.assertEqual(analyze_data_transfers(transfers), expected)

    def test_zero_transfer(self):
        transfers = [("192.168.1.1", "192.168.1.2", 0)]
        expected = [("192.168.1.1", 0)]
        self.assertEqual(analyze_data_transfers(transfers), expected)

    def test_negative_transfer(self):
        transfers = [("192.168.1.1", "192.168.1.2", -500)]
        expected = [("192.168.1.1", -500)]
        self.assertEqual(analyze_data_transfers(transfers), expected)

if __name__ == "__main__":
    unittest.main()