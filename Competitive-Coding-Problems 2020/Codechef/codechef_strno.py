for i in range(int(input())):
    x, k = list(map(int, input().split()))
    if x < k:
        print(0)
    elif x == k:
        print(0)
    elif x > k :
        if x - k > 1:
            print(1)
        else:
            print(0)
