print("hello rabin")


def takeInputAndAdd():
    count = int(input("How many numbers do you want to add? "))

    total = 0
    for i in range(count):
        num = int(input(f"Enter number {i + 1}: "))
        total += num

    print("The sum is: " + str(total))


takeInputAndAdd()