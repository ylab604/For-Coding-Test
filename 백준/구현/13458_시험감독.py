n = int(input())
a = map(int,input().split())
b, c = map(int,input().split())
num =0
for i in a:
    if (i-b) >=0:
       if (i - b)%c ==0:
           num+=(i-b)//c
       else:
           num+=((i-b)//c +1)




print(n+num)
