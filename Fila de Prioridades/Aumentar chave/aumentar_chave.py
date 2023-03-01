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

def acha_pai (pos):
    pai = (pos-1)//2

    if pai < 0:
        return
    else:
        return pai

def aumentar_chave (heap,pos,novo):
    
    if pos >= len(heap):
        heap.append(novo)
    else:
        heap[pos] = novo
    
    while pos > 0 and heap[acha_pai(pos)] > novo:
        heap[acha_pai(pos)], heap[pos] = heap[pos], heap[acha_pai(pos)]
        pos = acha_pai(pos)
    
    return heap

heap = eval(input())
pos = eval(input())
novo = eval(input())


while heap != []:

    heap = aumentar_chave(heap,pos,novo)
    print(heap)

    heap = eval(input())
    if heap == []:
        break
    pos = eval(input())
    novo = eval(input())    
