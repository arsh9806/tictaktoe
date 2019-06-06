'''game_size= 5
game = []
for i in range(game_size):
    row = []
    for i in range(game_size):
        row.append(0)
    game.append(row)

for row,column in enumerate(game):
    print(row,column)
game = [[i for i in range(3)] for i in range(3)]
for i,j in enumerate(game):
    print(i,j)
print(" when is was %d i was %s" %(5,"great"))'''
a = 2
b = 3
n = 0

for i in range(3, min(a, b) + 1):
    if a % i == b % i == 0:
        n += 1

print(n)

