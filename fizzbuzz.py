import unittest


class FizzBuzzTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_false(self):
        self.assertFalse(False)

    def test_plus(self):
        self.assertEqual(1 + 1, 2)


unittest.main()
