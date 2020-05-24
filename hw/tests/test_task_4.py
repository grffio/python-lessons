import unittest
from task_4 import masquerade


class TestMasquerade(unittest.TestCase):
    """Tests for Task 4"""

    def test_ok(self):
        """Test that it can return masqueraded value except for the 2 first and 2 last symbol."""
        input_value = "123qwerty56"
        want = "12*******56"
        result = masquerade(input_value)
        self.assertEqual(result, want)

    def test_ok_num(self):
        """Test that it can return not masqueraded value."""
        input_value = "123456"
        want = "123456"
        result = masquerade(input_value)
        self.assertEqual(result, want)

    def test_ok_min(self):
        """Test that it can return masqueraded value except for the first and last symbol."""
        input_value = "12qw"
        want = "1**w"
        result = masquerade(input_value)
        self.assertEqual(result, want)

    def test_err_type(self):
        """Test that it can return 'None' if use invalid data type."""
        input_value = 123
        want = None
        result = masquerade(input_value)
        self.assertEqual(result, want)


if __name__ == '__main__':
    unittest.main()
