#3. Create a simple calculator that allows the user to input two numbers and an operator (+,-, *, /, %, **, //). Based on the operator provided, the program should perform the corresponding arithmetic operation and display the result.
running = True
while(running):
    first = input("\nenter first number:")
    sec = input("enter secound number:")
    num1 =int(first)
    num2 =int(sec)
    print(f"\nAddition : {num1+num2}")
    print(f"Subtraction : {num1-num2}")
    print(f"Multiplication : {num1*num2}")
    print(f"Division : {num1/num2}")
    print(f"Modilo : {num1%num2}")
    print(f"Exponentiation : {num1**num2}")
    print(f"floor division : {num1//num2}")

    userWant = input("\ndo you want to calculate another numbers?Yes / No: ")
    if userWant == 'Yes' or userWant == 'yes' or userWant == 'YES':
        continue
    else:
        running = False