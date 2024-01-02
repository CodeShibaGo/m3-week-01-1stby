def array_diff(a, b):
    result_a =[]
    for item in a :
        print(a)
        if item not in b:
            result_a.append(item)
    return result_a
    pass
a= [1,2]
b = [1]
print(array_diff(a,b))