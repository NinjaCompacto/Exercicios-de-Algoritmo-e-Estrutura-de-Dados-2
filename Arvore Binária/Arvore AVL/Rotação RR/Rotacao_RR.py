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

def posOrder(arvore):
    if arvore['esq'] is not None:
        posOrder(arvore['esq'])

    if arvore['dir'] is not None:
        posOrder(arvore['dir'])

    print(arvore['valor'],end=' ')

def rotacaoRR (arvore):
	aux1 = arvore
	aux2 = arvore['dir']['esq']
	arvore = aux1['dir']
	arvore['esq'] = aux1
	arvore['esq']['dir'] = aux2
	return arvore


entrada = eval(input())
num_arvore = 1

while entrada != []:
	arvore = cria_arvore()
	
	for i in entrada:
		arvore = insere(arvore,i)
	
	arvore = rotacaoRR(arvore)
	
	print('Arvore',num_arvore)
	print('pre:',end=' ')
	preOrder(arvore)
	print()
	print('pos:',end=' ')
	posOrder(arvore)
	print()
	print()
	
	num_arvore += 1
	entrada = eval(input())