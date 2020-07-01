global_list = [2]
current = 3
def check_list():
    for i in global_list:
        if (current%i) == 0:
            return
    global_list.append(current)
        

while len(global_list) < 10001:
    check_list()
    current += 1
print(global_list)
