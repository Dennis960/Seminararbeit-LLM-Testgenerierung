import unittest
from solution import analyze_data_transfers

class TestAnalyzeDataTransfers(unittest.TestCase):
    def test_example_case(self):
        transfers = [
            ("192.168.1.1", "10.0.0.1", 500),
            ("192.168.1.1", "10.0.0.2", 300),
            ("10.0.0.1", "192.168.1.1", 200),
            ("10.0.0.2", "192.168.1.1", 100)
        ]
        expected_output = [("192.168.1.1", 800), ("10.0.0.1", 200), ("10.0.0.2", 100)]
        self.assertEqual(analyze_data_transfers(transfers), expected_output)

    def test_empty_transfers(self):
        transfers = []
        expected_output = []
        self.assertEqual(analyze_data_transfers(transfers), expected_output)

    def test_single_transfer(self):
        transfers = [("192.168.1.1", "10.0.0.1", 100)]
        expected_output = [("192.168.1.1", 100)]
        self.assertEqual(analyze_data_transfers(transfers), expected_output)

    def test_multiple_sources_with_same_total(self):
        transfers = [
            ("192.168.1.1", "10.0.0.1", 300),
            ("192.168.1.2", "10.0.0.2", 300),
            ("192.168.1.1", "10.0.0.3", 200),
            ("192.168.1.2", "10.0.0.4", 200)
        ]
        expected_output = [("192.168.1.1", 500), ("192.168.1.2", 500)]
        self.assertEqual(analyze_data_transfers(transfers), expected_output)

    def test_large_data_transfers(self):
        transfers = [
            ("192.168.1.1", "10.0.0.1", 1000000),
            ("192.168.1.2", "10.0.0.2", 500000),
            ("192.168.1.3", "10.0.0.3", 750000)
        ]
        expected_output = [
            ("192.168.1.1", 1000000),
            ("192.168.1.3", 750000),
            ("192.168.1.2", 500000)
        ]
        self.assertEqual(analyze_data_transfers(transfers), expected_output)

if __name__ == "__main__":
    unittest.main()