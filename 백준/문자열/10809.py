s= input()

test=[]
test_s=[]
cnt=0
for i in s:
    if i in test_s:
        cnt+=1
                
        
    else:    
        test_s.append(i)
        test.append([i,cnt])
        cnt+=1

alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for j in alpha:
    flag=0
    
    for k in test:
        if j == k[0]:
            print(k[1],end=" ")
            flag=1
        
    if flag ==0:
        print(-1,end=" ")        
        
        
####################################3
https://gururuglasses.tistory.com/88
S= input()
abc='abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in S:
        print(S.index(i),end=' ')
    else:
        print(-1, end=' ')