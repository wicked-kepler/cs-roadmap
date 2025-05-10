# Bisection search of an integer n

n = 200
low = 0
high = 1000
mid = (low + high) // 2
count = 1

while n != mid:
    if mid < n:
        low = mid
    else:
        high = mid
    mid = (low + high) // 2
    count += 1

print(f"count: {count}")
print(f"answer: {n}")
