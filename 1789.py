#서로 다른 N개의 자연수의 합이 S라고 한다. 


a= int(input())

i=1
cnt=1
while a>=i:
    a-=i
    i+=1
    cnt+=1

print(cnt-1)
    