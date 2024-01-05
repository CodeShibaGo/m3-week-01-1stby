def change_case(input_str, case):
    if case == 'upper':
        input_str = input_str.upper()
    elif case == 'lower':
        input_str = input_str.lower()
    return input_str
    pass

print(change_case("hello","upper"))
print(change_case("HELLO","lower"))

