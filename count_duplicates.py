def count_duplicates(text):
    text_list = set()
    text_list2 = set()

    for i in text:
        i_lower = i.lower()
        if i_lower in text_list:
            text_list2.add(i_lower)
        else:
            text_list.add(i_lower)
    return len(text_list2)
    pass
print(count_duplicates("AaBbCde"))