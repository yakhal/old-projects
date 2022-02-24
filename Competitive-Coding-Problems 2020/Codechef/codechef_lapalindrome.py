def lapindrome(str1, str2):
    for c in str1:
        if str1.count(c) != str2.count(c):
            return False
    return True

for i in range(int(input())):
    s = input()
    mid = len(s) // 2
    if len(s) % 2 == 0:
        if lapindrome(s[0:mid], s[mid:]) : print('YES')
        else: print('NO')
    else:
        if lapindrome(s[0:mid], s[mid+1:]) : print('YES')
        else : print('NO')
