import math
a= input()
count = 0
for i in range(len(a)-1):
    if a[i] != a[i+1]:
        count+=1
    
print(math.ceil(count/2))

