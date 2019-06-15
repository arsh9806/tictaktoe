'''List = [[1, 2, 3],
        [4, 5, 6 ],
        [7, 8, 9]]
sum1 = 0
sum2 = 0
sum = 15
for i in range(3):
        sum1 += List[i][2-i]'''
TotalSquares = [
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
     List = list(map(int,input().split()))
     GivenSquare.append(List)
print(TotalSquares[0][0][0])
#for i in range(3):
  #  for j in range(3):
   #     for k in range(3):
