rows, cols = map(int, input().split())
matrix = []
for i in range(rows):
	row = list(map(int, input().split()))
	matrix.append(row)
max_value = matrix[0][0]
max_j = 0
max_k = 0
for j in range(rows):
	for k in range(cols):
		if max_value < matrix[j][k]:
			max_value = matrix[j][k]
			max_j = j
			max_k = k
print(max_value)
print("Row: ", max_j + 1)
print("Column: ", max_k + 1)			
			
	
		
