# filterVowels(s)
def filterVowels(s):
    """Recursively remove vowels from the input."""
    if not s:  # empty string
        return s
    elif s[0] in "aeiouAEIOU":  # first character is vowel
        return filterVowels(s[1:])  # skip first character and process rest
    return s[0] + filterVowels(s[1:])  # return first character and process rest
