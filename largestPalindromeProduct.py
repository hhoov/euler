# -----------------------------
# Project Euler Problem 4: Largest Palindrome Product
# 		Find the largest palindrom made from the product of two 3-digit numbers
# -----------------------------

def largestPalindromeProd():
	firstNumber = 99
	secondNumber = 10
	largestPalindrome = 0
	result = 0
	while (firstNumber > 10 and firstNumber < 99) and (secondNumber > 10 and secondNumber < 99):
		result = firstNumber * secondNumber
		#print("Result: {}".format(result))
		resultReversed = reverseString(str(result))
		#print("Reversed result: {}".format(resultReversed))
		#print("Result AGAIN: {}".format(result))
		if str(result) == str(resultReversed):
			largestPalindrome = keepLargestPalindrome(largestPalindrome, result)
			print("Largest PAL: {}".format(largestPalindrome))
			firstNumber = firstNumber - 1
			secondNumber = secondNumber + 1
		else:
			firstNumber = firstNumber - 1
			secondNumber = secondNumber + 1
	print("Largest palindrome: {0} from the product of {1} and {2}".format(result, firstNumber, secondNumber))

def reverseString(inputString):
	return inputString[::-1]

def keepLargestPalindrome(currentResult, newResult):
	if currentResult >= newResult:
		return currentResult
	else:
		return newResult


def main():
	largestPalindromeProd()

if __name__ == '__main__':
	main()