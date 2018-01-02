
def even_Fib_Nums():
	first_term = 1
	second_term = 2
	total_Sum = 0
	while first_term < 10 and second_term < 10:

		if first_term % 2 == 0:
			total_Sum = total_Sum + first_term
		if second_term % 2 == 0:
			total_Sum = total_Sum + second_term
		
		new_term = first_term + second_term
		first_term = second_term
		second_term = new_term
		print("---------------------")
		print("First term -- ", first_term)
		print("Second term -- ", second_term)
		print("New term -- ", new_term)
		print("Total Sum of Evens -- ", total_Sum)
		print("---------------------")

def main():
	even_Fib_Nums()

if __name__ == '__main__':
	main()
