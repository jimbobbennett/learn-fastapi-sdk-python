# ExcitingSoda Services
A list of all services and services methods.
- Services

    - [Movie](#movie)

    - [Series](#series)
- [All Methods](#all-methods)


## Movie

| Method    | Description|
| :-------- | :----------| 
| [get_movies](#get_movies) | Get a list of movies |
| [get_movie_by_id](#get_movie_by_id) | Get a movie by id |


## Series

| Method    | Description|
| :-------- | :----------| 
| [get_series](#get_series) | Get a list of series |
| [get_series_by_id](#get_series_by_id) | Get a series by id |




## All Methods


### **get_movies**
Get a list of movies
- HTTP Method: GET
- Endpoint: /movie

**Parameters**

This method has no parameters.

**Return Type**

[GetMoviesResponse](/src/excitingsoda/models/README.md#getmoviesresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from excitingsoda import ExcitingSoda
sdk = ExcitingSoda()

results = sdk.movie.get_movies()

pprint(vars(results))

```

### **get_movie_by_id**
Get a movie by id
- HTTP Method: GET
- Endpoint: /movie/{id}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| id | str | Required |  |

**Return Type**

[Movie](/src/excitingsoda/models/README.md#movie) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from excitingsoda import ExcitingSoda
sdk = ExcitingSoda()

results = sdk.movie.get_movie_by_id(id = 'id')

pprint(vars(results))

```


### **get_series**
Get a list of series
- HTTP Method: GET
- Endpoint: /series

**Parameters**

This method has no parameters.

**Return Type**

[GetSeriesResponse](/src/excitingsoda/models/README.md#getseriesresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from excitingsoda import ExcitingSoda
sdk = ExcitingSoda()

results = sdk.series.get_series()

pprint(vars(results))

```

### **get_series_by_id**
Get a series by id
- HTTP Method: GET
- Endpoint: /series/{id}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| id | str | Required |  |

**Return Type**

[Series](/src/excitingsoda/models/README.md#series) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from excitingsoda import ExcitingSoda
sdk = ExcitingSoda()

results = sdk.series.get_series_by_id(id = 'id')

pprint(vars(results))

```




