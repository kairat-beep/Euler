def GCD(i,j):
   x, y = max(i,j),min(i,j)
   while(y): 
       x, y = y, x % y 
   return x

def LCM(i,j):
    return i*j/GCD(i,j)
previous_num = 1
for i in range(2,21):
    previous_num = LCM(previous_num, i)    
    print(i,previous_num)
