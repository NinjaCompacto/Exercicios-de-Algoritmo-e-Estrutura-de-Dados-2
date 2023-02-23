class Time:
    def __init__(self,nome,vitorias,empates,derrotas,gol_marcados,gol_recebidos):
        self.nome = nome
        self.vitorias = vitorias
        self.empates = empates
        self.derrotas = derrotas
        
        self.pontos = vitorias*3 + empates
        self.numero_jogos = vitorias + empates + derrotas

        self.gol_marcados = gol_marcados
        self.gol_recebidos = gol_recebidos
        self.saldo_gols = gol_marcados - gol_recebidos

    def __lt__ (self, outro):
        if self.pontos != outro.pontos:
            return self.pontos > outro.pontos
        else:
            if self.vitorias != outro.vitorias:
                return self.vitorias > outro.vitorias
            else:
                if self.saldo_gols != outro.saldo_gols:
                    return self.saldo_gols > outro.saldo_gols
                else:
                    if self.gol_marcados != outro.gol_marcados:
                        return self.gol_marcados > outro.gol_marcados
                    else:
                        if self.numero_jogos != outro.numero_jogos:
                            return self.numero_jogos < outro.numero_jogos
                        else:
                            return  self.nome.lower() < outro.nome.lower()


num_casos = eval(input())
tabela = []

for i in range(num_casos):
    entrada = eval(input())
    tabela.append(Time( entrada[0], entrada[1], entrada[2], entrada[3], entrada[4], entrada[5]))

tabela.sort()

for i in range(num_casos):
    print("{} - {}: {} pontos, {} jogos ({}-{}-{}), d.g. {} ({}-{})".format(
              i+1
            , tabela[i].nome
            , tabela[i].pontos
            , tabela[i].numero_jogos
            , tabela[i].vitorias
            , tabela[i].empates
            , tabela[i].derrotas
            , tabela[i].saldo_gols
            , tabela[i].gol_marcados
            , tabela[i].gol_recebidos
        ))

