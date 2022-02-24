for testCase in range(int(input())):
    N = int(input())
    array = list(map(int, input().split()))
    onesPos = []
    for i in range(len(array)):
        if array[i] == 1:
            onesPos.append(i)
##    print(onesPos)
    if N == 1:
        print('YES')
    elif N == 2:
        print('YES' if len(onesPos) == 1 else 'NO')
    else:
        ruleBreak = False
        for i in range(1, len(onesPos)):
            if onesPos[i] - onesPos[i-1] < 6:
                ruleBreak = True
        if ruleBreak: print('NO')
        else: print('YES')
        
        
