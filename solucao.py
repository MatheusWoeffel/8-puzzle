import math
from src.nodo import Nodo
from src.fronteiras import Fronteira, FilaFronteira, PilhaFronteira

PUZZLE_SIZE = 3 # 3x3
PUZZLE_GOAL = '12345678_'

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


def buscar(estado='', f=Fronteira):
  if not issubclass(f, Fronteira):
    raise TypeError('Implementação de fronteira não extende classe base Fronteira')
  
  expandidos = set()
  fronteira = f()
  fronteira.adicionar(Nodo(estado))
  
  while (len(fronteira) > 0):
    v = fronteira.remover()
    if v.estado == PUZZLE_GOAL:
      return v.tracar_caminho()
    if v.estado not in expandidos:
      expandidos.add(v.estado)
      for nodo in expande(v):
        fronteira.adicionar(nodo)
  
  return None

  
def bfs(estado=''):
  return buscar(estado, FilaFronteira)

def dfs(estado=''):
  return buscar(estado, PilhaFronteira)

#pai = Nodo('2_3541687')

#print(pai)
#print('-------')
#for nodo in expande(pai):
#    print(nodo)
#print('-------')
#print(bfs('2_3541687'))
#print(bfs('_23156478'))
#print(bfs('2_3541687'))
#print(sucessor('123456_78'))

# ['abaixo', 'abaixo', 'direita', 'direita']
#print(bfs('_23156478'))
# print(dfs('_23156478'))
print(dfs('12345_786'))
print(dfs('1234567_8'))

#print(sucessor('12345_786'))
# Retorna None
#print(bfs('185423_67'))
# print(dfs('185423_67'))
