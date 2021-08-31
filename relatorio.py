import time
from solucao import buscar
from src.fronteiras import Fronteira, FilaFronteira, PilhaFronteira, HeapFronteira
from src.heuristicas import distancia_de_hamming, distancia_de_manhattan

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
  gerar_relatorio('2_3541687')