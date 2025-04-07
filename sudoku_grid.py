def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    new_list =[]
    for element in row: 
        if element >0:
            if element not in new_list:
                new_list.append(element)
            else:
                return False
    return True

def column_correct(sudoku: list, column_no: int):
    new_list =[]
    for row in sudoku:
        if row[column_no]>0:
            if row[column_no] not in new_list:
                new_list.append(row[column_no])
            else:
                return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    new_list =[]
    for i in range(row_no, row_no+3):
        for j in range(column_no, column_no+3):
            if sudoku[i][j] >0:
                if sudoku[i][j] not in new_list:
                    new_list.append(sudoku[i][j])
                else:
                    return False
    return True

#here we first run a for loop from itr 0 to 8 and then will check if either of row function or column
#function return FALSE and if not then will have for loop for row and col from range(0, 9,3) and will call 
#block_current and if any block is false then return false or else return True

def sudoku_grid_correct(sudoku: list):
    for i in range(9):
        if (row_correct(sudoku, i) == False) or (column_correct(sudoku, i) == False):
            return False

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if (block_correct(sudoku, row, col) == False):
                return False
    return True


if __name__ == "__main__":
    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))