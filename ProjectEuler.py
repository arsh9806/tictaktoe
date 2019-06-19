triplets = int(input())
answer = []
for k in range(triplets):
    n1n2el = input().split()
    A = n1n2el[0]
    B = n1n2el[1]
    elementNo = int(n1n2el[2])
    C = A + B
    while len(C)< elementNo:
        A = B
        B = C
        C = A + B
        print(C)
    answer.append(C[elementNo-1])
for j in answer:
    print(answer)