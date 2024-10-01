# 4. Create a function print_details that accepts keyword arguments and prints them in the format: "key: value". Test the function with different sets of keyword arguments
def print_details(*args,**argus):
    for k, v in argus.items():
        print(f"{k} : {v}")
print_details(name='tushar',age=21)

#preactice

def details(**userData):
    for key, value in userData.items():
        print(f"{key} : {value}")
details(name="sachin", work='IT sector')
details(name="roshan", work='telecaller')
details(name="roshan", work='telecaller')
details(name="roshan", work='telecaller')