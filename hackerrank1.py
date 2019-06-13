NumberOfSquares = int(input())
ValuesOfSquares = list(map(int, input().split()))
date, Month = input().split()
date, Month = [int(date), int(Month)]
sum = 0
temp = 0
for i in range(0, NumberOfSquares - Month + 1):
    sum = 0
    for j in range(i, i+Month):

        sum += ValuesOfSquares[j]
    if sum is date:
        temp += 1

print(temp)


