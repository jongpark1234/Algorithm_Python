score = [0, 0]
for _ in range(int(input())):
	a, b = map(int, input().split())
	if a > b:
		score[0] += 1
	elif a < b:
		score[1] += 1
print(*score)
