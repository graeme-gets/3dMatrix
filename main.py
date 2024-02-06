# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

Matrix3D = []
MatrixNull = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def PrintMatrix(matrix):
    # Hpw many arrays to print
    for i in range(0, 3):
        print(formatMatrixRow(matrix[i], 3))


def formatMatrixRow(row, width):
    return (f"|{str.center(str(row[0]), width, ' ')} "
            f"{str.center(str(row[1]), width, ' ')} "
            f"{str.center(str(row[2]), width, ' ')} |")


# https://stackoverflow.com/questions/434287/how-to-iterate-over-a-list-in-chunks
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def PrintMatrixList(matrixLst, cols):
    for group in chunker(matrixLst, cols):
        s = ""
        for row in range(3):
            for m in range(cols):
                if m >= len(group):
                    s = s + f"{formatMatrixRow(MatrixNull[row], 3)}\t"
                else:
                    s = s + f"{formatMatrixRow(group[m][row],3)}\t"
            print(s)
            s = ""
        print("")


def EnteredMatrix():
    # for i in range(0, 3):
    #     row = input(f"Enter in row {i + 1} : ")
    #     row = row.replace(" ", "")
    #     rowSplit = row.split(',')
    #     if len(rowSplit) != 3:
    #         print(f"Syntax Error : {rowSplit}")
    #         exit()
    #     rowArray = []
    #     for j in range(0, 3):
    #         rowArray.append(int(rowSplit[j]))
    #     Matrix3D.append(rowArray)

    lst = [ ]
    lst.append([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    lst.append([[4, 4, 4], [5, 5, 5], [6, 7, 7]])
    lst.append([[7, 7, 7], [8, 8, 8], [9, 9, 9]])
    #PrintMatrix(Matrix3D)
    PrintMatrixList(lst, 2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    EnteredMatrix()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
