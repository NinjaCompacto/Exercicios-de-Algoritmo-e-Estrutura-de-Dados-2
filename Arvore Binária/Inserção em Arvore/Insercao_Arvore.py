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


def imprime_arvore(arvore, indent=0):
    """Imprime a árvore na forma de um dicionário indentado."""
    prefixo = ' ' * indent

    print("{ 'valor': ", arvore['valor'], ",", sep='')

    if arvore['esq'] is None:
        print(prefixo, "  'esq': None,", sep='')
    else:
        print(prefixo, "  'esq': ", sep='', end='')
        imprime_arvore(arvore['esq'], indent + 9)

    if arvore['dir'] is None:
        print(prefixo, "  'dir': None,", sep='')
    else:
        print(prefixo, "  'dir': ", sep='', end='')
        imprime_arvore(arvore['dir'], indent + 9)

    print(prefixo, "},", sep='')



# Lê o primeiro caso de teste
caso = eval(input())
num_arvores = 1

# Itera até o último caso
while caso != []:
    print("Arvore ", num_arvores )
    # complete o código aqui
    
    #cria a arvore vaiza
    arvore = cria_arvore()

    #percorre a entrada e insere os valores na arvore na ordem de entrada da lista
    for i in caso:
        arvore = insere(arvore, i)
      

    imprime_arvore(arvore)
    
    #conta o numero de arvores impressas    
    num_arvores += 1

    # Lê o próximo caso de teste
    caso = eval(input())
