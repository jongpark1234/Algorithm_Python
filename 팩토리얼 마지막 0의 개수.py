from sys import stdin
n = int(stdin.readline())
num = 1
for i in range(1, n + 1):
    num *= i
cnt = 0
for i in str(num)[::-1]:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)
