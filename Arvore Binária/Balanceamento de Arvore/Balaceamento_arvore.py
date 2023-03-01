def insere(arvore, valor):
   
    #caso Base da recursao
    if arvore is None:
       return  cria_no(valor)
    #caso em que o valor tem que ser inserido a direita da sub arvore
    elif valor > arvore['valor']:
            arvore['dir'] = insere(arvore['dir'], valor)
            return arvore
    #caso em que o valor tem qe se inserido a esquerda da sub arvore
    else:
            arvore['esq'] = insere(arvore['esq'], valor)
            return arvore
                             


def cria_arvore():
    """Cria uma árvore vazia.
    """
    return None


def cria_no(valor):
    """Cria um novo nó que não contém filhos e possui o valor
    especificado no argumento como chave."""
    return {'valor': valor, 'esq': None, 'dir': None}


# Adiciona os elementos da arvore em ordem na lista
def inOrder(arvore, lista):
    if arvore['esq'] is not None:
        inOrder(arvore['esq'],lista)

    lista.append(arvore['valor'])

    if arvore['dir'] is not None:
        inOrder(arvore['dir'],lista)


def preOrder(arvore):
    print(arvore['valor'], end=' ')

    if arvore['esq'] is not None:
        preOrder(arvore['esq'])
    if arvore['dir'] is not None:
        preOrder(arvore['dir'])

def posOrder(arvore):
    if arvore['esq'] is not None:
        posOrder(arvore['esq'])

    if arvore['dir'] is not None:
        posOrder(arvore['dir'])

    print(arvore['valor'],end=' ')


def balanciarArvore(arvore,lista,i,j):
    
    if j >= 0 and i <= len(lista)-1 and i < j :
        tam = j+i

        if tam%2 == 0:
            index_meio = int((tam/2))
        else: 
            index_meio = int((tam-1)/2)

       
        #print('valor i:', i)
        #print('valor j:',j)
        #print('Indexe_meio:',index_meio)
        #print('valor inserido:',lista[index_meio])
        arvore = insere(arvore, lista[index_meio])

        balanciarArvore(arvore,lista,i, index_meio-1 )
        balanciarArvore(arvore,lista, index_meio + 1, j)
    elif j >= 0 and i <= len(lista)-1 and i == j:
        #print('valor i:', i)
        #print('valor j:',j)
        #print('Indexe_meio:',i)
        #print('valor inserido:',lista[i])
        arvore = insere(arvore,lista[i])
    
    return arvore
    


caso = eval(input())
num_arvores = 1

# Cria uma lista vazia para inserção dos elementos em ordem
lista = []
 
#cria a arvore vaiza
arvore = cria_arvore()

#Insere todos os elementos da entrada na arvore inicial
for i in caso:
    arvore = insere(arvore, i)
    
# adiciona elementos em ordem na lista 
inOrder(arvore,lista)

arvore_balanciada = cria_arvore()

arvore_balanciada = balanciarArvore(arvore_balanciada, lista, 0, len(lista)-1)

print('pre:',end=' ')    
preOrder(arvore_balanciada)
print()
print('pos:',end=' ')    
posOrder(arvore_balanciada)

