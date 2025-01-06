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
        print("\n", boardev, "\nPlayer x has won! Congrats!")

    elif ("ooo" in boardev):
        print("\n", boardev, "\nYou, player o, have won! Great!")

    elif ("-" not in boardev):
        print ("\n", boardev, '\nThe board is full, nobody won! \n!!!!!!!!!!!!!!!!!!!!')

    else: # the game continues
        gameon = True  
    return(gameon)   #returns True if the game goes on


def checks_index(s, index): 
    valid_index = False 

    if index < 0:
        #print("The coordinate is outside the given board - number to low")
        pass

    if index > len(s):
        #print("The coordinate is to high and therefore outside the given board")
        pass

    if index == '':
        print('You should give a number between 0 and 19. Try again!') 
    else:
        valid_index = True
    return(valid_index)
    

def free_space(boardxo, posnow):
    # checks if possition is already taken. position is checked and True returned if available
    if boardxo[int(posnow)] == '-': #checking if possition is free and not marked.
        validspace = True

    else:       # alternative: (newval == ('x' or 'o')):
        validspace = False
    return(validspace)


def move(board4check, marku, markpc):
    # asks user for position. returns the new game board and the user's new mark position
    while True:
        print(board4check)
        pos_u = int(input(print("\nWhere do you want to set your mark?\n Which coordinate (0-19)? ")))
        if checks_index(board4check, pos_u): # Position 19 sometimes raises an "IndexError: string index out of range"
            if free_space(board4check, pos_u):
                break
            else:
                print('This position is already marked. Choose again!')
        else:
            print("This position is outside the board. Choose again! ")

    # insert the new string between "slices" of the original
    newst = board4check[:pos_u] + marku + board4check[pos_u + 1:]

    return(newst, pos_u)


def pc_move(boardpc, userpos, compmark):
    # Returns a game board with the computer's move. PC picks a position close to user's last coordinates.

    while 1 == 1:  
        compmove = userpos + random.randrange(-4, 4)
        if checks_index(boardpc, compmove):
            if free_space(boardpc, compmove):       
                boardpc = (boardpc[:compmove] + str(compmark) + boardpc[compmove + 1:]) # probaly ther is a bug in here :)
                break

    return(boardpc) 