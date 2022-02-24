from collections import defaultdict
##Naive Algorithm
def Znaive(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    count = 0
    for number in str(fact)[-1::-1]:
        if number == '0':
            count += 1
        else: break
    return count

## Smart Algorithm
def Z(n, power):
    if 5**power == n : return 1
    elif 5**power > n : return 0
    else: return n//(5**power) + Z(n, power+1)

for i in range(int(input())):
    n = int(input())
    print(Z(n, 1))

##d = defaultdict(int)
##for i in range(0, 23457):
##    d[i] = Z(i)
##q = set(d.values())
##print(q)

