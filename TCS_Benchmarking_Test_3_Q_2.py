#TCS_Benchmarking_T_3_Q_2

#input_handling
arr1 = list(map(int, input().split()))
N = arr1[0]
k = arr1[1]
#main_logic
counter = 0
for i in range(1, N + 1):
	if N % i == 0:
		counter += 1
		if counter == k:
			print(i)
#edge_case_handling			
if k > counter:
	print(1)
