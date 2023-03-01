def min_heapify (vetor,raiz,tam):
    menor = raiz
    
    esq = 2*raiz+1

    if esq < tam and vetor[esq] < vetor[menor]:
        menor = esq

    dir = 2*raiz+2

    if dir < tam and vetor[dir] < vetor[menor]:
        menor = dir
    
    if menor != raiz:
        vetor[raiz],vetor[menor] = vetor[menor], vetor[raiz]
        return min_heapify(vetor,menor,tam)
    else:
        return vetor


entrada = eval(input())

while entrada != []:
    entrada = min_heapify(entrada,0,len(entrada))

    print(entrada)
    entrada = eval(input())