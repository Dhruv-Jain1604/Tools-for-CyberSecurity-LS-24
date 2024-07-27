import subprocess
import re 

#Final Output
"""
-------------------------

Congratulations! Sudoku #420 solved!

--------------------------

All 420 Sudoku puzzles solved! Congratulations!! Here is your flag: flag{f34r1355_5ud0ku_c0nqu3r0r}
"""

#f = open("temp.txt","a")
# Functions involved in sudoku solving

def create_empty_list(board):
    list_empty=[]
    for row in range(9):
        for column in range(9):
            if board[row][column]==0:
                list_empty.append((row,column))
    return list_empty
    

def search_empty_cell(board) :
    for row in range(9):
        for column in range(9):
            if board[row][column]==0 :
                return (row,column)
    return None

def check_solved(board) :
    for row in range(9):
        if 0 in board[row]:
            return False
    return True

def check_valid_assignment(board, row, column, number):
    for i in range(9):
        if board[row][i] == number or board[i][column] == number :
            return False
        
    x_start = 3*(row // 3)
    y_start = 3*(column // 3)
    for j in range(3):
        for k in range(3):
            if board[x_start+j][y_start+k] == number:
                return False
    
    return True

def solve_sudoku(board):
    
    temp= search_empty_cell(board)

    if temp is None :
        return True
    
    x = temp[0]
    y = temp[1]

    for p in range(1,10):
        if check_valid_assignment(board,x,y,p):
            board[x][y] = p
        
            if solve_sudoku(board):
                return True
            
            board[x][y] = 0

    return False

#Functions for input-output handling

process = subprocess.Popen(["./sudoku"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

for a in range(840):
    sudoku_board = []
    while len(sudoku_board)<9 :
        row  = []
        line = process.stdout.readline().strip()
        #f.write(f"{line}\n")
        #if re.match(r"Welcome", line):
            #f.write(f"{line}\n")
        if re.match(r"\| [0-9\.]", line):
            for char in line:
                if char==".":
                    row.append(0)
                elif char.isdigit():
                    row.append(int(char))
            sudoku_board.append(row)
        
    empty_list = create_empty_list(sudoku_board)
    solve_sudoku(sudoku_board)

    for i in range(len(empty_list)):
        empty_num = empty_list[i]
        #f.write(f"{empty_num[0]} {empty_num[1]} {sudoku_board[empty_num[0]][empty_num[1]]}\n")
        process.stdin.write(f"{empty_num[0]} {empty_num[1]} {sudoku_board[empty_num[0]][empty_num[1]]}\n")
        process.stdin.flush()
        if i != len(empty_list) - 1:
            for i in range(14):
                line = process.stdout.readline()
    #f.write("exit")
while (line := process.stdout.readline()):
    print(line)

