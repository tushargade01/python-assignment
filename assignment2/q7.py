# 7. Write a Python function multiply(a, *args) that multiplies a fixed argument a with a variable number of additional arguments. Return the product.

def multiply(a,*args):
    product = a
    for num in args:
        product *= num
    return product

print(multiply(2,3,4))
print(multiply(3,4,5))