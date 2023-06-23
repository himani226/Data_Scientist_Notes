
import unittest
import countvowels

class PalindromeTest(unittest.TestCase):
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            countvowels.CountVowels("")

    def test_one_word_string(self):
        self.assertEqual(countvowels.CountVowels("rhythm"),0)
        self.assertEqual(countvowels.CountVowels("m"),0)
        self.assertEqual(countvowels.CountVowels("python"),1)
        self.assertEqual(countvowels.CountVowels("data"),2)

    def test_multi_word_strings(self):
        self.assertEqual(countvowels.CountVowels("hello himani"),5)
        self.assertEqual(countvowels.CountVowels("python good"),3)
    

if __name__ == '__main__':
    unittest.main()
