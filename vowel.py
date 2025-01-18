
char = input("Enter a letter : ").lower()

if len(char) == 1:
    if char in "aeiou":
        print(f"{char} is a Vowel")
    else:
        print(f"{char} is a consonate")
else:
    print("inavalid input")




