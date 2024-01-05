def calculate_average(nums):
    sum_nums = 0
    for i in nums:
        sum_nums += i
    return sum_nums / len(nums)
    pass
print(calculate_average([1, 2, 3, 4, 5]))
