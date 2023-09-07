from urllib.parse import quote
from .base import BaseService
from ..models.GetSeriesResponse import GetSeriesResponse as GetSeriesResponseModel
from ..models.Series import Series as SeriesModel


class Series(BaseService):
    def get_series(self) -> GetSeriesResponseModel:
        """
        Get a list of series
        """

        url_endpoint = "/series"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, list):
            return [SeriesModel(**model) for model in res]
        return res

    def get_series_by_id(self, id: str) -> SeriesModel:
        """
        Get a series by id
        Parameters:
        ----------
            id: str
        """

        url_endpoint = "/series/{id}"
        headers = {}
        self._add_required_headers(headers)
        if not id:
            raise ValueError("Parameter id is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace("{id}", quote(str(id)))
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return SeriesModel(**res)
        return res
