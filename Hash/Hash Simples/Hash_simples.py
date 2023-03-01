def coloca_na_tabela (tabela, num):
    indice = num%m

    if tabela[indice] is None:
        tabela[indice] = num
    
    else:
        aux = (indice+1)%m

        while aux%m != indice:
            if tabela[aux] is None:
                tabela[aux] = num
                break
            else:
                aux = (aux+1)%m

    
    return tabela

m = int(input())

tabela = m*[None]

n = int(input())

while n > 0:

    num = int(input())
    tabela = coloca_na_tabela(tabela,num)
 
    n -= 1

for i in range(0,m):
    if tabela[i] is not None :
        print("%d: %d" % (i, tabela[i]))