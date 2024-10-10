# 6.  Use  round()  inside  map()  to round a list of floating-point 
# numbers to 1 decimal place. 
# Example:  round_to_one([3.14159, 2.71828, 1.61803])  should return  [3.1, 
# 2.7, 1.6] . 

#print(round(34.5674,2))
numbers = [3.14159, 2.71828, 1.61803]
temp = list(map(lambda x : f"{round(x,1)}",numbers))
print(temp)