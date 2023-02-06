#대놓고 스택
#무언가 패턴이 있을 것이다.
cnt = 1
flag = True
stack = []
result = []

N = int(input())
for i in range(N):
    num = int(input())
    # num이하 숫자까지 스택에 넣기
    while cnt <= num:
        stack.append(cnt)
        result.append('+')
        cnt += 1

    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    # 스택 수열을 만들 수 없으므로 NO
    else:
        flag = False
        break

# 스택 수열을 만들수 있는지 여부에 따라 출력 
if flag == False:
    print("NO")
else:
    for i in result:
        print(i)