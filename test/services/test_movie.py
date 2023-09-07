import unittest
import responses
from src.excitingsoda.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.excitingsoda.services.movie import Movie


class TestMovie_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_movies(self):
        # Mock the API response
        responses.get("http://na.exciting.soda/movie", json={}, status=200)
        # call the method to test
        test_service = Movie()
        response = test_service.get_movies()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_movies_error_on_non_200(self):
        # Mock the API response
        responses.get("http://na.exciting.soda/movie", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Movie()
            test_service.get_movies()
        responses.reset()

    @responses.activate
    def test_get_movie_by_id(self):
        # Mock the API response
        responses.get("http://na.exciting.soda/movie/5359372754", json={}, status=200)
        # call the method to test
        test_service = Movie()
        response = test_service.get_movie_by_id("5359372754")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_movie_by_id_required_fields_missing(self):
        # Mock the API response
        responses.get("http://na.exciting.soda/movie/8430250089", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Movie()
            test_service.get_movie_by_id()
        responses.reset(),

    @responses.activate
    def test_get_movie_by_id_error_on_non_200(self):
        # Mock the API response
        responses.get("http://na.exciting.soda/movie/8123476034", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Movie()
            test_service.get_movie_by_id("8123476034")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
