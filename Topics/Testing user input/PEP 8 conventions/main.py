def check_name(name):
    if name in 'lOI':
        print(
            "Never use the characters 'l', 'O', or 'I' as single-character variable names")
    elif name == name.lower():
        print("It is a common variable")
    elif name == name.upper():
        print("It is a constant")
    else:
        print("You shouldn't use mixedCase")
