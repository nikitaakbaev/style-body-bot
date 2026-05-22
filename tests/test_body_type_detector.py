import unittest

from services.body_type_detector import detect_body_type


class BodyTypeDetectorTestCase(unittest.TestCase):
    def test_detects_pear(self) -> None:
        result = detect_body_type(bust=90, waist=65, hips=105)

        self.assertEqual(result["type"], "pear")
        self.assertEqual(result["title"], "Груша")
        self.assertEqual(result["confidence"], "примерно")

    def test_detects_inverted_triangle(self) -> None:
        result = detect_body_type(bust=108, waist=82, hips=94)

        self.assertEqual(result["type"], "inverted_triangle")

    def test_detects_apple(self) -> None:
        result = detect_body_type(bust=96, waist=94, hips=98)

        self.assertEqual(result["type"], "apple")

    def test_detects_rectangle(self) -> None:
        result = detect_body_type(bust=92, waist=84, hips=95)

        self.assertEqual(result["type"], "rectangle")

    def test_detects_hourglass(self) -> None:
        result = detect_body_type(bust=96, waist=68, hips=98)

        self.assertEqual(result["type"], "hourglass")


if __name__ == "__main__":
    unittest.main()
