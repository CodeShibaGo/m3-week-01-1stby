def positive_sum(arr):
    positive_sum = 0
    for i in arr:
        if i >0 :
            positive_sum += i
    return positive_sum
    pass
print(positive_sum([1, 2, 3, 4, 5]))