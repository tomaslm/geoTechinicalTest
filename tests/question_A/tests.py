import unittest
from chalenge import question_A


class TestLines(unittest.TestCase):
    def test_overlapping_lines_1(self):
        line_1 = (1, 5)
        line_2 = (2, 6)
        return self.assertTrue(question_A.check_line_overlap(line_1, line_2))

    def test_overlapping_lines_2(self):
        line_1 = (0, 100)
        line_2 = (50, 51)
        return self.assertTrue(question_A.check_line_overlap(line_1, line_2))

    def test_overlapping_lines_3(self):
        line_1 = (50, 51)
        line_2 = (0, 100)
        return self.assertTrue(question_A.check_line_overlap(line_1, line_2))

    def test_overlapping_lines_3(self):
        line_1 = (0, 100)
        line_2 = (100, 101)
        return self.assertTrue(question_A.check_line_overlap(line_1, line_2))

    def test_overlapping_lines_4(self):
        line_1 = (0, 100)
        line_2 = (-10, 0)
        return self.assertTrue(question_A.check_line_overlap(line_1, line_2))

    def test_non_overlapping_lines_1(self):
        line_1 = (1, 5)
        line_2 = (6, 8)
        return self.assertFalse(question_A.check_line_overlap(line_1, line_2))

    def test_non_overlapping_lines_2(self):
        line_1 = (0, 10)
        line_2 = (11, 20)
        return self.assertFalse(question_A.check_line_overlap(line_1, line_2))

    def test_non_overlapping_lines_3(self):
        line_1 = (-15, -10)
        line_2 = (-9, 10)
        return self.assertFalse(question_A.check_line_overlap(line_1, line_2))

    def test_non_overlapping_lines_4(self):
        line_1 = (-15, -10)
        line_2 = (5, 10)
        return self.assertFalse(question_A.check_line_overlap(line_1, line_2))

