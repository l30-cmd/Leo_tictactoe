import random

def mark_pick():
    # returns the user's choice of mark and tests if it is x oder o.
    # returns computer'S mark as well.
    while True:
        usermark = str(input(print("\n*\n**\n***\n****\nWelcome\n ** \nWhat mark are you choosing? 'x' or 'o'? ")))
        if usermark == 'o':
            pcmark = 'x'
            break

        elif usermark == 'x':
            pcmark = 'o'
            break

        else:
            print("This mark is not valid. Choose again!")
    return(usermark, pcmark)


def evaluate(boardev):
    # checks if anybody won or the board is out of free spaces.
    gameon = False
    if ("xxx" in boardev):
        print(boardev, "\nPlayer x has won! Congrats!")

    elif ("ooo" in boardev):
        print(boardev, "\nYou, player o, have won! Great!")

    elif ("-" not in boardev):
        print (boardev, '\nThe board is full, nobody won! \n!!!!!!!!!!!!!!!!!!!!')

    else: # the game continues
        gameon = True  
    return(gameon)   #returns True if the game goes on


def checks_index(s, index):  #borrowed by https://stackoverflow.com/questions/41752946/replacing-a-character-from-a-certain-index
    # raise an error if index is outside of the string
    
    if index not in range(len(s)):
        valid_index = False #raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    #if index < 0:  # add it to the beginning
        #raise ValueError("index outside given string - number to low") #adapted from the borrowed code

    if (index > len(s) and index < 0):  # add it to the end
        valid_index = False #raise ValueError("index outside given string - to high of a number")
    else:
        valid_index = True
    return(valid_index)
    

def free_space(boardxo, posnow):
    # checks if passition is already taken
    # position is checked and True returned if available
    if boardxo[int(posnow)] == '-': #checking if possition is free and not marked.
        validspace = True

    else:       # alternative: (newval == ('x' or 'o')):
        #print('This possition is already maked! Not possible, player', markturn)
        validspace = False
    return(validspace)


def move(board4check, marku):
    # asks user for position. returns the new game board and the user's new mark position
    while True:
        pos_u = int(input(print("\nWhere do you want to set your mark next?\n Which coordinates(0-19)?  ")))
        if checks_index(board4check, pos_u): # Position 19 sometimes raises an "IndexError: string index out of range"
            if free_space(board4check, pos_u):
                break
        else:
            print("This coorinates are not valid. Choose again!")

    # insert the new string between "slices" of the original
    newst = board4check[:pos_u] + marku + board4check[pos_u + 1:]
    return(newst, pos_u)

# ********************************************************************************
def pc_move(boardpc, userpos, compmark):
    # Returns a game board with the computer's move.
    # PC picks a position close to user's last coordinates.
    checkind = True
    checkspc = True

    while checkind and checkspc:
        compmove = (userpos + random.randrange(-4, 4))
        if checks_index(boardpc, compmove):
            if free_space(boardpc, compmove):
                boardpc = (boardpc[:compmove] + compmark + boardpc[compmove + 1:])
                break

    return(boardpc) 

def tictactoe_1d():
    istr = "--------------------" #setup new board before the first round
    running = True #initalizing the running of the game
    marks = mark_pick()
    mark_u = marks[0]
    mark_pc = marks[1]
    #print(istr)

    while running: #looping until the game is finished or quite
        valuesback = move(istr, mark_u) # user's turn and new board and the user's actual position are returned
        istr = valuesback[0]
        userposition = valuesback[1]
        istr = pc_move(istr, userposition, mark_pc) #PC's turn, returns updated board
        running = evaluate(istr)
        print(istr)

    return()

#main
tictactoe_1d()

print("End of the programm. Bye!")