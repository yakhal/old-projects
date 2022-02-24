budget = []

for i in range(int(input())):
    budget.append(int(input()))
budget.sort()
revenue = 0
##print(budget)
for i in range(len(budget)):
    buyers = len(budget) - i
    r = budget[i]*buyers
##    print(f'{budget[i]}*{buyers} = {r}')
    if revenue < r : revenue = r
print(revenue)
    
