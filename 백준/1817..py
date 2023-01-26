# 제한 조건 책이 탑처럼 쌓여 있다. => 스택 자료구조 의심
# 예제를 통해서 살펴본결과 큐인데??
from collections import deque
N, M = map(int, input().split(' '))
if N==0 :
    pass
else:
    book_list = list(map(int, input().split(' ')))
    queue = deque(book_list)

# 경우의수 나누기 
# 1. N이 0일경우 print(0)
# 2. 책의 무게가 상자를 넘길경우?! 빼기로 접근??
cnt=0
tmp = M

if N== 0:
    pass
else:
    for _ in range(N):
        a= queue.popleft()
        #print(a)
        #리셋 or 처음
        if M==tmp:
            cnt+=1
            M=M-a
            #print(M)
        
        elif M - a >0:
            M=M-a
            #print(M)
        elif M-a <0 :
            cnt+=1
            M = tmp
            M = tmp -a
            #print(M)
        elif M==0:
            cnt+=1
            M=tmp
            M=tmp-a
            #print(M)
        
        else:
            #cnt+=1
            M=tmp
            #M=tmp-a
            #print(M)

print(cnt)