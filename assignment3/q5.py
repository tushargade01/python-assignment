#  Create a function that rounds a list of numbers to the nearest 
# whole number. 
# Example:  round_list([1.2, 2.5, 3.8])  should return  [1, 3, 4] . 

#math.ceil() for upper bond 
#math.floor() for lower bond

import math
def roundList(list):
    for i in list:
        if i%1==0.5:
            print(math.ceil(i))
        else:
            print(round(i))
roundList([1.2,2.5,3.8])