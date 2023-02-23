class ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dist = (self.x**2) + (self.y**2)


    def __lt__(self, outro):
        if self.dist != outro.dist:
            return self.dist < outro.dist
        else:
            if self.x != outro.x:
                return self.x < outro.x
            else:
                    return self.y < outro.y



# Leitura da entrada
entrada = eval(input())

# Crie uma lista vazia e insira os objetos da classe ponto nela
pontos = []
for item in entrada:
    pontos.append(ponto(item[0],item[1]))
	# processe...



# Ordene e imprima de acordo com o enunciado
pontos.sort()

for i in range(len(pontos)):
    print(pontos[i].x, pontos[i].y)