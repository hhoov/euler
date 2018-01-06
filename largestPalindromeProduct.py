# -----------------------------
# Project Euler Problem 4: Largest Palindrome Product
# 		Find the largest palindrom made from the product of two 3-digit numbers
# -----------------------------

def largestPalindromeProd():
	largestPalindrome = 0
	for firstNumber in range(999,100,-1):
		for secondNumber in range(999,100,-1): 
			result = firstNumber * secondNumber
			resultReversed = reverseString(str(result))

			if str(result) == str(resultReversed):
				largestPalindrome = keepLargestPalindrome(largestPalindrome, result)
				break
			else:
				continue
		
	print("Largest palindrome: {0} from the product of {1} and {2}".format(largestPalindrome, firstNumber, secondNumber))

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