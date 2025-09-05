from main import is_palindrome

def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome.
    """
    s = ''.join(ch.lower() for ch in s if ch.isalnum())  # keep only alphanumeric
    return s == s[::-1]


class TestPalindrome(unittest.TestCase):

    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
    
    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))
    
    def test_case_insensitivity(self):
        self.assertTrue(is_palindrome("MadAm"))
        self.assertTrue(is_palindrome("RaceCar"))
    
    def test_with_spaces_and_punctuation(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
    
    def test_empty_and_single_char(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))


if __name__ == "__main__":
    unittest.main()
