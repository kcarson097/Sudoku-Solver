board = [
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

#note bo = board
def solve(bo):
    find = find_empty(bo)
    #find essentially finds the empty box and returns its coordinates
    if not find:
        return True
    #ie you have found the solution - no empty boxes left
    else:
        row, col = find
        #returns coordinates of empty box
        
    #loop through 1 to 9 and enter in box to see if it works
    for i in range(1,10):
        if valid(bo,i,(row,col)):
            bo[row][col] = i
            if solve(bo):
                return True
                
            bo[row][col] = 0
            
    return False
    #if false returned this means solution is not correct so the algorithim backtracks to previous box and tries again
        
        
def valid(bo,num,pos):
    #check row, pos is x coordinate essentially - i.e which list the number is in
    for i in range(len(bo[0])):
        #check through each element in row and see if equal to num and make sure it is not in pos - i.e the position you just inserted num in
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
        
        #check column
        for i in range(len(bo)):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False
            
        #check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        
        #loop through box and ensure that the same number has not been entered twice
        #boxes are essentailly : x axis pos 0, 1 ,2 and y axis 0,1,2 - this is why we multiply by 3
        for i in range(box_y *3, box_y * 3 + 3):
            for j in range(box_x *3, box_x * 3 + 3):
                if bo[i][j] == num and (i,j) != pos:
                    return False
        
        return True

def print_board(bo):
    #this will draw in dashed lines below each sudoku box
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -  ')
        #this will print line at side of each sudoku box    
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end ="")

            if j == 8:
                print(bo[i] [j])
            else:
                print(str(bo[i][j]) + " ", end = "")
            

def find_empty(bo):
    for i in range(len(bo)):
        #length of each row
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row , col 
            
    return None


print_board(board)
solve(board)
print('\n')
print_board(board)


    
    