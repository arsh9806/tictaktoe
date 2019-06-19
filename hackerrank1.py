'''NumberOfSquares = int(input())
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

print(temp)'''
'''matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
NewList = []
for _ in range(2):
    NewList = []
    for j in range(2, -1,-1):
        temp = []
        for i in range(3):
            temp.append(matrix[i][j])
        NewList.append(temp)
    matrix = NewList

print(NewList)
'''
str = "abcdefghijklmnopqrstuvwxyz"
nums = list(map(int,input().split()))
lists = []
entered = input()
for i in entered:
    lists.append(nums[str.index(i)])

print(max(lists) * len(entered))

