rows, cols = map(int, input().split())
matrix = []
for i in range(rows):
	row = list(map(int, input().split()))
	matrix.append(row)
transpose = []
for k in range(cols):
	new_row = []
	for j in range(rows):
		new_row.append(matrix[j][k])
	transpose.append(new_row)
for row in transpose:
	print(*row)			
