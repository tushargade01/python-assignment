from datetime import datetime 
def current_datetime():
    now = datetime.now()
    return now.strftime("%d %m %y  %H:%M:%S")
print(current_datetime())