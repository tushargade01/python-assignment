def factorial(number):
    temp = 1
    if number < 2:
        return number
    for i in range(2,number+1):
        temp = temp*i
    return temp
if __name__ == "__main__":
    print(factorial(5))