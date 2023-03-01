class Dupla:
    def __init__(self,peso,valor):
        self.peso = peso
        self.valor = valor
    
    def __lt__ (self,outro):
        
        if self.peso != outro.peso:
            return self.peso < outro.peso
        else:
            return False
        
    def __str__ (self):
        return str(self.valor)


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
    
    if pos >= len(heap)-1:
        heap.append(novo)
    else:
        heap[pos] = novo
    
    while pos > 0 and heap[acha_pai(pos)] > novo:
        heap[acha_pai(pos)], heap[pos] = heap[pos], heap[acha_pai(pos)]
        pos = acha_pai(pos)
    
    return heap


entrada = eval(input())
lista = []

while entrada != ():

    dupla = Dupla(entrada[0],str(entrada[1]))

    lista = aumentar_chave(lista, len(lista), dupla)

    entrada = eval(input())


for i in lista:
    print(i)