from nodo import Nodo
import unittest

OBJETIVO="12345678_"

def distancia_de_hamming(estado):
    lista_de_pecas_estado = [*estado]
    lista_de_pecas_objetivo = [*OBJETIVO]

    distance = 0
    for (peca, peca_objetivo) in zip(lista_de_pecas_estado, lista_de_pecas_objetivo):
        if peca != peca_objetivo and peca != "_":
            distance += 1
    return distance

class TestesDeHeuristica(unittest.TestCase):
    def test_1(self):
        self.assertEqual(distancia_de_hamming('1234567_8'), 1)

    def test_moodle(self):
        self.assertEqual(distancia_de_hamming('5_4732816'), 8)

    def test_none(self):
        self.assertEqual(distancia_de_hamming('12345678_'), 0)
   

if __name__ == "__main__":
    unittest.main()

