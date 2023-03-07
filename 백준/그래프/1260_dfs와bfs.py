import sys
from collections import deque
input = sys.stdin.readline
n,m,v = list(map(int,input().split()))
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = list(map(int,input().split()))
    adj[x].append(y)
    adj[y].append(x)
#작은 값부터 먼저 방문하기 위한 정렬    
for i in range(1,n+1):
    adj[i].sort()
    

#print(adj)
#print(visit)
#이거 dfs함수 안에 넣으면 재귀이기 때문에 무한으로 빠짐
visit = [0] * (n+1)
def dfs(x):
    
    visit[x] =1
    print(x,end=' ')
    for y in adj[x]:
        #만약 방문한거면 dfs하지 않고 다음으로 넘어가
        if visit[y]:
            continue
        dfs(y)
        
def bfs(x):
    visit = [0] * (n+1)
    q = deque()
    q.append(x)
    visit[x]=1
    while q:
        x=q.popleft()
        print(x,end=' ')
        for y in adj[x]:
            if visit[y]:
                continue
            visit[y]=1
            q.append(y)
dfs(v)
print()
bfs(v)
