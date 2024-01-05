def find_capitals(word):
    isupper_word = [char for char in word if char.isupper()]
    return ''.join (isupper_word)
print(find_capitals('The Quick Brown Fox'))
