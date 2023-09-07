import unittest
from src.excitingsoda.models.Series import Series


class TestSeriesModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_series(self):
        # Create Series class instance
        test_model = Series(
            episodes=["repellendus", "temporibus"],
            cast=["quo", "quod"],
            series_name="molestias",
            id="sed",
        )
        self.assertEqual(test_model.episodes, ["repellendus", "temporibus"])
        self.assertEqual(test_model.cast, ["quo", "quod"])
        self.assertEqual(test_model.series_name, "molestias")
        self.assertEqual(test_model.id, "sed")

    def test_series_required_fields_missing(self):
        # Assert Series class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = Series()


if __name__ == "__main__":
    unittest.main()
