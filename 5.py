rows, cols = map(int, input().split())
matrix = []
for i in range(rows):
	row = list(map(int, input().split()))
	matrix.append(row)
total = 0
for i in range(rows):
	total += matrix[i][cols - 1 - i]
print(total)	
			
