def achievable(money, target):
    if money == target : return 'Yes'
    elif money > target : return 'No'
    else:
        for n in [10, 20]:
            if achievable(money*n, target) == 'Yes' :
                return 'Yes'  
        return 'No'

money = []
for i in range(int(input())):
    money.append(int(input()))

for m in money:
    print(achievable(1, m))
        
