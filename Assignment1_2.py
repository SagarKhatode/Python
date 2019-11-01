
def chkNum(a):
	if int(a)%2 == 0:
		print("Even Number")
	else:
		print("Odd Number")

if __name__ == '__main__':
	print("Enter a Number: ")
	chkNum(input())