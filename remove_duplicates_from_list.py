def distinct(seq):
    test_list = []
    for i in seq:
        if i not in test_list:
            test_list.append(i)
    return test_list
    pass
print(distinct([1,2,3,4]))
