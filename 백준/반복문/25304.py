#총금액 x
#구매한 물건의 종류의 수 n
#각 물건의 가격 a와 개수 b 가 공백을 사이에 두고 주어짐

total = int(input())
n= int(input())
def multiple(a,b):
    c=a*b
    return c

def check(t,d):
    if t==d:
        return print("Yes")
    else:
        return print("No")

result =0
for _ in range(n):
    A,B = map(int,input().split())
    
    
    result+=multiple(A,B)
    #result+=A*B
check(total,result)

