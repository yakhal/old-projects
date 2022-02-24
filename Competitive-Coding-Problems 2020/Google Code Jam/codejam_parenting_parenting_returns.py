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
    timeRequired = []
    for s, e in acts: timeRequired.append(e-s)
##    print('TestCase:',testCase+1, acts)
##    print(timeRequired)
    sch = ''
    for r in range(len(acts)):
        if not sch: sch += random.choice(('C', 'J'))
        else :
            busyJ = False
            busyC = False
##            print('Schedule {} {}'.format(testCase+1, sch))
            
            for check in range(len(acts[:r])):
                if overLap(acts[r][0], acts[r][1], acts[check][0], acts[check][1]):
##                    print('BusyJ : {}, BusyC: {}'.format(busyJ, busyC))
                    if sch[check] == 'J': busyJ = True
                    elif sch[check] == 'C' : busyC = True
##                    print('BusyJ : {}, BusyC: {}'.format(busyJ, busyC) )
            if not busyJ and not busyC: sch += random.choice(('C', 'J'))
            elif not busyJ: sch += 'J'
            elif not busyC : sch += 'C'
            else :
                sch = 'IMPOSSIBLE'
                break
    print('Case #{}: {}'.format(testCase+1, sch))
    acts.sort()
    print(acts)
