
def is_palindrome(string):
    if not string:
        raise ValueError("Input string cannot be empty.")
    return string == string[::-1]
