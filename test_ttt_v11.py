import ttt_v11

# testing the evaluate module (which is checking if the game goes on)
def test_evaluatexxx():
    res = 'xxx' in '-----------xxx------'
    assert res == True

def test_evaluateNotxxx():
    res = 'xxx' in '---x---x-----x------'
    assert res == False

def test_evaluateooo():
    res = "ooo" in '----ooo-------------' 
    assert res == True

def test_evaluateNotooo():
    res = "ooo" in '----o-----oo--------'
    assert res == False

def test_evaluate_running():
    res = '-' in 'oooxxxoxoxoxoxoxooxx'
    assert res == False

def test_evaluate_end():
    res = '-' in 'ooxxoxoxoxox-oxooxxo'
    assert res == True  

# testing the move module
def test_move7():
    pos_u = 7
    board = '--------------------'
    board = board[:pos_u] + 'x' + board[pos_u + 1:]
    assert('-------x------------' == board)


def test_move0():
    pos_u   = 0
    board   = str()
    board = '--------------------'
    board = board[:pos_u] + 'x' + board[pos_u + 1:len(board)]
    assert(board  == 'x-------------------')




''' 
3) By your own words
(as comments at the end of the created Python test file) 
describe:'''

## What is a Python module and how does it differ from a Python package?
'''A module is only one file with a (or more) function(s) which are implemented by:
    import *otherfile.py*
The function is defined in the otherfile.py and initialized and 
called by a other py-file.

A package has more files organized in folders. Often organized in a hierachy. 
It is a collection of bigger and complexer modules (and sub-packages) 
which are ready to use for other projects as well. 
Packages are for reuseable code. It is neatly put together and 
packed in a folder with subfolders. The overview therefore is easier.'''


## What are side effects and give some examples.
'''Side effects overwrite variables (or functionalities) outside a function. 
This could lead to unpredictable functionality of a program like bugs 
if not managed well.
Or a side effect occurs if a function needs user's interaction to be 
called and started. Therefore we split the module of the game 
and put the call module in a seperate start-file. 
This start-file can not be tested but is is more unlikly to fail. 

And the other moduls can be tested in the original file: 
if __name__ == "__main__":
    tic_tac_toe_1d()

---> The game will only be imported (and not started automatically).'''


## What are Exceptions and 
# what to do if third-party code that we use throws them?
''' 
Exceptions are errors with a message printed out on the screen or in a file.
Exeptions raised help to prevent bugs or unwanted funcionalities.
There are built-in exceptions like ValueError or TypeError.
There are different exceptions which hint the the problem.
Therefore an error is shown early on before it could spread and
get harder to handle and fixed.

fx. standard biulit-in exceptions: 
except TypeError:
    print('This input is not vaild due to a wrong type.')
except ValueError:
    print('This value is outside the given board and expected boundaries.')

Costumed exceptions could give more info and make the code cleaner.
fx.:
class ToBigForBoard(Exception):
    pass
    

3rd-party code throw an exception:
Probably a user's input is invalid or our variable provided 
for the package/module?
I am not to sure about it. Some ppl mention that in python it isn't
very important to be very neat on exeptions and there are workarounds.
Some invalid input throws another error later on, f.x. invalid URL and
therefore the exception before is probalby not very crutial.
But I guess I'd check what kind of exception is raised by the 3rd party 
code, what this does or could do to my programs funcionality. 
And maybe deciding together with a coworker if the thrown exception 
could be fixed or just ignored and catched with a workaround.
'''

## Using which keywords can you create, throw and catch your new custom Exception?
'''
class ToBigForBoard(Exception):
    print('This coordinate is to big for the given board. Choose again.')

while True:
    # asks for input and checks if it's a valid number. 
    # otherwise raises a ValurError and asks again for user's new input.
    try:
        coordi = input(int(print('Where to place you next marker? 0-19')))
        break
    except ValueError:
        print('This is no valid number. Choose again!')
    
if (coordi > 19):
    # checks if the number is on the board or to big. Prints out if the 
    # number is to high but doesn't repeat asking for new input.
    except ToBigForBoard
'''



## Give examples of some benefits of testing?
'''
Testing checks the program without a person needing to manually test and print variables
to check the outcome.
There are psitive tests where x==b or x !=b is tested in the assert line
at the end of a test-module (like "return"). 

And there are negative tests 
(instead of raising exeptions in a positive test and making the test fail,
which is not wanted).
In a negative test e.g. invalid inputs and the moduls handling are checked.
Reporting back that the input is invalid and why are important for fixing
the programm or lealizing that there is a problem with the given input.
Otherwise problems which are hard to dedect later on could occur.

bash / terminal:
* cd / changing to the correct directory with the test_file.py and file.py *
python3 -m pytest -v  
'''