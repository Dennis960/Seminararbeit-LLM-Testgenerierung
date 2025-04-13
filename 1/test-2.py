import unittest
from solution import check_password_strength

class TestCheckPasswordStrength(unittest.TestCase):
    def test_strong_password(self):
        self.assertEqual(check_password_strength("StrongP@ss1"), "Strong")
        self.assertEqual(check_password_strength("Valid123!"), "Strong")

    def test_moderate_password(self):
        self.assertEqual(check_password_strength("Moderate1"), "Moderate")
        self.assertEqual(check_password_strength("WeakPass!"), "Moderate")

    def test_weak_password(self):
        self.assertEqual(check_password_strength("short"), "Weak")
        self.assertEqual(check_password_strength("12345678"), "Weak")

    def test_edge_cases(self):
        self.assertEqual(check_password_strength(""), "Weak")  # Empty password

if __name__ == "__main__":
    unittest.main()