def removedup(lis):
	
	#complete o código
	tam_lis = len(lis)
	lis_dup =[]
	retirados = 0
	
	for i in range(0,tam_lis):
		if i != tam_lis-1:
			if lis[i+1] == lis[i]:
				lis_dup.append(i+1)
				
	for i in range(0,len(lis_dup)):
		lis.pop(lis_dup[i] - retirados)
		retirados += 1
		

	
def bublesort (lis):
	for i in range(len(lis)-1, 0, -1):
		for j in range(i):
			if lis[j] > lis[j+1]:
				temp =  lis[j]
				lis[j] = lis[j+1]
				lis[j+1] = temp


entrada = eval(input())
while entrada != []:
	# complete o código
	
	bublesort(entrada)
	removedup(entrada)
	print(entrada)
	
	entrada = eval(input())
	
