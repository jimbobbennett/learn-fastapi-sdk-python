import unittest
from src.excitingsoda.models.Movie import Movie


class TestMovieModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_movie(self):
        # Create Movie class instance
        test_model = Movie(cast=["consequuntur", "laborum"], movie_name="ad", id="quia")
        self.assertEqual(test_model.cast, ["consequuntur", "laborum"])
        self.assertEqual(test_model.movie_name, "ad")
        self.assertEqual(test_model.id, "quia")

    def test_movie_required_fields_missing(self):
        # Assert Movie class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = Movie()


if __name__ == "__main__":
    unittest.main()
