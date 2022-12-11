import random
import math


def Calculator():
    choice = input('''
Enter a number from the following list
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Convert to decimal or percent
    6. Root of a number
    7. Exponent
    8. Find slope and y-intercept of linear equation
    9. Generate random number
    10. Cancel
    Option number: ''')
    if choice == "1":
        print("-------------")
        print("Adding two numbers")
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        ans = float(num1) + float(num2)
        print("-------------")
        print("{0} + {1} = {2}".format(num1,num2,ans))
        print("\nType 'Calculator()' to use it again")
    elif choice == "2":
        print("-------------")
        print("Subtracting two numbers")
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        ans = float(num1) - float(num2)
        print("-------------")
        print("{0} - {1} = {2}".format(num1,num2,ans))
        print("\nType 'Calculator()' to use it again")
    elif choice == "3":
        print("-------------")
        print("Multiplying two numbers")
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        ans = float(num1) * float(num2)
        print("-------------")
        print("{0} x {1} = {2}".format(num1,num2,ans))
        print("\nType 'Calculator()' to use it again")
    elif choice == "4":
        print("-------------")
        print("Dividing two numbers")
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        ans = float(num1) / float(num2)
        print("-------------")
        print("{0} ÷ {1} = {2}".format(num1,num2,ans))
        print("\nType 'Calculator()' to use it again")
    elif choice == "5":
        print("-------------")
        print("Converting to decimal/percent")
        num1 = input("Enter numerator: ")
        num2 = input("Enter denominator: ")
        ans = float(num1) / float(num2)
        print("-------------")
        print("Decimal: {0}/{1} = {2}".format(num1,num2,ans))
        print("Percent: {0}/{1} = {2}%".format(num1,num2,ans*100))
        print("\nType 'Calculator()' to use it again")
    elif choice == "6":
        print("-------------")
        print("Root of a number")
        num1 = input("Enter base: ")
        num2 = input("Enter root number: ")
        ans = float(num1) ** (1/float(num2))
        print("-------------")
        print("{0} root {1} = {2}".format(num2,num1,math.ceil(ans)))
        print("\nType 'Calculator()' to use it again")
    elif choice == "7":
        print("-------------")
        print("Exponent")
        num1 = input("Enter base: ")
        num2 = input("Enter exponent: ")
        ans = float(num1) ** float(num2)
        print("-------------")
        print("{0}^{1} = {2}".format(num1,num2,ans))
        print("\nType 'Calculator()' to use it again")
    elif choice == "8":
        print("-------------")
        print("Find slope and y-intercept of linear equation")
        print("(must be in y=mx+b form and use variable x)")
        eq = input("Enter equation: ")
        slope = eq.split("=", 1)[1].split("x", 1)[0]
        yint = eq.split("x", 1)[1]
        print("-------------")
        print('''
        Equation: {0}
        Slope: {1}
        Y-intercept: {2}
        '''.format(eq,slope,yint))
        print("\nType 'Calculator()' to use it again")
    elif choice == "9":
        print("-------------")
        print("Generate random number between x and y")
        x = input("Enter x: ")
        y = input("Enter y: ")
        ans = random.randint(float(x),float(y))
        print("-------------")
        print("Random number between {0} and {1} = {2}".format(x,y,ans))
        print("\nType 'Calculator()' to use it again")
    else: 
        print("-------------")
        print("\nType 'Calculator()' to use it again")
            

print('''
Calculator.py
-------------
''')
Calculator()
