import unittest
import tests_12_3 as m

test = unittest.TestSuite()
test.addTest(unittest.TestLoader().loadTestsFromTestCase(m.RunnerTest))
test.addTest(unittest.TestLoader().loadTestsFromTestCase(m.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test)
