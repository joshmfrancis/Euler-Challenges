for x in range (0,999,1):
    for y in range (0,999,1):
        if str(x * y) == (str(x * y)[::-1]):
            print (x, y)

