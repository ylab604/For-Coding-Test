N, M = map(int,input().split())

dna=[input() for _ in range(N)]
#print(dna)
#각 문열의 맥스값 찾는 것
result=""
haming = 0
for i in range(M):
    a,c,g,t=0,0,0,0
    #tmp=[]
    for j in range(N):
        if dna[j][i] =='A':
            a+=1
        elif dna[j][i] =='C':
            c+=1
        elif dna[j][i] =='G':
            g+=1
        else: 
            t+=1
    if max(a,c,g,t) ==a:
        result+='A'
        haming+=c+g+t
    elif max(a,c,g,t) ==c:
        result+='C'
        haming+=a+g+t
    elif max(a,c,g,t) ==g:
        result+='G'
        haming+=c+a+t
    elif max(a,c,g,t) ==t:
        result+='T'
        haming+=c+g+a    
print(result)
print(haming)