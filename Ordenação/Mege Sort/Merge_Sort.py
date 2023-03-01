def merge(lista, lista_temp, inicio, meio, fim):
    fim_esquerda = meio-1
    index = inicio
    tamanho = fim - inicio + 1

    # Intercala os elementos de cada lista de forma ordenada
    while inicio <= fim_esquerda and meio <= fim:
        if lista[inicio] <= lista[meio]:
            lista_temp[index] = lista[inicio]
            inicio += 1
        else:
            lista_temp[index] = lista[meio]
            meio += 1
        
        index += 1
    
    # Coloca os valores que sobraram da sublista esquerda
    while inicio <= fim_esquerda:
        lista_temp[index] = lista[inicio]
        index += 1
        inicio += 1
    
    #coloca os valores que sobraram da sublista direita
    while meio <= fim:
        lista_temp[index] = lista[meio]
        index += 1
        meio += 1
    
    #coloca os valores da lista temporaria na lista 'oficial'
    for i in range(0,tamanho):
        lista[fim] = lista_temp[fim]
        fim -= 1


def sort(lista,lista_temp,inicio,fim):
    if inicio < fim:
        meio = (inicio+fim)//2

        sort(lista, lista_temp, inicio, meio)
        sort(lista, lista_temp, meio+1, fim)
        merge(lista, lista_temp, inicio, meio+1,fim)

entrada = eval(input())

while entrada != []:

    lista_auxi = [0]*len(entrada)
    sort(entrada,lista_auxi,0,len(entrada)-1)
    print(entrada)

    entrada = eval(input())