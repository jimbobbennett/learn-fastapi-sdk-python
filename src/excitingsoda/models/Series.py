from .base import BaseModel
from typing import List


class Series(BaseModel):
    def __init__(
        self, episodes: List[str], cast: List[str], series_name: str, id: str, **kwargs
    ):
        """
        Initialize Series
        Parameters:
        ----------
            episodes: list of SeriesEpisodes
            cast: list of SeriesCast
            series_name: str
            id: str
        """
        self.episodes = episodes
        self.cast = cast
        self.series_name = series_name
        self.id = id
