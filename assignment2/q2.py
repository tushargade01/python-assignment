 #2. Write a Python program that counts the number of vowels in a given string. Ignore case sensitivity
#string = 'Tushar'
string = 'aeiouAEIOUzxz'
count = 0
for i in string:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        count+=1
print(f"In given string there are {count}")