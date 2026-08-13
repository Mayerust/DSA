
# TCS NQT Python I/O


# Single integer
n = int(input())

# Single string
s = input()

# Multiple integers
n, k = map(int, input().split())

# Integer array
arr = list(map(int, input().split()))

# String array
words = input().split()

# Array, one integer per line
n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = int(input())

# Multiple test cases
t = int(input())
for _ in range(t):
    # input for one test case
    pass

# 2D matrix, rows given separately
rows, cols = map(int, input().split())
matrix = []

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Character grid
grid = []
for i in range(rows):
    grid.append(list(input()))

# Comma-separated integers
arr = list(map(int, input().split(',')))

# [1,2,3,4] style input
s = input().strip('[]')
arr = list(map(int, s.split(',')))

# Space-separated output
print(*arr)

# Bracket output
print("[" + ",".join(map(str, arr)) + "]")

# Decimal formatting
print(f"{num:.3f}")

# Fraction input
f1, f2 = input().split()
a, b = map(int, f1.split('/'))
c, d = map(int, f2.split('/'))

# No newline
print(x, end="")
