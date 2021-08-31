import unittest

PUZZLE_GOAL="12345678_"

def distancia_de_hamming(estado):
  lista_de_pecas_estado = [*estado]
  lista_de_pecas_objetivo = [*PUZZLE_GOAL]

  distance = 0
  for (peca, peca_objetivo) in zip(lista_de_pecas_estado, lista_de_pecas_objetivo):
    if peca != peca_objetivo and peca != "_":
      distance += 1
  return distance


def distancia_de_manhattan(estado):
  lista_de_pecas = [*estado]

  i = 0
  distancia_total = 0
  for peca in lista_de_pecas:
    posicao_x = i % 3
    posicao_y = i // 3

    if peca != "_":
      distancia_x = posicao_correta_x(peca) - posicao_x
      distancia_y = posicao_correta_y(peca) - posicao_y
      distancia_total += abs(distancia_x) + abs(distancia_y)
    i += 1
  return distancia_total


def posicao_correta_y(peca):
  numero_peca = int(peca)
  return (numero_peca - 1) // 3


def posicao_correta_x(peca):
  numero_peca = int(peca)
  return (numero_peca - 1) % 3


class TestesDeHeuristica(unittest.TestCase):
  def test_1(self):
    self.assertEqual(distancia_de_hamming('1234567_8'), 1)
    self.assertEqual(distancia_de_manhattan('1234567_8'), 1)

  def test_moodle(self):
    self.assertEqual(distancia_de_hamming('5_4732816'), 8)
    self.assertEqual(distancia_de_manhattan('5_4732816'), 15)

  def test_none(self):
    self.assertEqual(distancia_de_hamming('12345678_'), 0)
    self.assertEqual(distancia_de_manhattan('12345678_'), 0)
   

if __name__ == "__main__":
  unittest.main()

