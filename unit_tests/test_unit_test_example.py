import unittest
import unit_test_example

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "Thebestpreparationfortomorrowisdoingyourbesttoday."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(unit_test_example.LetterCompiler(testcase), expected)

class TestCompiler2(unittest.TestCase):
    
    def test_two(self):
        testcase = "Abcdefghijklmnoqrstuvwxyz"
        expected = ['b', 'c']
        self.assertEqual(unit_test_example.LetterCompiler(testcase), expected)

# EDGE CASES HERE
    def test_number(self):
        testcase = "bbbca"
        expected = ['b', 'b']
unittest.main(argv = ['first-arg-is-ignored'], exit = False)