import unittest
from src.excitingsoda.models.Series import Series


class TestSeriesModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_series(self):
        # Create Series class instance
        test_model = Series(
            episodes=["molestias", "nemo"],
            cast=["animi", "ut"],
            series_name="exercitationem",
            id="error",
        )
        self.assertEqual(test_model.episodes, ["molestias", "nemo"])
        self.assertEqual(test_model.cast, ["animi", "ut"])
        self.assertEqual(test_model.series_name, "exercitationem")
        self.assertEqual(test_model.id, "error")

    def test_series_required_fields_missing(self):
        # Assert Series class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = Series()


if __name__ == "__main__":
    unittest.main()
