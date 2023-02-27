def max_heapify (vet, raiz, tamanho):
    maior = raiz

    filho_esq = 2*raiz+1
    
    if filho_esq < tamanho and vet[filho_esq] > vet[maior]:
        maior = filho_esq
    
    filho_dir = 2*raiz+2
    if filho_dir < tamanho and vet[filho_dir] > vet[maior]:
        maior = filho_dir

    if maior != raiz:
        temp = vet[maior]

        vet[maior] = vet[raiz]
        vet[raiz] = temp
        max_heapify(vet, maior, tamanho)


vet = eval(input())

while vet != []:

    max_heapify(vet,0,len(vet))
    print(vet)
    vet = eval(input())
