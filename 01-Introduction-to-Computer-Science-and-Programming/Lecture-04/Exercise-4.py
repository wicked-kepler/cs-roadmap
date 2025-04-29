# Finding the cube root of n

n = 27
perfect = False

for i in range(n**3):
    if n == i**3:
        print(f"Perfect root of {n} is {i}")
        perfect = True
        break

if not perfect:
    print("error")