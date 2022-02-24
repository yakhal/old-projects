for testCase in range(int(input())):
    s1 = input()
    s2 = ''
    for i in range(len(s1)):
        if i == 0:
            s2 += '('*int(s1[i])
        s2 += s1[i]
        if i == len(s1)-1:
            s2 += ')'*int(s1[i])
            break
##        s2 += s1[i]
        if int(s1[i]) > int(s1[i+1]):
            s2 += ')' * (int(s1[i]) - int(s1[i+1]))
        elif int(s1[i]) < int(s1[i+1]):
            s2 += '(' * (int(s1[i+1]) - int(s1[i]))
    print('Case #{}: {}'.format(testCase+1, s2))
