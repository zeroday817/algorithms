#recursion
def print_countdown(num):
	print(num)
	if(num == 0):
		return
	else:	
		print_countdown(num - 1)

def fact(num):

	if(num == 1):
		return 1
	else:
		return num * fact(num - 1)
