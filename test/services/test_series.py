import unittest
import responses
from src.excitingsoda.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.excitingsoda.services.series import Series


class TestSeries_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_series(self):
        # Mock the API response
        responses.get("http://na.exciting.soda/series", json={}, status=200)
        # call the method to test
        test_service = Series("testkey")
        response = test_service.get_series()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_series_error_on_non_200(self):
        # Mock the API response
        responses.get("http://na.exciting.soda/series", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Series("testkey")
            test_service.get_series()
        responses.reset()

    @responses.activate
    def test_get_series_by_id(self):
        # Mock the API response
        responses.get("http://na.exciting.soda/series/7089361840", json={}, status=200)
        # call the method to test
        test_service = Series("testkey")
        response = test_service.get_series_by_id("7089361840")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_series_by_id_required_fields_missing(self):
        # Mock the API response
        responses.get("http://na.exciting.soda/series/2003729966", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Series("testkey")
            test_service.get_series_by_id()
        responses.reset(),

    @responses.activate
    def test_get_series_by_id_error_on_non_200(self):
        # Mock the API response
        responses.get("http://na.exciting.soda/series/7726005985", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Series("testkey")
            test_service.get_series_by_id("7726005985")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
