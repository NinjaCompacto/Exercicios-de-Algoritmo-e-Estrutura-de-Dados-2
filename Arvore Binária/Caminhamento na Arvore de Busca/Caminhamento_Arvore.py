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

def preOrder(arvore):
    print(arvore['valor'], end=' ')

    if arvore['esq'] is not None:
        preOrder(arvore['esq'])
    if arvore['dir'] is not None:
        preOrder(arvore['dir'])

def inOrder(arvore):
    if arvore['esq'] is not None:
        inOrder(arvore['esq'])

    print(arvore['valor'], end=' ')

    if arvore['dir'] is not None:
        inOrder(arvore['dir'])

def posOrder(arvore):
    if arvore['esq'] is not None:
        posOrder(arvore['esq'])

    if arvore['dir'] is not None:
        posOrder(arvore['dir'])

    print(arvore['valor'],end=' ')

# Lê o primeiro caso de teste
caso = eval(input())
num_arvores = 1

# Itera até o último caso
while caso != []:
    print("Arvore", num_arvores )
    # complete o código aqui
    
    #cria a arvore vaiza
    arvore = cria_arvore()

    #percorre a entrada e insere os valores na arvore na ordem de entrada da lista
    for i in caso:
        arvore = insere(arvore, i)
    
    print('Pre-ordem:', end=' ')
    preOrder(arvore)
    print()
    print('In-ordem:', end=' ')
    inOrder(arvore)
    print()
    print('Pos-ordem:', end=' ')
    posOrder(arvore)
    print()
    print()

    
    #conta o numero de arvores impressas    
    num_arvores += 1

    # Lê o próximo caso de teste
    caso = eval(input())
