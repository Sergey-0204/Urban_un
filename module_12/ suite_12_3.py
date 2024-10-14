import unittest

# Определяем класс RunnerTest
class RunnerTest(unittest.TestCase):
    def test_challenge(self):
        self.assertEqual(1 + 1, 2)

    def test_run(self):
        self.assertEqual(1 + 2, 3)

    def test_walk(self):
        self.assertEqual(1 + 3, 4)


# Определяем класс TournamentTest
class TournamentTest(unittest.TestCase):
    def test_first_tournament(self):
        self.assertEqual(2 * 2, 4)

    def test_second_tournament(self):
        self.assertEqual(3 * 3, 9)

    def test_third_tournament(self):
        self.assertEqual(4 * 4, 16)


# Создание тестового набора
test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(RunnerTest))
test_suite.addTest(unittest.makeSuite(TournamentTest))


# Запуск тестов
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)