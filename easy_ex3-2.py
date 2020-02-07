def showStar(star):
	print("n=", star)
	for i in range(star):
		i = i + 1
		print(' '*(star-i) ,'*' * i)
	print("\n")

showStar(3)
showStar(4)
showStar(6)