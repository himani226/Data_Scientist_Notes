
import unittest
import palindrome

class PalindromeTest(unittest.TestCase):
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            palindrome.is_palindrome("")

    def test_palindrome_strings(self):
        self.assertTrue(palindrome.is_palindrome("radar"))
        self.assertTrue(palindrome.is_palindrome("level"))
        self.assertTrue(palindrome.is_palindrome("deed"))
        self.assertTrue(palindrome.is_palindrome("able was i ere i saw elba"))

    def test_non_palindrome_strings(self):
        self.assertFalse(palindrome.is_palindrome("hello"))
        self.assertFalse(palindrome.is_palindrome("python"))
        self.assertFalse(palindrome.is_palindrome("openai"))

if __name__ == '__main__':
    unittest.main()
