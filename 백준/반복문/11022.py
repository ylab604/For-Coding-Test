import sys
input=sys.stdin.readline
T=int(input())

for _ in range(T):
    a,b=map(int,input().split())
    c = a+b
    i=_+1
    print(f"Case #{i}: {a} + {b} = {c}")