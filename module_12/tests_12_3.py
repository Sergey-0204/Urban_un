import unittest

def skip_if_frozen(test_method):
    """Декоратор для пропуска тестов, если is_frozen = True."""
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_method(self, *args, **kwargs)
    return wrapper

# Определяем класс RunnerTest
class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        self.assertEqual(1 + 1, 2)

    @skip_if_frozen
    def test_run(self):
        self.assertEqual(1 + 2, 3)

    @skip_if_frozen
    def test_walk(self):
        self.assertEqual(1 + 3, 4)


# Определяем класс TournamentTest
class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertEqual(2 * 2, 4)

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertEqual(3 * 3, 9)

    @skip_if_frozen
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