n = int(input())

num = []
for _ in range(n):
    num.append(float(input()))

for i in range(1,n):
    num[i] = max(num[i-1]*num[i],num[i])
#print(num)
print(f"{max(num):.3f}")
