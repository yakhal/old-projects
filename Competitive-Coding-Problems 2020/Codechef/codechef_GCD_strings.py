# incomplete
def gcd(a, b):
    if b == 0: return a
    else : return gcd(b, a%b)


pairs = []
for i in range(int(input())):
    pairs.append(list(map(int, input().split())))

code = ''
for x, y in pairs:
    if x%y == 0:
        code += '1'
        for i in range(1, x) : code += '0'
    else:
        number = gcd(x,x%y)
        code = bin(number)[2:]
print(code)

