def showStar(star):
	print("n=", star)
	for i in range(star):
		if i < star//2:
			print(' ' * i, end='')
			print('*', end='')
			print(' ' * (star - i * 2 - 2), end='')
			print('*')
		elif i == star//2 and star % 2 != 0:
			print(' ' * i, end='')
			print('*')
		else:
			print(' ' * (star - i - 1), end='')
			print('*', end='')
			print(' ' * (i * 2 - star), end='')
			print('*')
	print("\n")

showStar(1)
showStar(2)
showStar(3)
showStar(4)
showStar(5)