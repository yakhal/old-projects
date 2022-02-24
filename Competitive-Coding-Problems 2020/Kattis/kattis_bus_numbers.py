n = int(input())
while True :
    a = list(map(int, input().split()))
    a.sort()
    consecutives = 0
    newList = []
    for i in range(n-1):
        if a[i] - a[i+1]:
            consecutives += 1
        else:
            if consecutives < 2:
                consecutives = 0
                newList.append(a[i])
            else:
                newList.append('{}-{}'.format(a[i-consecutives-1], a[i-1]))
        if consecutives >= 2 
        
