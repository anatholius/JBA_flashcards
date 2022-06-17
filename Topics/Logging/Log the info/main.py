logging.basicConfig(format='%(levelname)s -> %(message)s', level=10, stream=sys.stdout)
def hypotenuse(x, y):
    h = round(((x ** 2 + y ** 2) ** 0.5), 2)
    logging.info('Hypotenuse of %d and %d is %.2f', x, y, h)
    return h
