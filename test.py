import unittest
from horsepad import HorsePad
import reachability


class MyTestCase(unittest.TestCase):
    def test_default_horsepad_zero(self):
        pad = HorsePad()
        self.assertEqual(pad.is_within((0, 0)), True)

    def test_default_horsepad_oob(self):
        pad = HorsePad()
        self.assertEqual(pad.is_within((-1, -1)), False)
        self.assertEqual(pad.is_within((0, 3)), False)


if __name__ == '__main__':
    unittest.main()
