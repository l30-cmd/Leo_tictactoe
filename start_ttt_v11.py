import ttt_v11
# splitting the modul for the others 
# for a clean start with no side effects and for better testing.

def tictactoe_1d():
    istr = "--------------------" #setup new board before the first round
    running = True #initalizing the running of the game
    marks = ttt_v11.mark_pick()
    mark_u = marks[0]
    mark_pc = marks[1]

    while running: #looping until the game is finished or quite
        valuesback = ttt_v11.move(istr, mark_u, mark_pc) # user's turn: new board and the user's actual position are returned
        istr = valuesback[0]
        userposition = valuesback[1]
        istr = ttt_v11.pc_move(istr, userposition, mark_pc) #PC's turn, returns updated board
        running = ttt_v11.evaluate(istr) # Has anyone won? Is the board full? Or is the gae still on (True)?
    return()

tictactoe_1d()

print("***\n End of the programm. Bye!")
