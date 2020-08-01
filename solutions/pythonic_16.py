def div(x, y):
    z = None
    try:
        z = x / y
    except ZeroDivisionError as e:
        print(e)
    return z
div(1, 0)