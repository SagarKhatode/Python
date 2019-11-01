def checkNum(num):
	if int(num) == 0:
		print("ZERO")
	elif int(num) > 0:
		print("POSITIVE")
	elif int(num) < 0:
		print("NEGATIVE")

if __name__ == '__main__':
	print("Enter a number: ")
	num = input()
	checkNum(num)