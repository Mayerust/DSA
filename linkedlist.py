class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
n  = int(input())
arr = list(map(int, input().split()))

head = None
current = None		

for value in arr:
	new_node = Node(value)
	
	if head is None:
		head = new_node
		current = new_node
		
	else:
		current.next = new_node
		current = new_node	
				

current = head
while current is not None:
	print(current.data, end = " ")
	current = current.next
