import unittest
from not_repeating import first_not_repeating


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual("c", first_not_repeating("abacabad"))

    def test_2(self):
        self.assertEqual("_", first_not_repeating("abacabaabacaba"))

    def test_3(self):
        self.assertEqual("_", first_not_repeating(""))


if __name__ == "__main__":
    unittest.main()
