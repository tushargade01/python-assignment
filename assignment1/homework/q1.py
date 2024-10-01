#1. Write a Python program that converts temperature from Celsius to Fahrenheit and vice versa. The program should ask the user for the temperature value and the unit (Celsius or Fahrenheit) and then perform the conversion.
running = True
while running:
    temp = input("Enter the temperature value: ")
    unit = input("Enter the unit (celsius = c & Fahrenheit = f): ")

    userWant = input("do you want to convert another temperature? (y/n) : ")
    if userWant == 'n' or userWant == 'N':
        running = False