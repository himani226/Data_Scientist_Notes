
def CountVowels(text):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    if not text:
        raise ValueError("Input string cannot be empty.")
    else:
        for char in text:
            if char in vowels:
                vowel_count += 1
    return vowel_count
