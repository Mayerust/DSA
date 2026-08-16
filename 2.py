rows, cols = map(int, input().split())
matrix1 = []
matrix2 = []
for i in range(rows):
	row = list(map(int, input().split()))
	matrix1.append(row)
for i in range(rows):
	row = list(map(int, input().split()))
	matrix2.append(row)	
matrix3 = []	
for j in range(rows):
	row1 = []
	for k in range(cols):
		row1.append(matrix1[j][k] + matrix2[j][k])
	matrix3.append(row1)		
print(matrix3)		
		
