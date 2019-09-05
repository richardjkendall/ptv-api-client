# ptvapi.OutletsApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**outlets_get_all_outlets**](OutletsApi.md#outlets_get_all_outlets) | **GET** /v3/outlets | List all ticket outlets
[**outlets_get_outlets_by_geolocation**](OutletsApi.md#outlets_get_outlets_by_geolocation) | **GET** /v3/outlets/location/{latitude},{longitude} | List ticket outlets near a specific location


# **outlets_get_all_outlets**
> V3OutletResponse outlets_get_all_outlets(max_results=max_results, token=token, devid=devid, signature=signature)

List all ticket outlets

### Example
```python
from __future__ import print_function
import time
import ptvapi
from ptvapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ptvapi.OutletsApi()
max_results = 56 # int | Maximum number of results returned (default = 30) (optional)
token = 'token_example' # str | Please ignore (optional)
devid = 'devid_example' # str | Your developer id (optional)
signature = 'signature_example' # str | Authentication signature for request (optional)

try:
    # List all ticket outlets
    api_response = api_instance.outlets_get_all_outlets(max_results=max_results, token=token, devid=devid, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutletsApi->outlets_get_all_outlets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_results** | **int**| Maximum number of results returned (default &#x3D; 30) | [optional] 
 **token** | **str**| Please ignore | [optional] 
 **devid** | **str**| Your developer id | [optional] 
 **signature** | **str**| Authentication signature for request | [optional] 

### Return type

[**V3OutletResponse**](V3OutletResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outlets_get_outlets_by_geolocation**
> V3OutletGeolocationResponse outlets_get_outlets_by_geolocation(latitude, longitude, max_distance=max_distance, max_results=max_results, token=token, devid=devid, signature=signature)

List ticket outlets near a specific location

### Example
```python
from __future__ import print_function
import time
import ptvapi
from ptvapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ptvapi.OutletsApi()
latitude = 3.4 # float | Geographic coordinate of latitude
longitude = 3.4 # float | Geographic coordinate of longitude
max_distance = 1.2 # float | Filter by maximum distance (in metres) from location specified via latitude and longitude parameters (default = 300) (optional)
max_results = 56 # int | Maximum number of results returned (default = 30) (optional)
token = 'token_example' # str | Please ignore (optional)
devid = 'devid_example' # str | Your developer id (optional)
signature = 'signature_example' # str | Authentication signature for request (optional)

try:
    # List ticket outlets near a specific location
    api_response = api_instance.outlets_get_outlets_by_geolocation(latitude, longitude, max_distance=max_distance, max_results=max_results, token=token, devid=devid, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutletsApi->outlets_get_outlets_by_geolocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **float**| Geographic coordinate of latitude | 
 **longitude** | **float**| Geographic coordinate of longitude | 
 **max_distance** | **float**| Filter by maximum distance (in metres) from location specified via latitude and longitude parameters (default &#x3D; 300) | [optional] 
 **max_results** | **int**| Maximum number of results returned (default &#x3D; 30) | [optional] 
 **token** | **str**| Please ignore | [optional] 
 **devid** | **str**| Your developer id | [optional] 
 **signature** | **str**| Authentication signature for request | [optional] 

### Return type

[**V3OutletGeolocationResponse**](V3OutletGeolocationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

