def century(year):
    year = str(year)
    year_a = int(year[:2])
    if int(year[3:]) > 0:
        year_a += 1
    return year_a
    pass
print(century(2000))