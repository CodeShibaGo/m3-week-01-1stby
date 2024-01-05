def categorize_new_member(data):
    arr_data = []
    for age, value in data:
        if age >= 55 and value > 7:
            arr_data.append("Senior")
        else:
            arr_data.append("Open")
    return arr_data
    pass
print(categorize_new_member([(65, 8.0), (70, 7.5)]))