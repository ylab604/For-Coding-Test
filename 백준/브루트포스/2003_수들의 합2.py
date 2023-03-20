#just구현 
#N이 10^4까지 이기 때문에 n^2를 해도 괜찮을 것이라고 판단. 0.5초이긴하지만 일단 해보고 안되면 다른방법생각
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = list(map(int,input().split()))
#만족하는 경우 카운트 올리기
cnt=0
for i in range(n):
    #만약 i 가 m보다 크다면 무시 
    if num[i] > m:
        continue
    if num[i] == m:
        cnt+=1
        continue
    if num[i]< m:
        tmp=0
        #0을 포함시키면 안돼
        for j in range(i,n):
            #만약 tmp가 m보다 작다면 계속 하고 같다면 카운트 커지면 그만
            tmp +=num[j]
            if tmp == m:
                cnt+=1
                break
            if tmp > m:
                break
print(cnt)


#just구현 
#N이 10^4까지 이기 때문에 n^2를 해도 괜찮을 것이라고 판단. 0.5초이긴하지만 일단 해보고 안되면 다른방법생각
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = list(map(int,input().split()))
#만족하는 경우 카운트 올리기
cnt=0
left, right = 0, 1
tmp = num[left]
while left < n:
    if tmp == m:
        cnt+=1
        tmp-=num[left]
        left+=1
        
    if right == n and tmp <m:
        break
    elif tmp < m:
        tmp+=num[right]
        right+=1
    elif tmp>m:
        tmp-=num[left]
        left+=1
print(cnt)