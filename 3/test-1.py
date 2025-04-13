import unittest
from solution import highest_scorers

# test_solution.py


class TestHighestScorers(unittest.TestCase):
    def test_single_highest_scorer(self):
        students_scores = [("Alice", 85), ("Bob", 90), ("Charlie", 88)]
        self.assertEqual(highest_scorers(students_scores), ["Bob"])

    def test_multiple_highest_scorers(self):
        students_scores = [("Alice", 85), ("Bob", 90), ("Charlie", 88), ("Dave", 85), ("Eva", 90)]
        self.assertEqual(highest_scorers(students_scores), ["Bob", "Eva"])

    def test_all_same_scores(self):
        students_scores = [("Alice", 90), ("Bob", 90), ("Charlie", 90)]
        self.assertEqual(highest_scorers(students_scores), ["Alice", "Bob", "Charlie"])

    def test_empty_list(self):
        students_scores = []
        self.assertEqual(highest_scorers(students_scores), [])

    def test_single_student(self):
        students_scores = [("Alice", 85)]
        self.assertEqual(highest_scorers(students_scores), ["Alice"])

    def test_unsorted_input(self):
        students_scores = [("Charlie", 88), ("Alice", 85), ("Eva", 90), ("Bob", 90), ("Dave", 85)]
        self.assertEqual(highest_scorers(students_scores), ["Bob", "Eva"])

if __name__ == "__main__":
    unittest.main()