# -----------------------------
# Project Euler Problem 5: Smallest Multiple
# 		What is the smallest positive number that is evenly divisible by all of the numbers 
#			from 1 to 20?
# -----------------------------

def smallestMultiple():
	number = 2520
	divisorsAllSatisfied = 1
	while divisorsAllSatisfied != 21:
		if isEvenFactor(number, divisorsAllSatisfied) == True:
			divisorsAllSatisfied = divisorsAllSatisfied + 1
			if divisorsAllSatisfied >= 19:
				print("Divisors Satisfied: {}".format(divisorsAllSatisfied))
				print("Number is: {}".format(number))
			continue
		else:
			divisorsAllSatisfied = 1
			number = number + 2
			continue
	print("Smallest number is {}".format(number))
	print("divisorsAllSatisfied is: {}".format(divisorsAllSatisfied))

def isEvenFactor(number, divisorsAllSatisfied):
	return number % divisorsAllSatisfied == 0
	

def main():
	smallestMultiple()

if __name__ == '__main__':
	main()