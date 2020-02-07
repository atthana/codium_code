def isLeapYear(year):
	if(year % 400 == 0):
		print(year, ' -> ', "true")
	elif(year % 4 == 0 and year % 100 != 0):
		print(year, ' -> ', "true")
	else:
		print(year, ' -> ', "false")

isLeapYear(1600)
isLeapYear(2000)
isLeapYear(1500)
isLeapYear(2004)
isLeapYear(2008)
isLeapYear(2010)