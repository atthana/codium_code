def showStar(star):
	print("n=", star)
	r = (2 * star) - 1
	for i in range(r):
		if i < r / 2:
			print('A' * (r // 2 - i), end='')
			print('+', end='')
			print('E' * (i * 2 - 1), end='')
			if i > 0:
				print('+', end='')
			print('B' * (r // 2 - i))
		else:
			print('C' * (r // 2 - r + i + 1), end='')
			print('+', end='')
			print('E' * (2 * r - 2 * i - 3), end='')
			if i < r - 1:
				print('+', end='')
			print('D' * (r // 2 - r + i + 1))
	print("\n")


showStar(1)
showStar(2)
showStar(3)
showStar(4)