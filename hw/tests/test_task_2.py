import unittest
from task_2 import pop_div2


class TestPopDivBy2(unittest.TestCase):
    """Tests for Task 2"""

    def test_ok(self):
        """Test that it can return the list without numbers, divisible by 2."""
        input_value = [1, 2, 3, 4, -1, 1.22, 0, None, 'test', True, (1, 2, 3), {'a': 1, 'b': 2}]
        want = [1, 3, -1, 1.22, None, 'test', True, (1, 2, 3), {'a': 1, 'b': 2}]
        result = pop_div2(input_value)
        self.assertEqual(result, want)

    def test_err_type(self):
        """Test that it can return 'None' if use invalid data type."""
        input_value = 123
        want = None
        result = pop_div2(input_value)
        self.assertEqual(result, want)


if __name__ == '__main__':
    unittest.main()
