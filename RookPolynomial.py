def countCells(board,sizeMatrix):
    count = 0
    for i in range(sizeMatrix):
        for j in range(sizeMatrix):
            if(board[i][j] == False):
                count +=1
    return count

def findFirst(board,sizeMatrix):
    for i in range(0,sizeMatrix):
        for j in range(0,sizeMatrix):
            if(board[i][j] == False):
                return (i,j)

def delColAndRow(board,sizeMatrix,first):
    newBoard = []
    for i in range(0,sizeMatrix):
        newBoard_col = []
        for j in range(0,sizeMatrix):
            newBoard_col.append(board[i][j])
        newBoard.append(newBoard_col)

    col_del = first[1]
    row_del = first[0]

    ##del col
    for i in range(0,sizeMatrix):
        newBoard[i][col_del] = True
    for i in range(0,sizeMatrix):
        newBoard[row_del][i] = True
    return newBoard


def delCell(board,sizeMatrix,first):
    newBoard = []
    for i in range(0,sizeMatrix):
        newBoard_col = []
        for j in range(0,sizeMatrix):
            newBoard_col.append(board[i][j])
        newBoard.append(newBoard_col)
    col_del = first[1]
    row_del = first[0]
    newBoard[row_del][col_del] = True
    return newBoard

def add2Vector(subPoly_1,subPoly_2):
    add = []
    minSize = min(len(subPoly_1),len(subPoly_2))
    for i in range(0,minSize):
        current = subPoly_1[i] + subPoly_2[i]
        add.append(current)

    if(minSize<len(subPoly_1)):
        for i in range(minSize,len(subPoly_1)):
            add.append(subPoly_1[i])
    if(minSize < len(subPoly_2)):
        for i in range(minSize,len(subPoly_2)):
            add.append(subPoly_2[i])

    return add



def rookPoly(board,sizeMatrix):
    poly = []
    poly.append(1)
    countCell = countCells(board,sizeMatrix)
    if(countCell == 0):
        return poly
    elif(countCell == 1):
        poly.append(1)
        return poly
    else:
        first = findFirst(board,sizeMatrix)
        board_sub1 = delColAndRow(board,sizeMatrix,first)
        board_sub2 = delCell(board,sizeMatrix,first)

        subPoly_1 = rookPoly(board_sub1,sizeMatrix)
        subPoly_2 = rookPoly(board_sub2,sizeMatrix)
        subPoly_1.insert(0,0)
        poly = add2Vector(subPoly_1,subPoly_2)
        return poly
