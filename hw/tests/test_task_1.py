import unittest
from task_1 import char_counter


class TestCharCounter(unittest.TestCase):
    """Tests for Task 1"""

    def test_ok(self):
        """Test that it can return the dictionary in the correct format."""
        input_value = "test string"
        want = {'t': 3, 'e': 1, 's': 2, ' ': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1}
        result = char_counter(input_value)
        self.assertEqual(result, want)

    def test_err_type(self):
        """Test that it can return 'None' if use invalid data type."""
        input_value = 123
        want = None
        result = char_counter(input_value)
        self.assertEqual(result, want)


if __name__ == '__main__':
    unittest.main()
