import unittest
from chalenge import question_A


class TestLines(unittest.TestCase):
    def test_paralel_lines_1(self):
        l1 = ((0, 1), (1, 2))
        l2 = ((0, 1), (1, 2))
        self.assertFalse(question_A.check_line_overlap(l1, l2))
        self.assertFalse(question_A.check_line_overlap(l2, l1))

    def test_paralel_lines_2(self):
        l1 = ((0, 0), (5, 5))
        l2 = ((10, 10), (20, 20))
        self.assertFalse(question_A.check_line_overlap(l1, l2))
        self.assertFalse(question_A.check_line_overlap(l2, l1))

    def test_paralel_lines_3(self):
        l1 = ((4, 8), (2, 4))
        l2 = ((30, 60), (15, 30))
        self.assertFalse(question_A.check_line_overlap(l1, l2))
        self.assertFalse(question_A.check_line_overlap(l2, l1))

    def test_paralel_lines_4(self):
        l1 = ((4, 8), (2, 16))
        l2 = ((30, 60), (15, 120))
        self.assertFalse(question_A.check_line_overlap(l1, l2))
        self.assertFalse(question_A.check_line_overlap(l2, l1))

    def test_paralel_lines_4(self):
        l1 = ((1.5, 4.5), (1.5, 1.5))
        l2 = ((12, 12), (12, 4))
        self.assertFalse(question_A.check_line_overlap(l1, l2))
        self.assertFalse(question_A.check_line_overlap(l2, l1))

    def test_transversal_lines_1(self):
        l1 = ((0, 0), (0, 1))
        l2 = ((0, 0), (1, 1))
        self.assertTrue(question_A.check_line_overlap(l1, l2))
        self.assertTrue(question_A.check_line_overlap(l2, l1))

    def test_perpendicular_lines_1(self):
        l1 = ((0, 0), (0, 1))
        l2 = ((0, 0), (1, 0))
        self.assertTrue(question_A.check_line_overlap(l1, l2))
        self.assertTrue(question_A.check_line_overlap(l2, l1))

