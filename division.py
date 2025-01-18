
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num2!=0:
    remainder = num1%num2
    if num1%num2 == 0:
        print(f"{num1} is divisible by {num2}")
    else:
        print(f"{num1} is not divisible by {num2}, Remainder: {remainder}")
else:
    print("invalid input")


