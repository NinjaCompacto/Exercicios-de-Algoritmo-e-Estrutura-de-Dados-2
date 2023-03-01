def insere(arvore, valor):
   
    #caso Base da recursao
    if arvore is None:
       return  cria_no(valor)
    #caso em que o valor tem que ser inserido a direita da sub arvore
    elif valor > arvore['valor']:
            arvore['dir'] = insere(arvore['dir'], valor)
            
            if arvore['esq'] is not None:
                h_atual = max(arvore['esq']['h'],arvore['dir']['h']) + 1
            else:
                h_atual = 1 + arvore['dir']['h']
            arvore['h'] = h_atual
            
            if calcularFb(arvore)  > 1:
                if calcularFb(arvore['dir']) < 0:
                    arvore['dir'] = rotacaoLL(arvore['dir'])
                return rotacaoRR(arvore)
            elif calcularFb(arvore) < -1:
                if calcularFb(arvore['esq']) > 0:
                    arvore['esq'] = rotacaoRR(arvore['esq'])
                return rotacaoLL(arvore)
            else:
                return arvore
    #caso em que o valor tem qe se inserido a esquerda da sub arvore
    else:
            arvore['esq'] = insere(arvore['esq'], valor)
            arvore = atualizarAltura(arvore)
           
            if calcularFb(arvore)  > 1:
                if calcularFb(arvore['dir']) < 0:
                    arvore['dir'] = rotacaoLL(arvore['dir'])
                return rotacaoRR(arvore)
            elif calcularFb(arvore) < -1:
                if calcularFb(arvore['esq']) > 0:
                    arvore['esq'] = rotacaoRR(arvore['esq'])
                return rotacaoLL(arvore)
            else:
                return arvore

def rotacaoRR (arvore):
    aux1 = arvore
    if arvore['dir'] is not None:
        aux2 = arvore['dir']['esq']
    else:
        aux2 = None
    arvore = aux1['dir']
    arvore['esq'] = aux1
    arvore['esq']['dir'] = aux2
    #Atualiza as alturas dos nos que sofrem alteracao em suas alturas e relacao a arvore
    if arvore is not None:
        if arvore['esq'] is not None:
            arvore['esq']['dir'] = atualizarAltura(arvore['esq']['dir'])
            arvore['esq'] = atualizarAltura(arvore['esq'])
    arvore = atualizarAltura(arvore)
    return arvore  

def rotacaoLL (arvore):
    aux1 = arvore
    if arvore['esq']  is not None:
        aux2 = arvore['esq']['dir']
    else:
        aux2 = None
    arvore = aux1['esq']
    arvore['dir'] = aux1
    arvore['dir']['esq'] = aux2
    #Atualiza as alturas dos nos que sofrem alteracao em suas alturas e relacao a arvore
    if arvore is not None:
        if arvore['dir'] is not None:
            arvore['dir']['esq'] = atualizarAltura(arvore['dir']['esq'])
            arvore['dir'] = atualizarAltura(arvore['dir'])
    arvore = atualizarAltura(arvore)
    return arvore         

#atualiza altura do no passado como parametro
def atualizarAltura (arvore):
    if arvore is not None:
        if arvore['esq'] is not None and arvore['dir'] is not None:
            arvore['h'] =  max(arvore['dir']['h'], arvore['esq']['h']) + 1
        elif arvore['esq'] is not None and arvore['dir'] is None:
            arvore['h'] = arvore['esq']['h'] + 1
        elif arvore['esq'] is None and arvore['dir'] is not None:
            arvore['h'] = arvore['dir']['h'] + 1
        else:
            arvore['h'] = 1
    return arvore

def cria_arvore():
    """Cria uma árvore vazia.
    """
    return None


def cria_no(valor):
    """Cria um novo nó que não contém filhos e possui o valor
    especificado no argumento como chave."""
    return {'valor': valor, 'esq': None, 'dir': None,'h': 1}


def preOrder(arvore):
    if arvore is not None:
        print(arvore['valor'], end=' ')
        preOrder(arvore['esq'])
        preOrder(arvore['dir'])

def posOrder(arvore):
    if arvore is not None:
        posOrder(arvore['esq'])
        posOrder(arvore['dir'])
        print(arvore['valor'],end=' ')

#calcula o fator de balanciamento do no passado como paramentro
def calcularFb (arvore):
    if arvore['esq'] is not None and arvore['dir'] is not None:
        fb = arvore['dir']['h'] - arvore['esq']['h']
    elif arvore['esq'] is not None and arvore['dir'] is None:
        fb = arvore['esq']['h']*(-1)
    elif arvore['esq'] is None and arvore['dir'] is not None:
        fb = arvore['dir']['h']
    else:
        fb = 0
    return fb

entrada = eval(input())
num_arvore = 1

while entrada != []:
    print('Arvore', num_arvore)
    arvore = cria_arvore()

    for i in entrada:
        arvore = insere(arvore,i)
    
   

    #saida exigida
    print('pre:', end=' ')
    preOrder(arvore)
    print()
    print('pos:', end=' ')
    posOrder(arvore)
    print()
    print()


    num_arvore+=1
    entrada = eval(input())

    