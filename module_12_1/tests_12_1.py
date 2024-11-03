import module_12_1 as m
import unittest


class RunnerTest(unittest.TestCase):
    """Класc наследуемый от TestCase из модуля unittest"""

    def test_walk(self):
        """Метод, в котором создаётся объект класса Runner с произвольным именем.
        Вазывается метод walk у этого объекта 10 раз.
        Методом assertEqual сравнивает distance этого объекта со значением 50"""
        runner1 = m.Runner('runner1')
        for _ in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    def test_run(self):
        """Метод, в котором создаётся объект класса Runner с произвольным именем.
        Вызывается метод run у этого объекта 10 раз.
        После чего методом assertEqual сравнивает distance этого объекта со значением 100"""
        runner2 = m.Runner('runner2')
        for _ in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    def test_challenge(self):
        """Метод в котором создаются 2 объекта класса Runner с произвольными именами.
        Далее 10 раз у объектов вызываются методы run и walk.
        Методом assertNotEqual сравнивается неравенство результатов"""
        runner3 = m.Runner('runner3')
        runner4 = m.Runner('runner4')
        for _ in range(10):
            runner3.run()
            runner4.walk()
        self.assertNotEqual(runner3.distance, runner4.distance)


if __name__ == '__main__':
    unittest.main()
