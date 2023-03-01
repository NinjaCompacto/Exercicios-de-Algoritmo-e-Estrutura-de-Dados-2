from math import floor

def leComando():
	linha = input()
	return linha[0], int(linha[1:])

def buscar_chave(tabela, m , A, chave):
    indice = floor(m * (chave*A - floor(chave*A)))
    

    if tabela[indice] == chave:
        print("Chave %d encontrada no indice %d" % (chave,indice))
    else:
        isFinded = False
        i = 1
        aux = (indice + (i*i))%m

        while aux != indice:
            if tabela[aux] == chave:
                isFinded = True
                break
            else:
                i += 1
                aux = (indice + (i*i))%m

        if isFinded:
            print("Chave %d encontrada no indice %d" % (chave,aux))
        else:
            print("Chave %d nao esta na tabela" % (chave))


def remove_chave(tabela, m , A, chave):
    indice = floor(m * (chave*A - floor(chave*A)))
    isRemoved = False

    if tabela[indice] == chave:
        tabela[indice] = None
        isRemoved = True
    else:
        i = 1
        aux = (indice + (i*i))%m

        while aux != indice:
            if tabela[aux] == chave:
                tabela[aux] = None
                isRemoved = True
                break
            else:
                i += 1
                aux = (indice + (i*i))%m

    if isRemoved:
        print("Chave %d removida" % (chave))
    else:
        print("Chave %d nao esta na tabela" % (chave))
    
    return tabela

def insere_chave(tabela, m , A, chave):
    indice = floor(m * (chave*A - floor(chave*A)))

    if tabela[indice] is None:
        tabela[indice] = chave
        print("Chave %d inserida no indice %d" % (chave,indice))
    else:
        i = 1
        aux = (indice + (i*i))%m

        while aux != indice:
            if tabela[aux] is None:
                tabela[aux] = chave
                print("Chave %d inserida no indice %d" % (chave,aux))
                break
            else:
                i += 1
                aux = (indice + (i*i))%m
        
    return tabela



m = int(input())
A = float(input())

tabela = m*[None]

comando, chave = leComando()
while comando != "x":
	
    if comando == 'i':
        tabela = insere_chave(tabela, m, A, chave)
    if comando == 'r':
        tabela = remove_chave(tabela, m, A, chave)
    if comando == 'p':
        buscar_chave(tabela, m, A, chave)

    comando, chave = leComando()