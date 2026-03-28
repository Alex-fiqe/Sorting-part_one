m=int(input())
n=list(map(int, input().split()))
d = [0] * 100
for i in n:
  d[i] += 1
    
print(*d)
