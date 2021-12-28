# my sample sudoku board
board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]
         ]


# function to display 2D sudoku board
def display_board(bo):
    print("   " + "MY SUDOKU BOARD:\n")

    for i in range(len(bo)):

        if i % 3 == 0 and i != 0:
            # print("-----------------------------")
            print("- - - - - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j != 8:
                print(str(bo[i][j]) + "  ", end="")
            else:
                print(bo[i][j])  # this doesn't have end = "" since after the last number we want
                # the print to go in the next row


# Displays 2D Sudoku Board
# display_board(board)


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, column


# print(find_empty(board))
