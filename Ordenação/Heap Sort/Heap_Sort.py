def heap_sort (vetor):
    tamanho = len(vetor)
    montar_heap(vetor,tamanho)
    while tamanho > 1:
        vetor[0],vetor[tamanho-1] = vetor[tamanho-1],vetor[0]
        tamanho -= 1
        max_heapify(vetor,0,tamanho)
    
def max_heapify (vetor,raiz,tam):
    maior = raiz

    esq = 2*raiz+1
    if esq < tam and vetor[esq] > vetor[maior]:
        maior = esq

    dir =2*raiz+2
    if dir < tam and vetor[dir] > vetor[maior]:
        maior = dir
    
    if maior != raiz:
        vetor[raiz],vetor[maior] = vetor[maior],vetor[raiz]
        max_heapify(vetor,maior,tam)
    

def montar_heap(vetor,tam):
    last = int((tam/2)-1)
    for i in range(last,-1,-1):
        max_heapify(vetor,i,tam) 


entrada = eval(input())

while entrada != []:

    heap_sort(entrada)
    print(entrada)

    entrada = eval(input())