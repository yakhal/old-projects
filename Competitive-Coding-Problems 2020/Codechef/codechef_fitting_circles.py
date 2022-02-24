rects = []
for i in range(int(input())):
    rects.append(list(map(int, input().split())))

for l, b in rects:
    print(max(l, b)//min(l, b))
