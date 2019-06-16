'''TotalSquares = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
                ]
GivenSquare = []
List = []
for i in range(3):
     List = list(map(int, input().split()))
     GivenSquare.append(List)
List = []
for i in TotalSquares:
    total = 0
    for j in range(3):

        for k in range(3):
            if i[j][k] != GivenSquare[j][k]:
                total += abs(i[j][k] - GivenSquare[j][k])
    List.append(total)
print(min(List))

Array = [1, 2, 2, 3, 1, 2]
temp = []
NewList = []
for i in range(len(Array)):
    NewList.append(Array.count(Array[i])+Array.count(Array[i]+1))
print(max(NewList))'''
