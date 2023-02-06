print()
print("Project Euler #1")
print()

sum = 0

for values in range (0,1000,1):
    if values%3==0:
        sum+=values
    elif values%5==0:
        sum+=values

print(sum)
