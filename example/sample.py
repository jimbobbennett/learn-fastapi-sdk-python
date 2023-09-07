from os import getenv
from pprint import pprint
from excitingsoda import ExcitingSoda

sdk = ExcitingSoda()

results = sdk.movie.get_movies()

pprint(vars(results))
