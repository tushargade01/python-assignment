#6. Write a Python program that takes the principal amount, rate of interest, and time period as inputs and calculates the simple interest. Display the calculated interest.

p_amount = int(input("Enter principle Amount: "))
rate_of_interest = float(input("Enter rate of interest: "))
time_period = int(input("Enter Time Period: "))

print(f"Simple interest is : {(p_amount*rate_of_interest*time_period)/100}")