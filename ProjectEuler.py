# triplets = int(input())
# answer = []
# for k in range(triplets):
#     n1n2el = input().split()
#     A = n1n2el[0]
#     B = n1n2el[1]
#     elementNo = int(n1n2el[2])
#     C = A + B
#     while len(C)< elementNo:
#         A = B
#         B = str(C)
#         C = int(A + B)
#         print(C)
#     answer.append(C[elementNo-1])
# for j in answer:
#     print(answer)
#project euler #2 solution
'''case = int(input())
lis = []
for _ in range(case):
    n = int(input())
    a = 1
    b = 2
    c = a + b
    sum1 = 2
    while True:

        if c < n and c % 2 == 0:
            sum1 += c

        a = b
        b = c
        c = a + b
        if c < n:
            continue
        else:
            break
    lis.append(sum1)
for i in lis:
    print(i)'''

#project euler #3 solution
case = int(input())
lis = []
newlis = []

for _ in range(case):
    maxi = 0
    lis = []
    n = int(input())
    i = 2
    while (i*i) < n:
        if n % i == 0:
            lis.append(i)
            if (n//i) != 0 and :
                lis.append(n//i)
        i += 1
    if not lis:
        lis = [i for i in lis if i%2 != 0]
    for i in lis:
        temp = 0
        for j in range(2,(i//2)+1):

            if i%j == 0:
                temp = 1
        if temp == 0 and i > maxi:
            maxi = i
    newlis.append(maxi)

for k in newlis:
    print(k)
