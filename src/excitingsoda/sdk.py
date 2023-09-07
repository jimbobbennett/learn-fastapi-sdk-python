"""
Creates a ExcitingSoda class.
Generates the main SDK with all available queries as attributes.

Class:
    ExcitingSoda
"""
from .net.environment import Environment
from .services.movie import Movie
from .services.series import Series


class ExcitingSoda:
    """
    A class representing the full ExcitingSoda SDK

    Attributes
    ----------
    movie : Movie
    series : Series

    Methods
    -------
    set_url(url: str)
        Sets the end URL
    set_bearer_token(bearer_token)
        Set the bearer token
    """

    def __init__(self, bearer_token="", environment=Environment.DEFAULT) -> None:
        """
        Initializes the ExcitingSoda SDK class.
        Parameters
        ----------
        environment: str
            The environment that the SDK is accessing
        bearer_token : str
            The bearer token
        """
        self.movie = Movie(bearer_token)
        self.series = Series(bearer_token)

        self.set_url(environment.value)

    def set_url(self, url: str) -> None:
        """
        Sets the end URL

        Parameters
        ----------
            url:
                The end URL
        """
        self.movie.set_url(url)
        self.series.set_url(url)

    def set_bearer_token(self, token: str) -> None:
        """
        Sets bearer token key

        Parameters
        ----------
        token: string
            Bearer token value
        """
        self.movie.set_bearer_token(token)
        self.series.set_bearer_token(token)
