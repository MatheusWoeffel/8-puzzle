import math
from src.fronteiras import Fronteira, FilaFronteira, HeapFronteira, PilhaFronteira
from src.heuristicas import distancia_de_hamming, distancia_de_manhattan


PUZZLE_SIZE = 3 # 3x3
PUZZLE_GOAL = '12345678_'


class Nodo:
  def __init__(self, estado='', pai=None, acao=None, heuristica=None):
    self.estado = estado
    self.pai = pai
    self.acao = acao
    self.custo = 0 if pai == None else pai.custo + 1
      
      
  def tracar_caminho(self):
    node = self
    caminho = []
    while (node.pai != None):
      caminho.append(node.acao)
      node = node.pai
    return caminho[::-1]
  
  
  def __str__(self):
    string = 'Nodo:'
    string += '\n  estado = ' + self.estado
    string += '\n  acao = ' + str(self.acao)
    string += '\n  custo = ' + str(self.custo)
    return string
  

  # When the priority(heuristic in this case) is equal heapq uses the Node object for comparison
  # So we always return the left side of the assignment as we don't care in this case
  # For more info see: https://stackoverflow.com/questions/53554199/heapq-push-typeerror-not-supported-between-instances
  def __lt__(self, other):
    return True


# Dado o estado atual, o indice do vazio e o novo indice que o vazio irá ocupar,
# retorna a string correspondente ao novo estado
def gerar_estado(estado_atual, vazio_index, novo_index):
    char = estado_atual[novo_index]
    novo_estado = estado_atual[:novo_index] + '_' + estado_atual[novo_index+1:]
    novo_estado = novo_estado[:vazio_index] + char + novo_estado[vazio_index+1:]
    return novo_estado


def sucessor(estado=''):
  vazio_index = estado.index('_')
  vazio_x = vazio_index % PUZZLE_SIZE
  vazio_y = math.floor(vazio_index / PUZZLE_SIZE)
  
  movimentos = []
  if (vazio_y > 0): # can go up
    movimentos.append(('acima', gerar_estado(estado, vazio_index, vazio_index - 3)))
  
  if (vazio_y < 2): # can go down
    movimentos.append(('abaixo', gerar_estado(estado, vazio_index, vazio_index + 3)))
      
  if (vazio_x > 0): # can go left
    movimentos.append(('esquerda', gerar_estado(estado, vazio_index, vazio_index - 1)))
      
  if (vazio_x < 2): # can go right
    movimentos.append(('direita', gerar_estado(estado, vazio_index, vazio_index + 1)))
  
  return movimentos


def expande(pai = None):
  if pai == None or not isinstance(pai, Nodo):
    return []
  
  return [Nodo(sucessor[1], pai, sucessor[0]) for sucessor in sucessor(pai.estado)]


# Implementação do pseudo-código de busca. Dado um estado inicial e uma estrutura
# de dados que implemente a interface de "Fronteira", retorna uma tupla contendo
# os movimentos necessários para alcançar o objetivo (por padrão: 12345678_) e
# o número de estados expandidos. Caso não houver solução é retornado None.
def buscar(estado='', fronteira=Fronteira):
  if not issubclass(type(fronteira), Fronteira):
    raise TypeError('Implementação de fronteira não extende classe base Fronteira')
  
  expandidos = set()
  fronteira.adicionar(Nodo(estado))
  
  while (len(fronteira) > 0):
    v = fronteira.remover()
    if v.estado == PUZZLE_GOAL:
      return (v.tracar_caminho(), len(expandidos))
    if v.estado not in expandidos:
      expandidos.add(v.estado)
      for nodo in expande(v):
        fronteira.adicionar(nodo)
  
  return (None, len(expandidos))

  
def bfs(estado=''):
  return buscar(estado, FilaFronteira())[0]


def dfs(estado=''):
  return buscar(estado, PilhaFronteira())[0]


def astar_hamming(estado=''):
  return buscar(estado, HeapFronteira(distancia_de_hamming))[0]


def astar_manhattan(estado=''):
  return buscar(estado, HeapFronteira(distancia_de_manhattan))[0]

