def showStar(star):
	print("n=", star)
	for i in range(star):
		if i < (star/2):
			print(' ' * (star // 2 - i), end='')
			print('*' * (i * 2 + 1))
		else:
			print(' ' * (star // 2 - star + i + 1), end='')
			print('*' * ((star - i - 1) * 2 + 1))
	print("\n")

showStar(1)
showStar(2)
showStar(3)
showStar(4)
showStar(5)
showStar(9)