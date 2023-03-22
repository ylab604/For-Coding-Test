import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = list(map(int,input().split()))
#누적 합들을 전부 구해 놓고 반복문안에서 사칙연산만 진행하기
pre_sum = [0]
tmp = 0
for a in num:
    tmp+=a
    pre_sum.append(tmp)


for _ in range(m):
    i,j = map(int,input().split())
    print(pre_sum[j]-pre_sum[i-1])
    