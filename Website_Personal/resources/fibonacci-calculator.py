import time

limit = int(input("Enter a max number: "))

lis = [0, 1]
x = 0

while lis[-1] < limit:
    num = lis[x] + lis[x + 1]
    lis.append(num)
    
    x += 1

    if lis[-1] > limit:
        lis.remove(lis[-1])
        break

print(lis)

time.sleep(10)
