n = 0

for x in range(10000000):
    if n < 10001:
        if x > 1:
            for y in range(2, x):
                if x%y == 0:
                    break
            else:
                print(x)
                n = n+1