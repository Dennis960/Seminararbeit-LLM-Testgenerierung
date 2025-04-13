import unittest
from solution import highest_scorers

class TestHighestScorers(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(highest_scorers([]), [])

    def test_single_student(self):
        self.assertEqual(highest_scorers([("Alice", 95)]), ["Alice"])

    def test_multiple_students_with_unique_scores(self):
        self.assertEqual(
            highest_scorers([("Alice", 95), ("Bob", 90), ("Charlie", 85)]),
            ["Alice"]
        )

    def test_multiple_students_with_same_highest_score(self):
        self.assertEqual(
            highest_scorers([("Alice", 95), ("Bob", 95), ("Charlie", 85)]),
            ["Alice", "Bob"]
        )

    def test_all_students_with_same_score(self):
        self.assertEqual(
            highest_scorers([("Alice", 90), ("Bob", 90), ("Charlie", 90)]),
            ["Alice", "Bob", "Charlie"]
        )

    def test_negative_scores(self):
        self.assertEqual(
            highest_scorers([("Alice", -10), ("Bob", -20), ("Charlie", -10)]),
            ["Alice", "Charlie"]
        )

    def test_mixed_positive_and_negative_scores(self):
        self.assertEqual(
            highest_scorers([("Alice", 50), ("Bob", -20), ("Charlie", 50)]),
            ["Alice", "Charlie"]
        )


if __name__ == "__main__":
    unittest.main()