s=input()
total=0

for i in s:
    if i in "ABC":
        total+=3
        
    elif i in "DEF":
        total+=4
    elif i in "GHI":
        total+=5
    elif i in "JKL":
        total+=6
    elif i in "MNO":
        total+=7
    elif i in "PQRS":
        total+=8
    elif i in "TUV":
        total+=9
    elif i in "WXYZ":
        total+=10
    else:
        pass
    
print(total)



#######
https://j-remind.tistory.com/76



dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)