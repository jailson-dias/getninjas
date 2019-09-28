import unittest
from plateau import Plateau
from rover import Rover, directions, sides

class RoverTest(unittest.TestCase):

    def create(self, plateauSize, roverPosition, roverDirection):
        # Cria o plateau e o rover, e retorna o rover criado
        plateau = Plateau(plateauSize[0], plateauSize[1])
        rover = Rover(roverPosition[0], roverPosition[1], roverDirection, plateau)

        return rover

    def test_rover_create(self):
        rover = self.create((5, 5), (1, 2), "N")

        # Testa se o arquivo do rover está criando ele como era esperado que fosse criado
        self.assertEqual(rover.position[0], 1)
        self.assertEqual(rover.position[1], 2)
        self.assertEqual(directions[rover.direction], "N")

    def test_rover_rotate_left(self):
        rover = self.create((5, 5), (1, 2), "N")

        # Testa a rotação do rover para um ou os dois lados em sequência
        rover.rotate(sides["left"])
        self.assertEqual(directions[rover.direction], "W")
        rover.rotate(sides["left"])
        self.assertEqual(directions[rover.direction], "S")
        rover.rotate(sides["left"])
        rover.rotate(sides["left"])
        self.assertEqual(directions[rover.direction], "N")
        rover.rotate(sides["right"])
        self.assertEqual(directions[rover.direction], "E")
        rover.rotate(sides["right"])
        self.assertEqual(directions[rover.direction], "S")
        rover.rotate(sides["right"])
        rover.rotate(sides["left"])
        self.assertEqual(directions[rover.direction], "S")

    def test_move(self):
        rover = self.create((5, 5), (3, 3), "N")
        rover.move()
        self.assertEqual(rover.position[1], 4)
        rover.move()
        self.assertEqual(rover.position[1], 5)

        # Verifica se está reconhecendo quando o rover sai do plateau
        with self.assertRaises(ValueError) as error:
            rover.move()
        self.assertTrue("Unable to go North" in str(error.exception))

    def test_path_12_N_LMLMLMLMM(self):
        rover = self.create((5, 5), (1, 2), "N")
        rover.runCommands("LMLMLMLMM")

        # Testa se depois da execução de todos os comandos, o rover está na possição que deveria está
        self.assertEqual(rover.position[0], 1)
        self.assertEqual(rover.position[1], 3)
        self.assertEqual(directions[rover.direction], "N")

    def test_path_33_E_MMRMMRMRRM(self):
        rover = self.create((5, 5), (3, 3), "E")
        rover.runCommands("MMRMMRMRRM")

        self.assertEqual(rover.position[0], 5)
        self.assertEqual(rover.position[1], 1)
        self.assertEqual(directions[rover.direction], "E")

if __name__ == '__main__':
    unittest.main()