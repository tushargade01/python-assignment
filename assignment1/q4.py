# 4. Write a Python program that takes the length and width of a rectangle as input and calculates its area and perimeter. Display the results
length = int(input("Enter the length of rectangle: "))
width = int(input("Enter the width of rectangle: "))

print(f"area of rectangle is : {length*width}")
print(f"perimeter of rectangle is : {2*(length*width)}")