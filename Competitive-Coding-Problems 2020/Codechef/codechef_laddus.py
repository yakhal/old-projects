for testcase in range(int(input())):
    noOfAct, origin = input().split()
    activities = []
    totalLaddus = 0
    for act in range(int(noOfAct)):
        activities.append(input().split())
    for a in activities:
        if len(a) == 1:
            if a[0] == 'TOP_CONTRIBUTOR':
                totalLaddus += 300
            else: totalLaddus += 50
        else:
            if a[0] == 'CONTEST_WON':
                rank = int(a[1])
                totalLaddus += 300 + (0 if rank > 20 else (20 - rank))
            else:
                totalLaddus += int(a[1])
    if origin == "INDIAN" : print(totalLaddus // 200)
    else: print(totalLaddus // 400)
            
        
