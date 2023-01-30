T = int(input())

def ADD (A,B):
    C=A+B
    return C



for _ in range(T):
    A,B = map(int,input().split())
    ADD(A,B)
    print(ADD(A,B)) 