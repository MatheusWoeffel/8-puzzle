from collections import deque

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