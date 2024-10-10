# 7.  Write a function that takes two lists and uses map() to return a 
# list of the sums of corresponding elements. 
# Example: add_lists([1, 2], [3, 4]) should return [4, 6].
list1 = [1,2]
list2 = [3,4]

add_list = list(map(lambda x,y: x+y,list1,list2))
print(add_list)