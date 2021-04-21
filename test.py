import unittest
from horsepad import HorsePad
import reachability


class DefaultHpTest(unittest.TestCase):
    pad = HorsePad()

    def test_zero(self):
        self.assertEqual(self.pad.is_within((0, 0)), True)

    def test_oob(self):
        self.assertEqual(self.pad.is_within((-1, -1)), False)
        self.assertEqual(self.pad.is_within((0, 4)), False)

    def test_blocked(self):
        self.assertEqual(self.pad.is_within((0, 3)), False)

    def test_moves(self):
        self.assert_(self.pad.move((0, 0)))
        self.assertEqual(self.pad.loc(), (0, 0))
        self.assertNotEqual(self.pad.loc(), (1, 1))
        self.assert_(self.pad.move((1, 1)))
        self.assertEqual(self.pad.loc(), (1, 1))
        self.assert_(not self.pad.move((5, 5)))
        self.assertEqual(self.pad.loc(), (1, 1))

# TODO non-default HPs


if __name__ == '__main__':
    unittest.main()
