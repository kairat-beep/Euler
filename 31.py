currency = [1,2,5,10,20,50,100,200]
combinations = [(i,1) for i in range(201)]


for i in range(1,len(currency)):
    bounded = currency[i]
    print(combinations[:15])
    position = 1
    while position < 201:
        if position - currency[i] >= 0:
            combinations[position] = (position, combinations[position][1] + combinations[position - currency[i]][1])
        position += 1
print(combinations)
