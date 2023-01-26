##N개의 도시 M개의 버스 느낌 사악 ==> A에서 B로 가는데 드는 버스 비용 최소화 그래프 dfs or bfs
#N개의 도시

N= int(input())
#M개의 버스
M = int(input())

#출발도시번호 도착지 도시번호 비용
#우선 비용에 대해서 따로 정의
graph = []
cost = []
for _ in range(M):
    tmp=list(map(int, input().split(' ')))
    graph.append(tmp[:2])
    cost.append(tmp[2])
#시작 끝
start, end = map(int,input().split(' '))

# dfs 정의
visited = []
def dfs(cur_v, end):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            dfs(v)
            
            
dfs(start, end)

