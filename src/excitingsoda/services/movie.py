from urllib.parse import quote
from .base import BaseService
from ..models.GetMoviesResponse import GetMoviesResponse as GetMoviesResponseModel
from ..models.Movie import Movie as MovieModel


class Movie(BaseService):
    def get_movies(self) -> GetMoviesResponseModel:
        """
        Get a list of movies
        """

        url_endpoint = "/movie"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, list):
            return [MovieModel(**model) for model in res]
        return res

    def get_movie_by_id(self, id: str) -> MovieModel:
        """
        Get a movie by id
        Parameters:
        ----------
            id: str
        """

        url_endpoint = "/movie/{id}"
        headers = {}
        self._add_required_headers(headers)
        if not id:
            raise ValueError("Parameter id is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace("{id}", quote(str(id)))
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return MovieModel(**res)
        return res
