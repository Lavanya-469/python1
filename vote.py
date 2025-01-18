
age = int(input("Enter the age of user: "))

if age<1 or age>100:
    print("Invalid input")
elif age>18 and age<= 100:
    print("you are eligible to vote")
elif age==18:
    print("eligible to apply for vote")
else:
    print("your not eligible to vote")
