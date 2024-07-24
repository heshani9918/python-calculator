# TODO: Write the functions for arithmatic operations here
# These functions should cover Task 2


# -------------------------------------
# TODO: Write the select_op(choice) function here
# This function sould cover Task 1 (Section 2) and Task 3

def select_op(choice):
    if choice == "#":
        return -1
    elif choice == "$":
        return 0
    elif choice == "+" or "-" or "*" or "/" or "^" or "%":
        while True:
            number1 = input("Enter first number: ")
            print(number1)
            if number1.endswith("$"):
                return 0
            elif number1.endswith("#"):
                return -1
            try:
                number1 = float(number1)
                break
            except ValueError:
                print("Invalid input. To get the manu back enter \"$\"")

        while True:
            number2 = input("Enter second number: ")
            print(number2)
            if number2.endswith("$"):
                return 0
            elif number2.endswith("#"):
                return -1
            try:
                number2 = float(number2)
                break
            except ValueError:
                print("Invalid input. To get the manu back enter \"$\"")

        if choice == "+":
            result = number1+number2
        elif choice == "-":
            result = number1-number2
        elif choice == "*":
            result = number1*number2
        elif choice == "/":
            if number2 != 0:
                result = number1/number2

            else:
                print("float division by zero")
                result = None
                print(f"{number1} {choice} {number2} = {result}")
                return 0

        elif choice == "**":
            result = number1**number2
        elif choice == "%":
            result = number1 % number2

    print(f"{number1} {choice} {number2} = {result}")


# End the select_op(choice) function here
# -------------------------------------
# This is the main loop. It covers Task 1 (Section 1)
# YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    if (select_op(choice) == -1):
        # program ends here
        print("Done. Terminating")
        exit()
