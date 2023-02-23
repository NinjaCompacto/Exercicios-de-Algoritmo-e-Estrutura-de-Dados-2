class Competidor:
    def __init__(self,nome,nota,cod):
        self.nome = nome
        self.nota = nota
        self.cod = cod        
        
    
    def __lt__ (self,outro):
            return outro.nota < self.nota

numero_participantes = eval(input())

placar = []

for i in range(numero_participantes):
    entrada = eval(input())
    lista_notas = [entrada[1],entrada[2],entrada[3]]
    lista_notas.sort()
    nota = lista_notas[1] + lista_notas[2]
    placar.append(Competidor(entrada[0],nota,i))
    

placar.sort()

for i in range(numero_participantes):
    print(placar[i].nome +': '  + str(placar[i].nota) )
