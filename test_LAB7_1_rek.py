import unittest
from LAB7_1_rek import process_matrix

a = [
    [79, 34, 28, 67, 32, 49],
    [72, 69, 29, 50, 86, 73],
    [65, 42, 25, 23, 59, 44],
    [58, 53, 17, 77, 90, 69],
    [40, 72, 46, 69, 60, 72],
    [29, 76, 89, 89, 76, 53],
    [26, 35, 83, 53, 23, 43],
    [25, 20, 51, 53, 83, 44]
]


class TestProcessingMatrix(unittest.TestCase):
    def test_process_matrix(self):
        matrix, count, total_sum = process_matrix(a, 8, 6)
        self.assertEqual(total_sum, 2062)  # add assertion here


if __name__ == '__main__':
    unittest.main()
