for test in range(int(input())):
    g = int(input())
    for game in range(g):
        i, n, q = list(map(int, input().split()))
        if i == 1: print(n//2 if q == 1 else (n - n//2))
        else : print((n - n//2) if q == 1 else n//2)
