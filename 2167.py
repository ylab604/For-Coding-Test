import sys
input= sys.stdin.readline
##(i,j)~~(x,y)위치까지 저장 되어있는 수들의 합을 구하라
#1. 입력 받고
#2. 배열 만들고
#3. k입력받고 슬라이스 해서 넣고

N,M = map(int, input().split(' '))
arr1 = [list(map(int,input().split(' '))) for _ in range(N)]
K=int(input())    
#arr2 = [list(map(int,input().split(' '))) for _ in range(K)]
#arr=[[1,2,4],
#     [8,16,32]]
#print(arr[0][0]~arr[1][3])
#걍 이중포문 쓰자.
#print(arr2)
#print(arr2[2][0])
#print(type(arr2[2][2]))
for _ in range(K):
    result=[]
    #print(_)
    cnt=0
    i,j,x,y = map(int,input().split(' '))
    for a in range(i-1,x):
        #print(i)
        for b in range(j-1,y):
            cnt+=arr1[a][b]
            #result.append(arr1[a][b])
    #print(sum(result))
    print(cnt)