# -----------------------------
# Project Euler Problem 3: Largest prime factor
# 		What is the largest prime factor of the number 600851475143?
# -----------------------------

def largestPrimeFactor():

	number = 600851475143
	divisor = 1
	largestPrime = 0

	while divisor <= number:
		#print("\nDivisor is: {}".format(divisor))
		#print("Number is: {}".format(number))
		#print("Largest prime is: {}\n".format(largestPrime))

		if number % divisor == 0:
			#print("Divisible by divisor.")
			number = number / divisor
			if divisor % 2 != 0 or divisor % 3 != 0:
				#print("Prime number.")
				largestPrime = divisor
				divisor = divisor + 1
			else:
				#print("Non-prime. Increasing divisor.")
				divisor = divisor + 1
		else:
			#print("Not divisible. Increasing divisor.")
			divisor = divisor + 1

		#print("\nDivisor is NOW: {}".format(divisor))
		#print("Number is NOW: {}".format(number))
		#print("Largest prime is NOW: {}\n".format(largestPrime))
	print("Largest Prime Factor is: {}".format(largestPrime))

def main():
	largestPrimeFactor()
if __name__ == '__main__':
	main()