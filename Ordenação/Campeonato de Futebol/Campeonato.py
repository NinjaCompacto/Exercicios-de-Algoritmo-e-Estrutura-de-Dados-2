class Time:
	def __init__(self,nome):
		self.nome = nome
		self.vitorias = 0
		self.empates = 0
		self.derrotas = 0

		self.pontos = 0
		self.numero_jogos = 0
		
		self.gols_sofridos = 0
		self.gols_marcados = 0
		self.saldo_gols = 0

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
					if self.gols_marcados != outro.gols_marcados:
						return self.gols_marcados > outro.gols_marcados
					else:
						if self.numero_jogos != outro.numero_jogos:
							return self.numero_jogos < outro.numero_jogos
						else:
							return  self.nome.lower() < outro.nome.lower()

#ler os times e retorna a tabela primitiva dos jogos
def ler_times (num_times):
	tabela = []
	while num_times > 0:
		
		nome_time = input()
		tabela.append(Time(nome_time))
		
		num_times -= 1
	return tabela


def ler_jogos (num_jogos,tabela):
	while num_jogos > 0:
		jogo = input()
		tabela = atualizar_dados(jogo,tabela)
		num_jogos -= 1
	return tabela

def atualizar_dados(jogo,tabela):
		nome_time1 = ''
		nome_time2 = ''
		gols_time1 = 0
		gols_time2 = 0
		
		aux1 = jogo.split('#')
		aux2 = aux1[0].split(':')
		nome_time1 = aux2[0]
		gols_time1 = int(aux2[1])
		aux2 = aux1[1].split(':')
		nome_time2 = aux2[0]
		gols_time2 = int(aux2[1])
		
		for time in tabela:
			if time.nome == nome_time1:
				time.numero_jogos += 1
				if gols_time1 > gols_time2:
					time.vitorias += 1
					time.pontos += 3
				elif gols_time1 == gols_time2:
					time.empates += 1
					time.pontos += 1
				else:
					time.derrotas += 1
				time.gols_sofridos += gols_time2
				time.gols_marcados += gols_time1
				time.saldo_gols += (gols_time1 - gols_time2)
			
			if time.nome == nome_time2:
				time.numero_jogos += 1
				if gols_time2 > gols_time1:
					time.vitorias += 1
					time.pontos += 3
				elif gols_time2 == gols_time1:
					time.empates += 1
					time.pontos += 1
				else:
					time.derrotas += 1
				time.gols_sofridos += gols_time1
				time.gols_marcados += gols_time2
				time.saldo_gols += (gols_time2 - gols_time1)
		return tabela

def quicksort (vet, inicio, fim):
	if inicio > fim:
		return None
	i = inicio
	j = fim
	pivor = vet[inicio]
	while i < j:
		while i < j and pivor < vet[j]:
			j -= 1
		if i < j:
			vet[i] = vet[j]
			i += 1
		while i < j and vet[i] < pivor:
			i += 1
		if i < j:
			vet[j] = vet[i]
			j -= 1
		vet[i] = pivor
	quicksort(vet,inicio,i-1)
	quicksort(vet,i+1,fim)

num_campeonatos = eval(input())

while num_campeonatos > 0:
	nome_campeonato = input()
	
	num_times = eval(input())
	tabela = ler_times(num_times)
	
	num_jogos = eval(input())
	tabela = ler_jogos(num_jogos,tabela)
	
	tabela.sort()
	
	print(nome_campeonato)
	for i in range(num_times):
		print("{} - {}: {} pontos, {} jogos ({}-{}-{}), d.g. {} ({}-{})".format(
              i+1
            , tabela[i].nome
            , tabela[i].pontos
            , tabela[i].numero_jogos
            , tabela[i].vitorias
            , tabela[i].empates
            , tabela[i].derrotas
            , tabela[i].saldo_gols
            , tabela[i].gols_marcados
            , tabela[i].gols_sofridos
        ))
	
	
	num_campeonatos -= 1