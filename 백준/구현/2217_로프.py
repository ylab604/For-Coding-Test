#시간 제한 2초 메모리제한도 192mb로 넉넉한 편

import sys 
input = sys.stdin.readline
n = int(input())
w = [int(input()) for _ in range(n)] 
#print(min(w)*n)

#n빵한다음에 최대 버틸수 있는 중량 체크
#모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.
#w/k 값들에 대해 모든 경우의수 뽑아서 최대값 구해야할듯?? 
w.sort(reverse=True)
result=[]
for i in range(n):
    result.append(w[i]*(i+1))
    

print(max(result))
