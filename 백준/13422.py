import sys
input = sys.stdin.readline
def house(N, M, K, money):
    cnt=0
    for i in range(N):
        # 경우의수
        # 1번 i+M <= N
        # 2번 i+M > N
        # 3번 i==N-1
        # M개의 집의 돈의 합이 
        #money[i]+money[i+1]+money[i+2]+...+money[i+M-1]
        if i+M <=N:
            if sum(money[i:i+M]) < K:
                cnt+=1
        elif i ==N-1:
            if money[i]+sum(money[:M])<K:
                cnt+=1
                       
            break
        else:
            if sum(money[i:]) + sum(money[:M-(N-i)])<K:
                cnt+=1
                
            
    print(cnt)
    return 
    

T = int(input())

for _ in range(T):
    ##function
    
    N, M , K = map(int, input().split(' '))
    money = list(map(int,input().split(' ')))
    
    house(N, M, K, money) 