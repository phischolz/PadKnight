import unittest
from horsepad import HorsePad
from reachability import reachability_recursive, reachability_dynamic


class DefaultHpTest(unittest.TestCase):
    pad = HorsePad()

    # is (0,0) correctly identified?
    def test_zero(self):
        self.assertEqual(self.pad.is_within((0, 0)), True)

    # out of bounds
    def test_oob(self):
        self.assertEqual(self.pad.is_within((-1, -1)), False)
        self.assertEqual(self.pad.is_within((0, 4)), False)

    # disabled fields
    def test_blocked(self):
        self.assertEqual(self.pad.is_within((0, 3)), False)

    # move logic
    def test_moves(self):
        self.assertTrue(self.pad.move((0, 0)))
        self.assertEqual(self.pad.loc(), (0, 0))
        self.assertNotEqual(self.pad.loc(), (1, 1))
        self.assertTrue(self.pad.move((1, 1)))
        self.assertEqual(self.pad.loc(), (1, 1))
        self.assertTrue(not self.pad.move((5, 5)))
        self.assertEqual(self.pad.loc(), (1, 1))
        self.pad.move((-1, -1))
        self.assertEqual(self.pad.loc(), (0, 0))

    # reachability at recursion anchor
    def test_reachability_base_case(self):
        pad = HorsePad()
        self.assertEqual(reachability_recursive(pad, 1), 1)
        self.assertEqual(pad.loc(), (0, 0))

    # reachability for symmetric starting points
    def test_reachability_symmetry(self):
        for n in range(8):
            self.assertTrue(reachability_recursive(HorsePad(start_position=(0, 0)), n) ==
                         reachability_recursive(HorsePad(start_position=(0, 2)), n) ==
                         reachability_recursive(HorsePad(start_position=(2, 0)), n) ==
                         reachability_recursive(HorsePad(start_position=(2, 2)), n))

    # reachability for the impossible start
    def test_reachability_core(self):
        self.assertEqual(reachability_recursive(HorsePad(start_position=(1, 1)), 999999), 1)

    # if recursive method is correct, dynamic one must hereby be too
    def test_equality(self):
        for max_step in range(10):
            for start_x in range(4):
                for start_y in range(3):
                    if not (start_x == 3 and (start_y == 0 or start_y == 2)):
                        pad = HorsePad(start_position=(start_x, start_y))
                        self.assertEqual(reachability_recursive(pad, max_step), reachability_dynamic(pad, max_step))


# TODO? non-default HPs


if __name__ == '__main__':
    unittest.main()
