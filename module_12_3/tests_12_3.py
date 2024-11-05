import module_12_3 as m
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner = m.Runner('Nick', 10)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """Метод проверяет корректность выполнения Runner.run()
        Пропускается в зависимости от значения is_frozen"""
        self.runner.run()
        self.assertEqual(self.runner.distance, self.runner.speed * 2)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """Метод проверяет корректность выполнения Runner.walk()
        Пропускается в зависимости от значения is_frozen"""
        self.runner.walk()
        self.assertEqual(self.runner.distance, self.runner.speed)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        """Метод проверяет корректность выполнения Runner.challenge()
        Пропускается в зависимости от значения is_frozen"""
        self.runner.challenge()
        self.assertEqual(self.runner.distance, self.runner.speed * 2 + self.runner.speed)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        """Метод, где создаётся атрибут класса all_results.
        Это словарь в который будут сохраняться результаты всех тестов"""
        cls.all_result = {}

    def setUp(self):
        """Метод, где создаются 3 объекта:"""
        self.runner1 = m.Runner('Усэйн', 10)
        self.runner2 = m.Runner('Андрей', 9)
        self.runner3 = m.Runner('Ник', 3)

    def tearDown(self):
        """Метод, где выводятся all_results по очереди в столбец"""
        print(self.all_result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run1(self):
        """ Метод тестирования забегов"""
        tournament = m.Tournament(90, self.runner1, self.runner3)
        result = tournament.start()
        for key, value in result.items():
            self.all_result[key] = value.name
        self.assertTrue(self.all_result[max(self.all_result.keys())] == self.runner3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run2(self):
        """ Метод тестирования забегов"""
        tournament = m.Tournament(90, self.runner2, self.runner3)
        result = tournament.start()
        for key, value in result.items():
            self.all_result[key] = value.name
        self.assertTrue(self.all_result[max(self.all_result.keys())] == self.runner3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run3(self):
        """ Метод тестирования забегов"""
        tournament = m.Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tournament.start()
        for key, value in result.items():
            self.all_result[key] = value.name
        self.assertTrue(self.all_result[max(self.all_result.keys())] == self.runner3)


if __name__ == '__main__':
    unittest.main()
