def disemvowel(s):
    remove_vowels ="aeiouAEIOU"
    result_string = ''.join(char if char not in remove_vowels else ''for char in s)
    return result_string
    pass
print(disemvowel("Hello World"))