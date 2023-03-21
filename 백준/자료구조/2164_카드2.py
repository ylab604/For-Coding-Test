from collections import deque

#큐를 선언하고 주어진대로 구현하면 된다. 그리고 덱을 부르는 이유는 popleft()쓰려고!!
#즉 큐안에 1개가 남았을 때 그 값을 출력하는 것이 문제포인트!!
n = int(input())
q= []

for i in range(n):
    q.append(i+1)
    
que = deque(q)
#반례로 길이 1자리 들어오면 출력하고 종료
if len(que)==1:
    print(que.popleft())
    exit(0)
#que의 길이가 1이 될때까지
while 1:
    #맨위에꺼 버려
    que.popleft()
    #그다음꺼 뒤에붙혀
    a=que.popleft()
    que.append(a)
    if len(que)==1:
        break
    
print(que.popleft())