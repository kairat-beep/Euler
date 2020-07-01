for i in range(1, 998):
    for j in range(i+1, 999):
        for k in range(j+1, 1000):
            if i**2 + j**2 == k**2:
                print("triplet found:",i,j,k)
                if i + j + k == 1000:
                    print(i,j,k)
