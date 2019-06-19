'''List = [[1, 2, 3],
        [4, 5, 6 ],
        [7, 8, 9]]
sum1 = 0
sum2 = 0
sum = 15
for i in range(3):
        sum1 += List[i][2-i]'''
'''Image = [
            [[255, 150, 210], [3, 105, 107], [224, 199, 102]],
            [[106, 101, 108], [207, 105, 203], [112, 119, 114]],
            [[124, 129, 122], [133, 135,137], [140 ,141, 146]],
                ]'''
NewList = [100,100,50,40,40,20,10]
element = 5
for i in range(7):
    if element<=NewList[i]:
        NewList.insert(i,element)
print(NewList)