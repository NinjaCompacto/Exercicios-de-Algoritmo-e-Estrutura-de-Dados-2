def calcula_valor (palavra):
    valor = 0

    for i in range(len(palavra)):

        num = ord(palavra[i])

        if num == 45:
            num = 0
        else:
            num -= 96
        
        valor += num
    
    return valor

def coloca_na_tabela (tabela, num, palavra):
    indice = num%m

    if tabela[indice] is None:
        tabela[indice] = palavra
    
    else:
        aux = (indice+1)%m

        while aux%m != indice:
            if tabela[aux] is None:
                tabela[aux] = palavra
                break
            else:
                aux = (aux+1)%m

    
    return tabela

m = int(input())

tabela = m*[None]

n = int(input())

while n > 0:

    palavra = input()
    tabela = coloca_na_tabela(tabela,calcula_valor(palavra), palavra)
    

    n -= 1

for i in range(0,m):
    if tabela[i] is not None :
        print("%d: %s" % (i, tabela[i]))