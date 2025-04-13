import unittest
from solution import check_password_strength

class TestCheckPasswordStrength(unittest.TestCase):
    def test_strong_password(self):
        self.assertEqual(check_password_strength("Password1!"), "Strong")
        self.assertEqual(check_password_strength("StrongPass123@"), "Strong")
        self.assertEqual(check_password_strength("Valid_12345"), "Strong")

    def test_moderate_password(self):
        self.assertEqual(check_password_strength("Password1"), "Moderate")  # Missing special character
        self.assertEqual(check_password_strength("password1!"), "Moderate")  # Missing uppercase letter
        self.assertEqual(check_password_strength("PASSWORD!1"), "Moderate")  # Missing lowercase letter
        self.assertEqual(check_password_strength("Password!"), "Moderate")  # Missing digit
        self.assertEqual(check_password_strength("Pass1!"), "Moderate")  # Too short

    def test_weak_password(self):
        self.assertEqual(check_password_strength("password"), "Weak")  # Missing uppercase, digit, special character
        self.assertEqual(check_password_strength("PASSWORD"), "Weak")  # Missing lowercase, digit, special character
        self.assertEqual(check_password_strength("12345678"), "Weak")  # Missing uppercase, lowercase, special character
        self.assertEqual(check_password_strength("!!!!!!!!"), "Weak")  # Missing uppercase, lowercase, digit
        self.assertEqual(check_password_strength("short1!"), "Weak")  # Too short and missing uppercase

    def test_edge_cases(self):
        self.assertEqual(check_password_strength(""), "Weak")  # Empty password
        self.assertEqual(check_password_strength("A1!"), "Weak")  # Too short
        self.assertEqual(check_password_strength("ThisIsAVeryLongPassword123!"), "Weak")  # Too long

if __name__ == "__main__":
    unittest.main()