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
  
  #When the priority(heuristic in this case) is equal heapq uses the Node object for comparison
  #So we always return the left side of the assignment as we don't care in this case
  #For more info see: https://stackoverflow.com/questions/53554199/heapq-push-typeerror-not-supported-between-instances
  def __lt__(self, other):
    return True