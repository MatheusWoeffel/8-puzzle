import unittest
from solucao import astar_hamming, astar_manhattan, astar_manhattan, bfs, dfs

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
    
    
if __name__ == "__main__":
  unittest.main()