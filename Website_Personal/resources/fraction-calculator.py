import time

fraction = input("Enter a fraction (e.g 20/30): ")

numerator, denominator = fraction.split('/')

numerator = int(numerator)
denominator = int(denominator)

original_numerator = str(numerator)[:]
original_denominator = str(denominator)[:]

numerator_lis = []
denominator_lis = []

if numerator > denominator:
    x = numerator // 2
elif denominator > numerator:
    x = denominator // 2
else:
    x = numerator // 2

while x != 1:
    if x == 1:
        break

    if denominator % x == 0:
        numerator = numerator / x
        denominator = denominator / x

        numerator_lis.append(numerator)
        denominator_lis.append(denominator)
    else:
        x -= 1

try:
    if numerator_lis[0] > numerator_lis[1]:
        numerator = numerator_lis[0]
    else:
        numerator = numerator_lis[1]
except:
    numerator = numerator_lis[0]

try:
    if denominator_lis[0] > denominator_lis[1]:
        denominator = denominator_lis[0]
    else:
        denominator = denominator_lis[1]
except:
    denominator = denominator_lis[0]


while str(numerator)[-1] != "0":
    if str(numerator)[-1] == "0":
        break

    if str(numerator)[-1] == "3":
        numerator = numerator * 3
        numerator_lis.append(numerator)

        denominator = denominator * 3
        denominator_lis.append(numerator)
    
    if str(numerator)[-1] == "5":
        numerator = numerator * 2
        numerator_lis.append(numerator)

        denominator = denominator * 2
        denominator_lis.append(denominator)

if numerator % 2 == 0 and numerator != 2:
    if denominator % 2 == 0 and denominator != 2:
        numerator = numerator / 2
        denominator = denominator / 2

numerator = int(numerator)
denominator = int(denominator)

if str(numerator) == original_numerator and str(denominator) == original_denominator:
    print("This fraction can't be simplified.")

if denominator == 1.0:
    print(str(numerator))
else:
    print(str(numerator) + '/' + str(denominator))


time.sleep(10)

