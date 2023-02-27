def busca_binaria(lis, chave):
    """Busca binária em uma lista.

    Parâmetros:
    lista:  Um objeto da classe list ou outra coleção que permita
            indexação posicional (por índices).
    chave:  Chave a ser pesquisada na lista. Deve ter tipo que
            permita comparação pelos operadores == e < com os
            elementos da lista.

    Retorno: a função retorna o índice do elemento que possui a
            chave buscada ou -1 se esse elemento não existir na lista.
    """
    elementos_verificados = 0
    ini = 0
    fim = len(lis) - 1
    
    while ini <= fim:
        meio = (ini + fim) // 2

        if lis[meio] == chave:
            return meio

        if lis[meio] < chave:
            elementos_verificados +=1 
            ini = meio + 1
        else:
            elementos_verificados +=1 
            fim = meio - 1
    print(elementos_verificados+1)
    return -1

lista = eval(input())

busca_binaria(lista,-12321321312312)