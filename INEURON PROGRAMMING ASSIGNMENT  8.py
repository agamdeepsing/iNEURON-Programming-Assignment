
class MatrixOperations:
    def add_matrices(matrix_1, matrix_2):
        result = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]

        for i in range(len(matrix_1)):
            for j in range(len(matrix_1[0])):
                result[i][j] = matrix_1[i][j] + matrix_2[i][j]

        return result

    def multiply_matrices(matrix_3, matrix_4):
        result = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]

        for i in range(len(matrix_3)):
            for j in range(len(matrix_3[0])):
                result[i][j] = matrix_3[i][j] * matrix_4[i][j]

        return result

    def transpose_matrix(matrix):
        rows = len(matrix)
        column = len(matrix[0])

        transpose = []
        for i in range(column):
            transpose.append([0]*rows)

        for i in range(rows):
            for j in range(column):
                transpose[j][i] = matrix[i][j]
    
        return transpose

    def sort_string():
        string = input("Enter a String: ").title()
        sorted = sorted(string.split(' '))
        print(' '.join(sorted))

    def remove_punctuations():
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        in_string = input('Enter a String: ')
        out_string = ''
        for ele in in_string:
            if ele not in punctuations:
                out_string += ele
        print(out_string)


# Testing the methods

matrix_1 = [[8, 7, 9],
           [5, 9, 4],
           [0, 6, 3]]

matrix_2 = [[9, 8, 6],
           [5, 1, 3],
           [4, 8, 11]]

result = MatrixOperations.add_matrices(matrix_1, matrix_2)
print("Matrix 1:")
for row in matrix_1:
    print(row)

print("Matrix 2:")
for row in matrix_2:
    print(row)

print("Result Matrix:")
for row in result:
    print(row)

matrix_3 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix_4 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

result = MatrixOperations.multiply_matrices(matrix_3, matrix_4)
print("Matrix 3:")
for row in matrix_3:
    print(row)

print("Matrix 4:")
for row in matrix_4:
    print(row)

print("Result Matrix:")
for row in result:
    print(row)

matrix= [[2,6,8],
         [7,8,4],
         [6,4,2]]

transpose = MatrixOperations.transpose_matrix(matrix)
for row in matrix:
    print(row)

for row in transpose:
    print(row)

MatrixOperations.sort_string()

MatrixOperations.remove_punctuations()
