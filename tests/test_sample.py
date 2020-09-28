import unittest
# from unittest import TestCase


class TestSample(unittest.TestCase):
    def setUp(self):
        self.initial = []
        return super().setUp()

    def test_list(self):
        foo = (2, 3)
        self.initial.append(foo)
        self.assertNotEqual(self.initial, [], 'both lists should be unequal')

    def tearDown(self):
        self.initial = None
        return super().tearDown()


if __name__ == '__main__':
    unittest.main()