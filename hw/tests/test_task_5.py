import unittest
from task_5 import swap_dict


class TestSwapDict(unittest.TestCase):
    """Tests for Task 5"""

    def test_ok(self):
        """Test that it can return swapped key and values in a dictionary."""
        input_value = {'a': 1, 'b': 2, '9': 'c', 3: 5}
        want = {1: 'a', 2: 'b', 'c': '9', 5: 3}
        result = swap_dict(input_value)
        self.assertEqual(result, want)

    def test_err_type(self):
        """Test that it can return 'None' if use invalid data type."""
        input_value = "data"
        want = None
        result = swap_dict(input_value)
        self.assertEqual(result, want)


if __name__ == '__main__':
    unittest.main()
