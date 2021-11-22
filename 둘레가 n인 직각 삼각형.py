n = int(input())
cnt = 1
for i in range(n // 2):
    for j in range(n // 2):
        for k in range(n // 2):
            if i + j + k == n:
                if i ** 2 + j ** 2 == k ** 2 and i + j > k and i <= j < k:
                    print(f'({cnt}) {i} {j} {k}')
                    cnt += 1