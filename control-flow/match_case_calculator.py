# A simple calculator
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /)")
match operation:
    case "*":
        if num1 == 0 or num2 == 0:
            print("Cannot multiply by zero!")
        else:
            multiply = num1 * num2
            print("The result is: ", multiply)
    case "+":
        add = num1 + num2
        print("The result is: ", add)
    case "-":
        subtract = num1 - num2
        print("The result is: ", subtract)
    case "/":
        if num1 ==0 or num2 == 0:
            print("Cannot divide by 0!!!")
        else:
            divide = num1 / num2
            print("The result is: ", divide)
    case _:
        print("err!")
