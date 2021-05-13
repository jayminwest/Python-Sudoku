#Python-Sudoku
#ALL CREDIT TO TECH WITH TIM's YOUTUBE TUTORIAL
#Backtracking Logic
#   Pick empty square
#   Try all numbers
#   Find number that works and move to next square
#   Repeat this
#   Once square becomes impossible, backtrack

gameBoard = [
    [7,8,0,4,0,0,1,2,0], 
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(board):
    find = find_empty(board)

    if not find:
        return True #Base case, when we get here, we're done
    else:
        row, col = find

    for i in range(1,10): #goes through 1-9
        if valid(board, i, (row, col)): #Row, col here is position
            board[row][col] = i
            
            if solve(board): #this makes it recursive, continues to check the board
                return True
            
            board[row][col] = 0 #Backtracking, reset the last item
            
    return False


def valid(board, num, pos):
    #Check row
    for i in range(len(board[0])): #Just getting the size of the board, for typical Sudoku this is always 9
        if board[pos[0]][i] == num and pos[1] != i: #Goes through each element in the row, checks if there is two of the same numbers in a row given the number passed in and the rest of the row
            return False

    #Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i: #Same as above but it loops through the column instead of the row
            return False

    #Check 3x3 box
    box_x = pos[1] // 3 #integer division
    box_y = pos[0] // 3

    #Loop for the box:
    for i in range(box_y * 3, box_y * 3 + 3): #This will return either 0,1,2 and give coords of the box
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    
    return True

def print_board(board):
    
    for i in range(len(board)):
        if i % 3 == 0 and i != 0: #This makes the horizontal lines between the rows. i != 0 makes it so that it doesnt print a line on top
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0: #j != 0 is here so it doesn't print out a line on the first column
                print (" | ", end = "") #end means it doesnt print out a next line char, j is the index and it checks that it is the third line

            if j == 8: #8 is the last index, could be changed if not playing typical board size
                print (board[i][j])
            else:
                print (str(board[i][j]) + " ", end = "")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, col

    return None #if there are no empty squares, return this

print("Starting Board: \n")
print_board(gameBoard)
solve(gameBoard)
print("Solved Board: \n")
print_board(gameBoard)