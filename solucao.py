import math
import time
from src.nodo import Nodo
from src.fronteiras import Fronteira, FilaFronteira, HeapFronteira, PilhaFronteira
from src.heuristicas import distancia_de_hamming, distancia_de_manhattan
import unittest


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


class GraphSearchMethods(unittest.TestCase):
  def test_simple(self):
    self.assertEqual(['direita'], dfs('1234567_8'))
    self.assertEqual(['direita'], bfs('1234567_8'))
    self.assertEqual(['direita'], astar_hamming('1234567_8'))
    self.assertEqual(['direita'], astar_manhattan('1234567_8'))

  def test_no_solution(self):
    self.assertEqual(None, bfs('185423_67'))
    self.assertEqual(None, dfs('185423_67'))
    self.assertEqual(None, astar_hamming('185423_67'))
    self.assertEqual(None, astar_manhattan('185423_67'))

  def test_intermediate_solution_bfs(self):
    self.assertEqual(['abaixo', 'abaixo', 'direita', 'direita'], bfs('_23156478'))
    self.assertEqual(['abaixo', 'abaixo', 'direita', 'direita'], astar_hamming('_23156478'))
    self.assertEqual(['abaixo', 'abaixo', 'direita', 'direita'], astar_manhattan('_23156478'))

  def test_intermediate_solution_dfs(self):
    self.assertEqual(['esquerda', 'esquerda', 'abaixo', 'direita', 'direita', 
    'acima', 'esquerda', 'esquerda', 'abaixo', 'direita', 'direita', 'acima', 
    'esquerda', 'esquerda', 'abaixo', 'direita', 'direita', 'acima', 'esquerda', 
    'esquerda', 'abaixo', 'direita', 'direita', 'acima', 'esquerda', 'esquerda', 
    'abaixo', 'direita', 'direita'], dfs('12345_786'))
    self.assertEqual(['abaixo'], bfs('12345_786'))
    self.assertEqual(['abaixo'], astar_hamming('12345_786'))
    self.assertEqual(['abaixo'], astar_manhattan('12345_786'))
   
    
def avaliar_busca(estado='', fronteira=Fronteira, nome=''):
  inicio = time.time()
  caminho, n_expandidos = buscar(estado,fronteira)
  fim = time.time()
  
  tempo_total = (fim - inicio) * 1000
  
  if (nome == ''):
    nome = type(fronteira).__name__
  
  print('\nResultados para busca ' + nome + ':')
  print(' - Tempo de execucao: ' + str(tempo_total) + ' ms')
  print(' - Numero de nos expandidos: ' + str(n_expandidos))
  print(' - Custo do caminho: ' + str(len(caminho)))
  

def gerar_relatorio(estado=''):
  avaliar_busca(estado, FilaFronteira(), 'BFS')
  avaliar_busca(estado, PilhaFronteira(), 'DFS')
  avaliar_busca(estado, HeapFronteira(distancia_de_hamming), 'A* com Distancia de Hamming')
  avaliar_busca(estado, HeapFronteira(distancia_de_manhattan), 'A* com Distancia de Manhattan')


if __name__ == "__main__":
  #unittest.main()
  gerar_relatorio('2_3541687')

