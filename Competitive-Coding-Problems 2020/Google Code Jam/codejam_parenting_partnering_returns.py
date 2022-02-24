import random
def overLap(a1, b1, a2, b2):
    v1, v2 = ((a1 - b2), (b1 - a2))
    b = not ((v1 >= 0 and v2 >= 0) or (v1 <= 0 and v2 <= 0))
##    print('OverlapCheck for ({}, {}) and ({}, {}) {} v1 = {}, v2 = {}'.format(a1, b1, a2, b2, b, v1, v2))
    return b
        
for testCase in range(int(input())):
    N = int(input())
    acts = []
    for n in range(N):
        acts.append(list(map(int, input().split())))
    sch = ''
    d = {i:acts[i] for i in range(N)}
##    print(d)
    acts.sort()
##    print(acts)
##    for i in range(N):
##        for j in range(i, N):
##            if i != j:
##                print(f'Overlap between {acts[i][0]},{acts[i][1]} and {acts[j][0]},{acts[j][1]} is {overLap(acts[i][0],acts[i][1],acts[j][0],acts[j][1])}')
    jBusy = False
    cBusy = False
    sch = ''
    jEnd = 0
    cEnd = 0
    for i in range(N):
        s, e = acts[i]
        if not cBusy:
            cEnd = e
            cBusy = True
            sch += 'C'
        elif not jBusy:
            jEnd = e
            jBusy = True
            sch += 'J'
        elif cEnd <= s :
            cEnd = e
            sch += 'C'
        elif jEnd <= s :
            jEnd = e
            sch += 'J'
        else :
            sch = 'IMPOSSIBLE'
            break
##        print(i, sch)
    newSch = ''
    if sch != 'IMPOSSIBLE':
        for i in d.keys():
##            acts[acts.index(d[i])]
            newSch += sch[acts.index(d[i])]
            acts[acts.index(d[i])] = None 
    else: newSch = sch
    print('Case #{}: {}'.format(testCase+1, newSch))



