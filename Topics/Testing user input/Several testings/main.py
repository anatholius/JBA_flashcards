def check(entry):
    try:
        entry = int(entry)
    except ValueError:
        print("It is not a number!")
        return

    print(
        entry
        if entry >= int('202') else
        "There are less than 202 apples! You cheated me!",
    )
