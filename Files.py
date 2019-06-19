file = open("E:/New.txt", "r")
num = 0
for i in range(10):
    f = file.readline()
    if "line" in f:
        num += 1
print(num)
