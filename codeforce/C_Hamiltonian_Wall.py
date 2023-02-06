for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	for i in range(n): a[i] %= 3
	
	x, y = a.count(1), a.count(2)
	x, y = min(x, y), max(x, y)

	ans = 0
	while y >= x + 3:
		ans += 1
		x += 2
		y -= 2
	x, y = min(x, y), max(x, y)
	if y == x+1:
		if x > 0: ans += 2
		else: ans += 6
	if y == x+2:
		if x > 1 or (x > 0 and x+y < n): ans += 4
		else: ans += 5
	print(ans + x)