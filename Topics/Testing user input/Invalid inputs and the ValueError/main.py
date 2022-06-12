def check():
    entry = input()
    message = "Correct the error!"
    try:
        print(entry if int('25') <= int(entry) <= int('37') else message)
    except ValueError:
        print(message)
