import math
global_list = [2]
current = 3
def check_list():
    root = math.sqrt(current)
    for i in global_list:
        if  root < i:
            break;
        if  (current%i) == 0:
            return
    global_list.append(current)
        

while current < 2000000:
    check_list()
    current += 2
print(global_list)
print(sum(global_list))
