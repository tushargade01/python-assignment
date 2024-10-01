# 5. Write a Python program that takes an integer as input and determines if it is even or odd.Print the result
running = True
while running:
    userInput = int(input("\nEnter Number which you want to check odd or even: "))
    if userInput % 2 == 0:
        print(f"{userInput} is even.")
    else:
        print(f"{userInput} is odd.")
    userWant = input("\nDo you want to check another number even or not? (y/n) : ")
    if userWant == 'y' or userWant == 'Y':
        continue
    else:
        running = False