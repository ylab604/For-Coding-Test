# 맨첨에 이해가 잘 안됬는데 손으로 써보니 이해가 되었음!
# 1935 후위 표기식2
n = int(input())
S = input()                
num = [0]*n				  

for i in range(n):
    num[i] = int(input())  
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
stack = []                    

for i in S :					
    if i in abc :		
        stack.append(num[ord(i)-ord('A')])
    else :						
        str2 = stack.pop()		
        str1 = stack.pop()

        if i =='+' :
            stack.append(str1+str2)
        elif i == '-' :
            stack.append(str1-str2)
        elif i == '*' :
            stack.append(str1*str2)
        elif i == '/' :
            stack.append(str1/str2)

print('%.2f' %stack[0])










