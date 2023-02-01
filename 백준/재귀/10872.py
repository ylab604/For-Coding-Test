n=int(input())
if n==0:
    print(1)
    exit()
#result =1

def facto(x):
    result =1
    if x>0:
        result = x*facto(x-1)
    return result
    
    
    
print(facto(n))