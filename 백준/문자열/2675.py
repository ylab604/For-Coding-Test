T= int(input())

for k in range(T):
    R, S = map(str, input().split())


    for i in range(len(S)):
        for _ in range(int(R)):
            print(S[i],end='')
    print()        

        
        
###############
https://ooyoung.tistory.com/69
#*되는구나?


n = int(input())

for _ in range(n):
    cnt, word = input().split()
    for x in word:
        print(x*int(cnt), end='')  # end='' 옆으로 붙임
    print()  # 줄넘김