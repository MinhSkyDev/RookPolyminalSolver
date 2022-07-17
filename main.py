from tkinter import *
from functools import partial
from RookPolynomial import *

tk = Tk()
tk.geometry("400x400")

global sizeMatrix

board_button = []

board = []
board_bool = []

def changeColorButton(i,j):
    if(board_bool[i][j] == True): ## if the button havent changed color
        board_button[i][j].configure(bg = "#EE4B2B")
        board_bool[i][j] = False
    else:
        board_button[i][j].configure(bg = "#FFFDD0")
        board_bool[i][j] = True

def vectorToLabel(poly):
    textString = ""
    textString += "1 "
    for i in range(1,len(poly)):
        if(i == 1):
            textString+="+ " + str(poly[i]) +"x "
        else:
            textString+="+ " + str(poly[i]) +"x^"+str(i)+" "
    return textString


def solveRookPolynomial():
    global sizeMatrix
    poly = rookPoly(board_bool,sizeMatrix)
    poly_string = vectorToLabel(poly)
    global poly_text_StringVar
    poly_text_StringVar.set(poly_string)

def appearChessboard():
    global sizeMatrix
    global poly_text_StringVar
    for i in range(0,sizeMatrix):
        board_button_col = []
        for j in range(0,sizeMatrix):
            button = Button(tk,bg = "#FFFDD0",height = 1, width = 2, command = partial(changeColorButton,i,j))
            button.place(x = 135 + 25*i, y =10 + 25*j)
            board_button_col.append(button)
        board_button.append(board_button_col)
    solveButton = Button(tk, text = "Solve",height = 5, width = 10, command = solveRookPolynomial)
    solveButton.place(x=150,y= 225)
    poly_text_StringVar = StringVar()
    poly_text = Label(tk, textvariable = poly_text_StringVar)
    poly_text.place(x = 110, y= 200)

def generateBoardBool():
    global sizeMatrix
    for i in range(0,sizeMatrix):
        board_bool_col = []
        for j in range(0,sizeMatrix):
            board_bool_col.append(True)
        board_bool.append(board_bool_col)

def hideConfirmMatrixFrame():
    matrixEnter_label.pack_forget()
    matrixEnter_entry.pack_forget()
    matrixEnter_button.pack_forget()

def confirmedMatrixSize():
    global sizeMatrix
    try:
        sizeMatrix = int(matrixEnter_stringVar.get())
    except:
        errorNumber_label = Label(tk,text = "Số nhập vô không hợp lệ, xin vui lòng nhập lại")
        errorNumber_label.pack()
        return
    hideConfirmMatrixFrame()
    generateBoardBool()
    appearChessboard()

matrixEnter_label = Label(tk, text = "Nhập kích thước của bàn cờ: ")
matrixEnter_stringVar = StringVar()
matrixEnter_entry = Entry(tk, textvariable = matrixEnter_stringVar)
matrixEnter_button = Button(tk, text = "Xác nhận", command = confirmedMatrixSize)
matrixEnter_label.pack()
matrixEnter_entry.pack()
matrixEnter_button.pack()

tk.mainloop()
