# ExcitingSoda Python SDK 0.0.1
A Python SDK for ExcitingSoda.

A test API for LibLab

- API version: 0.0.1
- SDK version: 0.0.1

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
    - [Dependencies](#dependencies)
- [API Endpoint Services](#api-endpoint-services)
- [API Models](#api-models)
- [Testing](#testing)
- [Configuration](#configuration)
- [Sample Usage](#sample-usage)
- [ExcitingSoda Services](#excitingsoda-services)

## Installation
```bash
pip install exciting-soda
```

### Dependencies

This SDK uses the following dependencies:
- requests 2.28.1
- http-exceptions 0.2.10
- pytest 7.1.2
- responses 0.21.0


## API Endpoint Services

All URIs are relative to http://na.exciting.soda.

Click the service name for a full list of the service methods.

| Service |
| :------ |
|[Movie](./services/README.md#movie)|
|[Series](./services/README.md#series)|

## API Models
[A list documenting all API models for this SDK](./models/README.md#excitingsoda-models).

## Testing

Run unit tests with this command:

```sh
python -m unittest discover -p "test*.py" 
```

## Sample Usage

```py
from os import getenv
from pprint import pprint
from excitingsoda import ExcitingSoda

sdk = ExcitingSoda()

results = sdk.movie.get_movies()

pprint(vars(results))
```


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






