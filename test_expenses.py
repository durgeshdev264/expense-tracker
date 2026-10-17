import unittest
from main import validate_amount


class TestValidateAmount(unittest.TestCase):

    def test_valid_amount(self):
        result = validate_amount("25.50")
        self.assertEqual(result, 25.50)


if __name__ == "__main__":
    unittest.main()
    