#1. 무조건 5원많은거
#2. 5원으로 나누었을 때  나지 홀? => 몫 - 1 

N = int(input())


#거슬러 줄수 없는 경우!!
if N==1 or N == 3:
    print(-1)

elif N%5 == 1 :
    print((N//5)-1+(N%5+5)//2)
    
elif N%5 == 3:
    print((N//5)-1+(N%5+5)//2)

else:
    print(N//5 + (N%5)//2)
    

