for testCase in range(int(input())):
    N = int(input())
    prices = list(map(int, input().split()))
    prices.sort(reverse = True)
    yearsPassed = 0
    profitEarned = 0
    for price in prices:
        profit = (price - yearsPassed)
        profitEarned += profit if profit > 0 else 0
        yearsPassed += 1
    print(profitEarned%1000000007)
