import sys
input = sys.stdin.readline

N = int(input())
square = []
for _ in range(N):
    square.append(list(map(int,input().split())))
    

## 방문여부 확인 배열
visited = [[0]*N for _ in range(N)]


## 하, 우
dx=[1,0]
dy=[0,1]

from collections import deque

## bfs 함수 만들기
def dfs(x,y):
    visited[x][y]=True
    #2방향밖에 못움직임
    for i in range(2):
        #갈 수 있는 경우의수 발판의 숫자
        nx,ny = x+dx[i]*square[x][y], y+dy[i]*square[x][y]
        if 0<=nx <N and 0<= ny < N and not visited[nx][ny]:
            if square[nx][ny] == -1:
                print("HaruHaru")
                break
            else:
                dfs(nx,ny)
    return True

if dfs(0,0):
    print("Hing")