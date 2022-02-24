from random import randint
d = {2:'2486', 4:'4862', 8:'8624', 6:'6248'}

for i in range(int(input())):
    size, d0, d1 = list(map(int, input().split()))
##    print(size, d0, d1)
    if (d0 + d1) != 10 and d0+d1 != 5:
        if size >= 3 and d0+d1 != 15:
            startNumber = (d0+d1+(d0+d1)%10)%10
            midNumSize = (size-3)//4
            lastNumber = d[startNumber][0:(size-3)%4]
            finalNumber = str(d0) + str(d1) + str((d0+d1)%10) \
                          + lastNumber
            summation = 20*midNumSize
            for i in finalNumber: summation += int(i)
            print('YES' if summation%3 == 0 else 'NO')
        elif size >= 3 and d0+d1 == 15:
            print('NO')
        elif size == 2 :
            print('YES' if (d0+d1)%3 == 0 else 'NO')
##        print(startNumber, midNumSize, finalNumber, lastNumber)
##        print(summation)
    else:
        print('NO')

##list(map(int, input().split()))
##randint(2, 10**12), randint(1, 9), randint(0, 9)
