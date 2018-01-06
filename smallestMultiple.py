
def smallestMultiple():
	number = 1
	divisorsAllSatisfied = 1
	while divisorsAllSatisfied != 20:
		if number % divisorsAllSatisfied == 0:
			divisorsAllSatisfied = divisorsAllSatisfied + 1
			print("Divisors Satisfied: {}".format(divisorsAllSatisfied))
			print("Number is: {}".format(number))
			continue
		else:
			divisorsAllSatisfied = 1
			number = number + 1
			continue
	print("Smallest number is {}".format(number))
	print("divisorsAllSatisfied is: {}".format(divisorsAllSatisfied))

def main():
	smallestMultiple()

if __name__ == '__main__':
	main()