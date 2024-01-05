def unique_in_order(iterable):
    result = []
    if iterable:
        result.append(iterable[0])

    for i in range(1,len(iterable)):
        if iterable[i] != iterable[i-1]:
            result.append(iterable[i])

    return result
    pass
print(unique_in_order("AAAABBBCCDAABBB"))