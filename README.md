# PTV API v3 Client
The PTV Timetable API provides direct access to Public Transport Victoria’s public transport timetable data.    

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) but the code has been modified to support automatically generating the authorisation signature

- API version: v3
- Package version: 1.0.0
- Build package: ptvapi

For more information, please visit [https://timetableapi.ptv.vic.gov.au/swagger/ui/index](https://timetableapi.ptv.vic.gov.au/swagger/ui/index)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

### pip install

This package is available on PyPi, and you can install it in your environment (we recommend always using a venv) as follows

```sh
pip install ptvapi
```
(you may need to run `pip` with root permission: `sudo pip install ptvapiclient`)

Then import the package:
```python
import ptvapi 
```

### Setuptools

You can also clone this repo and install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ptvapi
```

## Getting Started

### API Key
Before you can get started you need a developer ID and secret issued by PTV.  There are instructions on this here [https://www.ptv.vic.gov.au/assets/default-site/footer/data-and-reporting/Datasets/PTV-Timetable-API/60096c0692/PTV-Timetable-API-key-and-signature-document.rtf](https://www.ptv.vic.gov.au/assets/default-site/footer/data-and-reporting/Datasets/PTV-Timetable-API/60096c0692/PTV-Timetable-API-key-and-signature-document.rtf)

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import ptvapi
from ptvapi.rest import ApiException
from pprint import pprint

devid = '<your dev ID>'
key = b'<your key>'

config = ptvapi.Configuration()
config.devid = devid
config.key = key
api_instance = ptvapi.RouteTypesApi(ptvapi.ApiClient(config))


try:
    api_response = api_instance.route_types_get_route_types()
    pprint(api_response)
except ApiException as e:
    print("Error calling API")
```

## Documentation for API Endpoints & Models

This client is based on v3 of the PTV API.  This API is fully documented here [https://timetableapi.ptv.vic.gov.au/swagger/ui/index](https://timetableapi.ptv.vic.gov.au/swagger/ui/index)

## Documentation For Authorization

Traditional authentication/authorisation is not used.  Each GET requires a signature to be calucated based on the resource path and query parameters.  The client will handle this in the background.

To access this feature, make sure that each time you create an API client instance, you pass a `Configuration` object with the `devid` and `key` attributes set.  e.g.

```python
devid = '<your dev ID>'
key = b'<your key>'

config = ptvapi.Configuration()
config.devid = devid
config.key = key
api_instance = ptvapi.RouteTypesApi(ptvapi.ApiClient(config))
```

## Author

Richard Kendall



