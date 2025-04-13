import unittest
from solution import check_password_strength

class TestPasswordStrength(unittest.TestCase):

    def test_strong_password(self):
        self.assertEqual(check_password_strength("Password1!"), "Strong")

    def test_moderate_password(self):
        self.assertEqual(check_password_strength("Password!"), "Moderate")

    def test_weak_password(self):
        self.assertEqual(check_password_strength("pass!"), "Weak")

    def test_empty_password(self):
        self.assertEqual(check_password_strength(""), "Weak")

    def test_password_with_only_lowercase(self):
        self.assertEqual(check_password_strength("password"), "Weak")

    def test_password_with_only_uppercase(self):
        self.assertEqual(check_password_strength("PASSWORD"), "Weak")

    def test_password_with_only_numbers(self):
        self.assertEqual(check_password_strength("12345678"), "Weak")

    def test_password_with_special_characters_only(self):
        self.assertEqual(check_password_strength("!@#$%^&*"), "Weak")

    def test_password_with_no_special_characters(self):
        self.assertEqual(check_password_strength("Password1"), "Moderate")

    def test_password_with_minimum_length(self):
        self.assertEqual(check_password_strength("Pass1!"), "Moderate")

    def test_password_with_less_than_minimum_length(self):
        self.assertEqual(check_password_strength("P1!"), "Weak")

    def test_password_with_all_criteria_met(self):
        self.assertEqual(check_password_strength("StrongPass1!"), "Strong")

if __name__ == "__main__":
    unittest.main()