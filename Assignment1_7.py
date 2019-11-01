def checkNum(num):
	if int(num)%5 == 0:
		return True
	else:
		return False


if __name__ == '__main__':
	print("Enter a number: ")
	num = input()
	print(checkNum(num))