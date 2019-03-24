import unittest
from chalenge import question_B


class TestStringVersion(unittest.TestCase):
    def test_same_version(self):
        version_1 = "1.0"
        version_2 = "1.0"
        self.assertEqual(0, question_B.compare_string_version(version_1, version_2))

    def test_simple_greater(self):
        version_1 = "1.1"
        version_2 = "1.0"
        self.assertEqual(1, question_B.compare_string_version(version_1, version_2))

    def test_simple_smaller(self):
        version_1 = "0.9"
        version_2 = "1.0"
        self.assertEqual(-1, question_B.compare_string_version(version_1, version_2))

    def test_with_char(self):
        version_1 = "1.1b"
        version_2 = "1.1a"
        self.assertEqual(1, question_B.compare_string_version(version_1, version_2))

    def test_different_length(self):
        version_1 = "1.1.1"
        version_2 = "1"
        self.assertEqual(1, question_B.compare_string_version(version_1, version_2))

    def test_complex(self):
        version_1 = "1.2-rc3"
        version_2 = "1.2"
        self.assertEqual(1, question_B.compare_string_version(version_1, version_2))

    def test_with_none(self):
        version_1 = "1.2-rc3"
        version_2 = None
        self.assertEqual(1, question_B.compare_string_version(version_1, version_2))

