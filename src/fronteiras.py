from collections import deque
import heapq

class Fronteira:
  def adicionar(nodo=None):
    raise NotImplementedError('Método não implementado')
  
  def remover(): 
    raise NotImplementedError('Método não implementado')
  
  def __len__(self):
    raise NotImplementedError('Método não implementado')
 
  
class FilaFronteira(Fronteira):
  def __init__(self):
    self._fronteira = deque([])
    
  def adicionar(self, nodo=None):
    self._fronteira.append(nodo)
    
  def remover(self):
    return self._fronteira.popleft()
  
  def __len__(self):
    return len(self._fronteira)


class PilhaFronteira(Fronteira):
  def __init__(self):
    self._fronteira = []
    
  def adicionar(self, nodo=None):
    self._fronteira.append(nodo)
    
  def remover(self):
    return self._fronteira.pop()
  
  def __len__(self):
    return len(self._fronteira)

class HeapFronteira(Fronteira):
  def __init__(self, calcula_heuristica):
    self.heap = []
    self.calcula_heuristica = calcula_heuristica

  def adicionar(self, nodo=None):
    heapq.heappush(self.heap, (nodo.custo + self.calcula_heuristica(nodo.estado),nodo))

  def remover(self):
    return heapq.heappop(self.heap)[1]

  def __len__(self):
    return len(self.heap)