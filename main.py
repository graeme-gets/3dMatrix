# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy
from numpy import matrix

Matrix3D = []


def PrintMatrix(matrix):
    # Hpw many arrays to print
    for i in range(0, 3):
        print(formatMatrixRow(matrix[i], 3))


def formatMatrixRow(row, width):
    return (f"|{str.center(str(row[0]), width, ' ')} "
            f"{str.center(str(row[1]), width, ' ')} "
            f"{str.center(str(row[2]), width, ' ')} |")


def PrintMatrixList(matrixLst, cols):
    noofMatrix = len(matrixLst)
    for i in range(0, noofMatrix):
        s = ""
        for col in range(0, cols):
            m = matrixLst[i]
            s = s + formatMatrixRow(m[col],3) + "   "
        print(s)


def EnteredMatrix():
    for i in range(0, 3):
        row = input(f"Enter in row {i + 1} : ")
        row = row.replace(" ", "")
        rowSplit = row.split(',')
        if len(rowSplit) != 3:
            print(f"Syntax Error : {rowSplit}")
            exit()
        rowArray = []
        for j in range(0, 3):
            rowArray.append(int(rowSplit[j]))
        Matrix3D.append(rowArray)

    lst = []
    lst.append(Matrix3D)
    lst.append(Matrix3D.reverse())
    PrintMatrix(Matrix3D)
    PrintMatrixList(lst,2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    EnteredMatrix()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
