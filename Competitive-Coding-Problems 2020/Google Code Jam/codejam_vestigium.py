for testCase in range(int(input())):
    N = int(input())
    matrix = []
    r = 0
    c = 0
    trace = 0
    for row in range(N):
        matrix.append(list(map(int, input().split())))
    # Row Check
    for row in matrix:
        s = set(row)
        if len(s) < N: r += 1
    # Column check
    for i in range(N):
        column = []
        for j in range(N):
            column.append(matrix[j][i])
        s = set(column)
        if len(s) < N: c += 1
    # Trace
    for i in range(N):
        trace += matrix[i][i]
    print('Case #{}: {} {} {}'.format(testCase+1, trace, r, c))
    
