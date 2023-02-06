from collections import deque
n=int(input())
#딕셔너리에 키와 벨류 값을 넣어야 겠다.
value = list(map(int, input().split()))
ballon = dict()

for _ in range(n):
    ballon[_+1] = value[_]
   
#덱에 풍선들을 넣어야 겠다 왜??? => 값에 따라서 왼쪽 오른쪽 
#pop()오른쪽 제거 popleft()왼쪽제거
#종이에 0은 적혀있지 않으므로 음수면?, 양수면?
queue = [ i+1 for i in range(n)]
queue = deque(queue)
#### rotate 사용

while queue:
    if len(queue) ==1:
        a = queue.popleft()
        print(a,end='')
    else:
        a = queue.popleft()
        print(a,end=' ')
        #왼쪽으로 돌려
        if ballon[a] > 0:
            queue.rotate(-ballon[a]+1)
        #오른쪽으로 돌려
        else:
            queue.rotate(-ballon[a])
            
        





#### 
#### 문자열을 이용해 deque를 만들면 각 문자가 요소로된 리스트 형태의 deque가 만들어진다!!
####