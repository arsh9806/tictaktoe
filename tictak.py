import itertools
def win(game):
    def same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    #horizontal winner
    for row in game:
        if same(row):
            print(f" Player {row[0]} won the game horizontally ")
            return True

    for col in range(len(game)):
        #vertical winner
        check = []
        for row in game:
            check.append(row[col])
        if same(check):
            print(f" Player {check[0]} won the game vertically ")
            return True


    #diagonal winner
    diags = []
    for row,col in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if same(diags):
        print(f" Player {diags[0]} won the game diagoally(/) ")
        return True


    diag = []
    for i in range(len(game)):
        diag.append(game[i][i])
    if same(diag):
        print(f" Player {diag[0]} won the game diagoally(\) ")
        return True

    return False



def game_board(game_map,player=0,row=0,column=0,just_display = False):
    try:
        if game_map[row][column]!= 0:
            print("Try another position , This is occupied")
            print(f"Current player : {current_player}")
            return game_map,False
        if not just_display:
            game_map[row][column] = player
        a = "   "+"  ".join([str(i) for i in range(len(game_map))])
        print(a)
        for row,column in enumerate(game_map):
            print(row, column)
    except Exception as e:
        print("Enter valid row or column", e)
        return game_map,False
    except IndexError as a:
        print(" Enter valid input ", a)
        return game_map,False
    return game_map, True


play = True
player = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0], ]
    game_won = False
    game , _= game_board(game, just_display = True)
    b = itertools.cycle(player)

    while not game_won:
        current_player = next(b)
        print(f"Current player : {current_player}")
        played = False
        while not played:
            row = int(input("enter row : "))
            column = int(input("enter column : "))
            game, played = game_board(game, current_player, row, column)
            if win(game):
                game_won = True
                play_again = input("You want to play again (y/n)? : ")
                if play_again.lower() == 'y':
                    play = True
                elif play_again.lower() == 'n':
                    play = False
                else:
                    print("WRONG CHOICE !! EXITING....")
                    play = False





