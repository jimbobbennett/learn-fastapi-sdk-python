from os import getenv
from pprint import pprint
from excitingsoda import ExcitingSoda

sdk = ExcitingSoda()
sdk.set_bearer_token(getenv("EXCITINGSODA_BEARER_TOKEN"))

results = sdk.movie.get_movies()

pprint(vars(results))
