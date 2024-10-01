#  9. Create a dictionary with at least 5 key-value pairs. Write a Python program to:
#  ● Addanewkey-value pair to the dictionary.
#  ● Updateanexisting key with a new value.
#  ● Delete a key-value pair from the dictionary

dict = {
    'tushar':74,
    'sachin':89,
    'roshan':64,
    'rohan':78,
    'anand':74
}
print(dict)
dict['balaji'] = 67 # add new key-value pair
print(dict)
dict['roshan'] = 69 #update extending data
print(dict)
del dict['tushar'] #delete key value pair
print(dict)