#맨첨에 이해가 잘 안됬는데 손으로 써보니 이해가 되었음!

n= int(input())
s = input()
abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = dict()
for _ in range(n):
    num[abc[_]] = int(input())
   
cal = "*/+-"
stack=[]
for i in s:
    stack.append(i)
    
tmp=[]

for j in stack:
    if j in abc:
        tmp.append(j)
        
    else:
        tmp.pop()
        tmp.pop()