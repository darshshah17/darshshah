wow = True

while wow == True:
    numbers = int(input("Enter a whole number: "))
    total = 1

    yesno = input("Would you like us to show the steps (Y/N): ").upper()

    def factorial(numbers, total):
        for i in range(1, numbers + 1):
            total *= i
            print(total)

    def factorial_two(numbers, total):
        for i in range(1, numbers + 1):
            total *= i
        print(total)

    if yesno == "Y":
        factorial(numbers, total)
    elif yesno == "N":
        factorial_two(numbers, total)
    else:
        print("Please type Y or N")


    reply = input("Would you like to use the factorial calculator again (Y/N): ").upper()
    if reply == "Y":
        wow = True
    elif reply == "N":
        wow = False
        print("Thank you for using the factorial calculator!")
    else:
        print("Please type Y or N")
        reply = input("Would you like to use the factorial calculator again (Y/N): ").upper()
        if reply == "Y":
            wow = True
        else:
            wow = False




