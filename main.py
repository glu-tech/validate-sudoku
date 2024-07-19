def isValidSudoku(board: [[str]]) -> bool:
    subBoard:[[str]] = []

    for i in range(len(board)):
        countNumbersLine = []
        countNumbersColumn = []
        for j in range(len(board[i])):
            if board[i][j] != "." and board[i][j] not in countNumbersLine:
                countNumbersLine.append(board[i][j])
            elif board[i][j] != ".":
                return False

            if board[j][i] != "." and board[j][i] not in countNumbersColumn:
                countNumbersColumn.append(board[j][i])
            elif board[j][i] != ".":
                return False

    limit = 7
    countLine = 0
    countColumn = 0
    countSubBoard = 0
    while countColumn < limit and countLine < limit:
        subBoard.append([])
        subBoard[countSubBoard].append(board[countColumn][countLine])
        subBoard[countSubBoard].append(board[countColumn][countLine+1])
        subBoard[countSubBoard].append(board[countColumn][countLine+2])
        subBoard[countSubBoard].append(board[countColumn+1][countLine])
        subBoard[countSubBoard].append(board[countColumn+1][countLine+1])
        subBoard[countSubBoard].append(board[countColumn+1][countLine+2])
        subBoard[countSubBoard].append(board[countColumn+2][countLine])
        subBoard[countSubBoard].append(board[countColumn+2][countLine+1])
        subBoard[countSubBoard].append(board[countColumn+2][countLine+2])
        if countColumn + 3 < limit:
            countColumn += 3
        else:
            countLine += 3
            countColumn = 0

        countSubBoard += 1

    for i in range(len(subBoard)):
        countNumbersThreeForThree = []
        for j in range(len(subBoard[i])):
            if subBoard[i][j] != "." and subBoard[i][j] not in countNumbersThreeForThree:
                countNumbersThreeForThree.append(subBoard[i][j])
            elif subBoard[i][j] != ".":
                return False

    return True

print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."]
                    ,[".","9","8",".",".",".",".","6","."]
                    ,["8",".",".",".","6",".",".",".","3"]
                    ,["4",".",".","8",".","3",".",".","1"]
                    ,["7",".",".",".","2",".",".",".","6"]
                    ,[".","6",".",".",".",".","2","8","."]
                    ,[".",".",".","4","1","9",".",".","5"]
                    ,[".",".",".",".","8",".",".","7","9"]]))