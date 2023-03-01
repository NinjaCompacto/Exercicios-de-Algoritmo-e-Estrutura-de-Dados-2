def valorRoda(config, roda): #retorna o valor da configuracao na posicao roda
	return (config // 10 ** (4 - roda)) % 10

def gira(config, roda, sentido): 
	peso = 10 ** (4 - roda)
	
	digitoAtual = valorRoda(config, roda)
	
	if sentido == 'a':
		proximoDigito = (digitoAtual + 9) % 10
	else:
		proximoDigito = (digitoAtual + 1) % 10
	
	subtrair = digitoAtual * peso
	somar = proximoDigito * peso
	
	return config - subtrair + somar

# Retorna 1 quando n existe e 0 quando existe
def naoExisteEm(estado, lista):
	naoExiste = 1
	
	for i in lista:
		naoExiste -= (i == estado.numero)
	
	return naoExiste

def naoExisteEmObj(estado, lista):
	naoExiste = 1
	
	for i in lista:
		naoExiste -= (i.numero == estado.numero)
	
	return naoExiste

def heuristica(config):
	passos = 0
	
	for i in range(4):
		valor = valorRoda(config, i+1)
		if valor <= 5 :
			passos += valor
		else:
			passos += (10 - valor)
	
	return passos

class Estado:
	def __init__(self, numero, proibidos, passos):
		# Guarda a configuração atual e a coleção de
		# estados proibidos
		self.numero = numero
		self.proibidos = proibidos
		
		# Calcule f, g e h
		self.g = passos
		self.h = heuristica(self.numero) # Deve calcular a heurística aqui
		self.f = self.g + self.h # F(x) = g(x) + h(x)
	
	def transicoes(self):
		saida = []
		
		for i in range(4):
			n1 = Estado(gira(self.numero, i+1, 'a'), proibidos, self.g+1)
			if naoExisteEm(n1, self.proibidos) and naoExisteEmObj(n1, heap) and naoExisteEmObj(n1, historico):
				saida.append(n1)
			n1 = Estado(gira(self.numero, i+1, 'h'), proibidos, self.g+1)
			if naoExisteEm(n1, self.proibidos) and naoExisteEmObj(n1, heap) and naoExisteEmObj(n1, historico):
				saida.append(n1)
		
		return saida
	
	def __lt__(self, other):
		if self.f != other.f :
			return self.f < other.f
		return False
	
	def __repr__(self):
		return "{:04d}".format(self.numero)

#########################
#   FUNÇÕES PARA HEAP   #
#########################

def aumentar_chave(heap, pos, novo):
	if pos == len(heap):
		heap.append(novo)
	else :
		heap[pos] = novo
		min_heapfy(heap, pos)
	verifica_pai(heap, pos)

def verifica_pai(lista, i):
	pai = int((i-1)/2)
	
	if pai < 0 :
		return
	elif lista[pai] > lista[i] :
		troca(lista, pai, i)
		verifica_pai(lista, pai)

def min_heapfy(lista, i):
	
	tam = len(lista)
	
	f1 = (2*i) + 1
	f2 = (2*i) + 2
	
	exf1 = False
	exf2 = False
	
	if (f1 < tam) :
		exf1 = (lista[i] > lista[f1])
	
	if (f2 < tam) :
		exf2 = (lista[i] > lista[f2])
	
	if (exf1 and exf2) :
		if (lista[f1].f <= lista[f2].f) :
			troca(lista, f1, i)
			min_heapfy(lista, f1)
		else :
			troca(lista, f2, i)
			min_heapfy(lista, f2)
	elif exf1 :
		troca(lista, f1, i)
		min_heapfy(lista, f1)
	elif exf2 :
		troca(lista, f2, i)
		min_heapfy(lista, f2)

def troca(lista, p1, p2) :
	aux = lista[p1]
	lista[p1] = lista[p2]
	lista[p2] = aux


def remove(heap, pos):
	troca(heap, pos, len(heap)-1)
	heap.pop()
	min_heapfy(heap, pos)

##########################
########   MAIN   ########
##########################

inicial = int(input())

while inicial != -1 :
	proibidos = eval(input())
	
	heap = []
	historico = []
	
	heap.append(Estado(inicial, proibidos, 0))
	
	aux = heap[0]
	
	while(heap[0].numero != 0) :
		
		historico.append(heap[0])
		remove(heap, 0)
		
		novos = aux.transicoes()
		
		for i in novos:
			aumentar_chave(heap, len(heap), i)
		
		aux = heap[0]
	
	print(heap[0].f)
	
	inicial = int(input())