
def even_Fib_Nums():
	first_term = 1
	second_term = 2
	total_Sum = 0
	new_term = 0

	if first_term % 2 == 0:
		total_Sum = total_Sum + first_term
	if second_term % 2 == 0:
		total_Sum = total_Sum + second_term

	while first_term <= 4000000 and second_term <= 4000000 and new_term <= 4000000:

		new_term = first_term + second_term
		first_term = second_term
		second_term = new_term

		if new_term % 2 == 0 and new_term <= 4000000:
			total_Sum = total_Sum + new_term

	print("First term: {}".format(first_term))
	print("Second term: {}".format(second_term))
	print("New term: {}".format(new_term))
	print("Total Sum of Evens: {}".format(total_Sum))

def main():
	even_Fib_Nums()

if __name__ == '__main__':
	main()
