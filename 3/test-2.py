import unittest
from solution import highest_scorers

class TestHighestScorers(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(highest_scorers([]), [])

    def test_single_student(self):
        self.assertEqual(highest_scorers([("Alice", 95)]), ["Alice"])

    def test_multiple_students_with_unique_scores(self):
        students_scores = [("Alice", 95), ("Bob", 90), ("Charlie", 85)]
        self.assertEqual(highest_scorers(students_scores), ["Alice"])

    def test_multiple_students_with_same_highest_score(self):
        students_scores = [("Alice", 95), ("Bob", 95), ("Charlie", 85)]
        self.assertEqual(highest_scorers(students_scores), ["Alice", "Bob"])

    def test_students_with_same_scores_and_names_sorted(self):
        students_scores = [("Charlie", 95), ("Alice", 95), ("Bob", 95)]
        self.assertEqual(highest_scorers(students_scores), ["Alice", "Bob", "Charlie"])

    def test_students_with_negative_scores(self):
        students_scores = [("Alice", -10), ("Bob", -5), ("Charlie", -5)]
        self.assertEqual(highest_scorers(students_scores), ["Bob", "Charlie"])

if __name__ == "__main__":
    unittest.main()