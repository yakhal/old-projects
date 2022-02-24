def makeLatinSquare(matrix):
    for i in range(len(matrix)):
        for j in range(0, i):
            matrix[i].insert(0, matrix[i].pop())
def rotate(matrix):
    for i in range(len(matrix)):
        matrix[i].insert(0, matrix[i].pop())
def printMatrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=' ')
        print()
##    print()
def trace(matrix):
    trace = 0
    for i in range(len(matrix)): trace += matrix[i][i]
    return trace
        
for testCase in range(int(input())):
    n, k = list(map(int, input().split()))
    matrix = [[i for i in range(n, 0, -1)] for j in range(1, n+1)]
    makeLatinSquare(matrix)
    found = False
    for i in range(n):
        rotate(matrix)
##        printMatrix(matrix)
        if trace(matrix) == k:
            found = True
            break
    if found:
        print('Case #{}: POSSIBLE'.format(testCase+1))
        printMatrix(matrix)
    else:
        print('Case #{}: IMPOSSIBLE'.format(testCase+1))

