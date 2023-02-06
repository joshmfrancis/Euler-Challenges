for a in range (0, 1001, 1):
    for b in range (0, 1001, 1):
            for c in range (0, 1001, 1):
                    if a + b + c == 1000 and a < b < c and a**2 + b**2 == c**2:
                            print("The Ptyhagorean Triplet Consists of", a, b, c)

