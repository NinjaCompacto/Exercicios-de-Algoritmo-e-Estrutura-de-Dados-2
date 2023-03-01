def quicksort (vet, inicio, fim):

    if inicio > fim:
        return None
    
    i = inicio
    j = fim
    pivor = vet[inicio]

    while i < j:

        while i < j and vet[j] > pivor:
            j -= 1

        if i < j:
            vet[i] = vet[j]
            i += 1
        
        while i < j and vet[i] <= pivor:
            i += 1
        
        if i < j:
            vet[j] = vet[i]
            j -= 1
        
        vet[i] = pivor
    
    quicksort(vet,inicio,i-1)
    quicksort(vet,i+1,fim)


entrada = eval(input())

while entrada != []:

    quicksort(entrada,0,len(entrada)-1)
    print(entrada)

    entrada = eval(input())