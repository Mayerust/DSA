#haha this is my first real program :)
def hello_world(n):
	a = n
	if n == 0:
		print("Hello World")
	elif n >= 1 and n <= 10:
		while n <= 10:
			print ("*" * n)
			n = n + 1
		while a <= n:
			print ("*" * (n - 1))
			n = n - 1	
	else:
		print("Invalid Value")		
n = int(input("Enter a value from 1 - 10"))
hello_world(n)			
