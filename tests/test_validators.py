import unittest

from utils.validators import parse_measurement


class ValidatorsTestCase(unittest.TestCase):
    def test_parse_measurement_accepts_integer(self) -> None:
        self.assertEqual(parse_measurement("90"), 90)

    def test_parse_measurement_accepts_comma_decimal(self) -> None:
        self.assertEqual(parse_measurement("90,5"), 90.5)

    def test_parse_measurement_rejects_text(self) -> None:
        self.assertIsNone(parse_measurement("девяносто"))

    def test_parse_measurement_rejects_too_small_value(self) -> None:
        self.assertIsNone(parse_measurement("39"))

    def test_parse_measurement_rejects_too_large_value(self) -> None:
        self.assertIsNone(parse_measurement("201"))


if __name__ == "__main__":
    unittest.main()
