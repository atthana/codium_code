def showStar(star):
	print("n=", star)
	print(' '* (star-1), end = '')
	print('*', end='')
	print(' ' * (star-1))
	for i in range(star-1):
		print(' '*((star-i)-2), end='')
		print('*', end='')
		print(' '*((i*2)+1), end='')
		print('*')
	print("\n")


showStar(1)
showStar(2)
showStar(3)
showStar(4)
showStar(5)

