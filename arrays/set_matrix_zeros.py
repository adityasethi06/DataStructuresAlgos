# Problem Statement: Given a matrix if an element in the matrix is 0 
# then you will have to set its entire column and row to 0 and then return the matrix.

# Examples 1:

# Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]

# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.
 
# Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

# Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. 
# Therefore 1st row, 1st column and 4th column will be set to 0

def set_matrix_zero(mat: [[int]]):
    rows, cols = len(mat), len(mat[0])
    first_row_zero = False
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                if i == 0:
                    first_row_zero = True
                else:
                    mat[i][0] = 0
                mat[0][j] = 0
    for c in range(1, cols):
        if mat[0][c] == 0:
            for r in range(1, rows):
                mat[r][c] = 0
    for r in range(1, rows):
        if mat[r][0] == 0:
            for c in range(1, cols):
                mat[r][c] = 0
    if mat[0][0] == 0:
        for r in range(rows):
            mat[r][0] = 0
    if first_row_zero:
        for c in range(cols):
            mat[0][c] = 0

def print_2d_matrix(mat):
    for row in mat:
        print(*row, sep=' ')

if __name__ == '__main__':
    matrix=[[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]
    # matrix=[[1,1,1],[1,0,1],[1,1,1]]
    print(f"input matrix: \n")
    print_2d_matrix(matrix)
    set_matrix_zero(matrix)
    print(f"output matrix: \n")
    print_2d_matrix(matrix)