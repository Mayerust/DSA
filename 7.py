rows, cols = map(int, input().split())
matrix = []
rotated = []
for i in range(rows):
	row = list(map(int, input().split()))
	matrix.append(row)
for k in range(cols):
	new_row = []
	rotated_row = []
	for j in range(rows):
		new_row.append(matrix[j][k])
	rotated_row = new_row[::-1]
	rotated.append(rotated_row)
for row in rotated:
	print(*row)		
