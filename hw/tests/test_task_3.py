import unittest
from task_3 import max_num_parser


class TestMaxNumParser(unittest.TestCase):
    """Tests for Task 3"""

    def test_ok_float(self):
        """Test that it can parse the string and return a maximum number in float."""
        input_value = "123;122.5;0.5;0.0;123.5;-111;0"
        want = 123.5
        result = max_num_parser(input_value)
        self.assertEqual(result, want)

    def test_ok_int(self):
        """Test that it can parse the string and return a maximum number in int."""
        input_value = "123;122.5;0.5;0.0;123.5;124;-111;0"
        want = 124
        result = max_num_parser(input_value)
        self.assertEqual(result, want)

    def test_err_item(self):
        """Test that it can return 'None' if use invalid item type."""
        input_value = "1;2;3;0x0;2,2"
        want = None
        result = max_num_parser(input_value)
        self.assertEqual(result, want)

    def test_err_type(self):
        """Test that it can return 'None' if use invalid data type."""
        input_value = [1, 2, 3]
        want = None
        result = max_num_parser(input_value)
        self.assertEqual(result, want)


if __name__ == '__main__':
    unittest.main()
