while True:
    num1 = input("Enter a number: ")
    operater = input("Enter an operater + or - or / or *: ")
    num2 = input("Enter another number: ")
    num1 = float(num1)  
    num2 = float(num2)
    if operater == "+":
        print("{} + {} = {}".format(num1, num2, num1 + num2))
    elif operater == "-":
        print("{} - {} = {}".format(num1, num2, num1 - num2))
    elif operater == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            continue
        print("{} / {} = {}".format(num1, num2, num1 / num2))
    elif operater == "*":
        print("{} * {} = {}".format(num1, num2, num1 * num2))
    else:
        print("Invalid operater")