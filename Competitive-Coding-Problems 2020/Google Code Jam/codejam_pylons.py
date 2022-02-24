def check(r1, c1, path):
    if len(path) == r*c :
        return path
    else:
        for r2 in range(r):
            found = False
            for c2 in range(c):
                if r1 != r2 and c1 != c2 and r1-c1 != r2-c2 and r1 + c1 != r2+c2 and (r2, c2) not in path:
                    found = True
                    path.append((r2, c2))
                    return check(r2, c2, path)
        if not found:
            return None

def printAns(l):
    for i, j in path:
        print(i+1, j+1)

for testCase in range(int(input())):
    r,c = list(map(int, input().split()))
    grid = [[0 for c0 in range(c)] for r0 in range(r)]
    for i in range(r):
        found = False
        for j in range(c):
            path = check(i, j, [(i, j)])
            if path: 
                found = True
                break
        if found : break
    if found:
        print('Case #{}: {}'.format(testCase+1, 'POSSIBLE'))
        printAns(path)
    else:
        print('Case #{}: {}'.format(testCase+1, 'IMPOSSIBLE'))
    

        
        
    