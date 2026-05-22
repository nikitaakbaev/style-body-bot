import unittest

from services.body_type_detector import BODY_TYPE_TITLES, detect_body_type
from services.recommendations import RECOMMENDATIONS, format_result_text


class RecommendationsTestCase(unittest.TestCase):
    def test_recommendations_exist_for_all_body_types(self) -> None:
        self.assertEqual(set(RECOMMENDATIONS), set(BODY_TYPE_TITLES))

        for body_type, recommendation in RECOMMENDATIONS.items():
            with self.subTest(body_type=body_type):
                self.assertTrue(recommendation["goal"])
                self.assertTrue(recommendation["suitable"])
                self.assertTrue(recommendation["avoid"])

    def test_format_result_text_contains_required_sections(self) -> None:
        detection = detect_body_type(bust=90, waist=65, hips=105)
        text = format_result_text(detection)

        self.assertIn("Ваш примерный тип фигуры: Груша", text)
        self.assertIn("Почему:", text)
        self.assertIn("Главная задача в одежде:", text)
        self.assertIn("Что будет смотреться выигрышно:", text)
        self.assertIn("Чего лучше избегать:", text)


if __name__ == "__main__":
    unittest.main()
