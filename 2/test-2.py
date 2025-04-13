import unittest
from solution import analyze_data_transfers

class TestAnalyzeDataTransfers(unittest.TestCase):

    def test_single_transfer(self):
        transfers = [("192.168.1.1", "192.168.1.2", 500)]
        expected = [("192.168.1.1", 500)]
        self.assertEqual(analyze_data_transfers(transfers), expected)

    def test_multiple_transfers_same_source(self):
        transfers = [
            ("192.168.1.1", "192.168.1.2", 500),
            ("192.168.1.1", "192.168.1.3", 300)
        ]
        expected = [("192.168.1.1", 800)]
        self.assertEqual(analyze_data_transfers(transfers), expected)

    def test_multiple_sources(self):
        transfers = [
            ("192.168.1.1", "192.168.1.2", 500),
            ("192.168.1.2", "192.168.1.3", 300)
        ]
        expected = [("192.168.1.1", 500), ("192.168.1.2", 300)]
        self.assertEqual(analyze_data_transfers(transfers), expected)

    def test_sorted_by_data_amount(self):
        transfers = [
            ("192.168.1.2", "192.168.1.3", 300),
            ("192.168.1.1", "192.168.1.2", 500)
        ]
        expected = [("192.168.1.1", 500), ("192.168.1.2", 300)]
        self.assertEqual(analyze_data_transfers(transfers), expected)

    def test_sorted_by_ip_when_equal_data(self):
        transfers = [
            ("192.168.1.2", "192.168.1.3", 300),
            ("192.168.1.1", "192.168.1.2", 300)
        ]
        expected = [("192.168.1.1", 300), ("192.168.1.2", 300)]
        self.assertEqual(analyze_data_transfers(transfers), expected)

    def test_empty_transfers(self):
        transfers = []
        expected = []
        self.assertEqual(analyze_data_transfers(transfers), expected)

if __name__ == "__main__":
    unittest.main()