step = 2
summer = 1
current = 1
while step <= 1001:
    for i in range(4):
        current += step
        summer += current
        print(current, summer)
    step += 2

print(summer,current,step)
