#1~n의 합

#solution 1 
#단순히 포문으로 더한다.
n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
    
print(sum)

#solution 2 
#((n)*(n+1))/2 공식 사용 
# 타입 주의!!!!
n=int(input())
print(int(((n)*(n+1))/2))