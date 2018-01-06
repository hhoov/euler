
def smallestMultiple():
	number = 1
	while True:
		for divisor in range (1,10):
			if number % divisor == 0:
				continue
			else:
				number = number + 1
				break