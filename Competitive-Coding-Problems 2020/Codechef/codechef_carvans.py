for testcase in range(int(input())):
    size = int(input())
    speeds = list(map(int, input().split()))
    cars = 1
    for i in range(1, len(speeds)):
        if speeds[i] > speeds[i-1] :
            speeds[i] = speeds[i-1]
        else:
            cars += 1
    print(cars)
