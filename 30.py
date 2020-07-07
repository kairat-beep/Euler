from math import floor
def check_num(num):
    str_num = str(num)
    summation = 0
    for i in range(len(str_num)):
        summation += int(str_num[i])**5
    if summation ==  num:
        print(num,30*"*")
        return num
    return 0
current = 2
summer = 0
while True:
    if(current%10000 == 0):
        print("checking",current, summer)
    summer += check_num(current)
    current += 1
