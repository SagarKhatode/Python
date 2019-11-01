def printStar(num):
	i = 1
	while i <= int(num):
		print("*", end = " ")
		i += 1
	

if __name__ == '__main__':
	print("Enter a number: ")
	num = input()
	printStar(num)