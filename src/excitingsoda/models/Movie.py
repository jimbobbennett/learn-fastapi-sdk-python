from .base import BaseModel
from typing import List


class Movie(BaseModel):
    def __init__(self, cast: List[str], movie_name: str, id: str, **kwargs):
        """
        Initialize Movie
        Parameters:
        ----------
            cast: list of MovieCast
            movie_name: str
            id: str
        """
        self.cast = cast
        self.movie_name = movie_name
        self.id = id
