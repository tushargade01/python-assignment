# 3.  Create a lambda function to check if a string starts with the 
# letter 'A'. 
# Example: (lambda s: s[0].lower() == 'a')('Apple') should return True. 

check = lambda inputString : True if inputString[0].upper() == "A" else False

print(check("Apple"))