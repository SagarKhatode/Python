def printEvenNum():
	num = 2
	for x in range(10):
		if int(num)%2 == 0:
			print(num, end=" ")
		num += 2 
if __name__ == '__main__':
	printEvenNum()