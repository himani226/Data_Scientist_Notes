
def cap_text(text):
    words = text.lower().split()
    cap_words = []
    for word in words:
        if word.startswith("'"):
            # Preserve the apostrophe and convert the second character to lowercase
            cap_words.append("'" + word[1:].capitalize())
        else:
            cap_words.append(word.capitalize())
    return " ".join(cap_words)
