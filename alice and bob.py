s, t = (input().split())
s, t = [int(s), int(t)]
a,b = (input().split())
a, b = [int(a), int(b)]
Apples = 0
Oranges = 0
m,n = (input().split())
m, n = [int(m), int(n)]
DistanceApples = list(map(int, input().split()))

for i in DistanceApples:
    if (i+a)>=s and (i+a)<= t:
        Apples += 1


DistanceOranges = list(map(int, input().split()))
for i in DistanceOranges:
    if(i+b)>=s and (i+b)<=t:
        Oranges += 1

print(Apples)
print(Oranges)