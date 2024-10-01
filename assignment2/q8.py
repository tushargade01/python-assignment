#8. Write a Python program to take a list of 10 elements and slice it to create a sublist containing every second element.
list1 = [6,3,8,3,1,6,4,9,10,34]
temp = 1
list2 = []
for i in list1:
    if temp % 2 == 0:
        list2.append(i)
        list1.remove(i)
        temp += 1
    temp += 1

print(list1)
print(list2)
