def count_sheep(sheep):
    sheep_count = 0
    for i in sheep:
        if i  == True:
         sheep_count += 1
    return sheep_count
    pass
print(count_sheep([True,True,True,True,True,True,False]))
