def CasaGus (lista):
    return lista[int(len(lista)/2)]

def calculaDistancias (lista, k):
    soma = 0

    for i in lista:
        soma += abs(i - k)
    
    return soma

entrada = eval(input())

while entrada != []:
    entrada.sort()
    casa = CasaGus(entrada)
    distancia = calculaDistancias(entrada, casa)

    print(distancia)
    entrada = eval(input())