import sys
input = sys.stdin.readline

#visited = []
#for _ in range(N):
#    visited.append(0)
#visited = [0 for _ in range(N)]
#print(visited)
def check(eggs):
    cnt=0
    for egg in eggs:
        if egg[0] <=0:
            cnt+=1
    return cnt

def dfs(idx, eggs):
    global answer
    
    if idx ==N:
        result = max(result,check(eggs))
        return
    if eggs[idx][0] <= 0:
        dfs(idx+1,eggs)
    else:
        all_broken = True
        for i in range(len(eggs)):
            if idx != i and eggs[i][0]>0:
                all_broken = False
                eggs[idx][0] -=eggs[i][-1]
                eggs[i][0] -= eggs[idx][-1]
                dfs(idx +1,eggs)
                eggs[idx][0] +=eggs[i][-1]
                eggs[i][0] += eggs[idx][-1]
        if all_broken:
            dfs(N,eggs)

N = int(input())
eggs=[list(map(int,input().split())) for _ in range(N)]
result=0
dfs(0,eggs)
print(result)