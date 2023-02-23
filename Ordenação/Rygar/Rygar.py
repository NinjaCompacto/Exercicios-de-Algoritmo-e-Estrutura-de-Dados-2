from math import ceil
class Monstro:
    def __init__(self, energia,forca):
        self.forca = forca
        self.energia = energia
        self.eficiencia_morte = (ceil(energia/40)-1)*forca
                
        
    def __lt__ (self, outro):
        return self.eficiencia_morte < outro.eficiencia_morte


entrada = eval(input())
list_monstros = []

monstros_derrotados = 0
energia_guerreiro = 100

for item in entrada:
    list_monstros.append(Monstro(item[0],item[1]))

list_monstros.sort()

for i in list_monstros:
    energia_guerreiro = energia_guerreiro - i.eficiencia_morte
    if energia_guerreiro > 0:
        monstros_derrotados += 1
    else:
        energia_guerreiro = 0
        break
    
print("{} {}".format(monstros_derrotados,energia_guerreiro))