# ptvapi.DirectionsApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**directions_for_direction**](DirectionsApi.md#directions_for_direction) | **GET** /v3/directions/{direction_id} | View all routes for a direction of travel
[**directions_for_direction_and_type**](DirectionsApi.md#directions_for_direction_and_type) | **GET** /v3/directions/{direction_id}/route_type/{route_type} | View all routes of a particular type for a direction of travel
[**directions_for_route**](DirectionsApi.md#directions_for_route) | **GET** /v3/directions/route/{route_id} | View directions that a route travels in


# **directions_for_direction**
> V3DirectionsResponse directions_for_direction(direction_id, token=token, devid=devid, signature=signature)

View all routes for a direction of travel

### Example
```python
from __future__ import print_function
import time
import ptvapi
from ptvapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ptvapi.DirectionsApi()
direction_id = 56 # int | Identifier of direction of travel; values returned by Directions API - /v3/directions/route/{route_id}
token = 'token_example' # str | Please ignore (optional)
devid = 'devid_example' # str | Your developer id (optional)
signature = 'signature_example' # str | Authentication signature for request (optional)

try:
    # View all routes for a direction of travel
    api_response = api_instance.directions_for_direction(direction_id, token=token, devid=devid, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectionsApi->directions_for_direction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction_id** | **int**| Identifier of direction of travel; values returned by Directions API - /v3/directions/route/{route_id} | 
 **token** | **str**| Please ignore | [optional] 
 **devid** | **str**| Your developer id | [optional] 
 **signature** | **str**| Authentication signature for request | [optional] 

### Return type

[**V3DirectionsResponse**](V3DirectionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directions_for_direction_and_type**
> V3DirectionsResponse directions_for_direction_and_type(direction_id, route_type, token=token, devid=devid, signature=signature)

View all routes of a particular type for a direction of travel

### Example
```python
from __future__ import print_function
import time
import ptvapi
from ptvapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ptvapi.DirectionsApi()
direction_id = 56 # int | Identifier of direction of travel; values returned by Directions API - /v3/directions/route/{route_id}
route_type = 56 # int | Number identifying transport mode; values returned via RouteTypes API
token = 'token_example' # str | Please ignore (optional)
devid = 'devid_example' # str | Your developer id (optional)
signature = 'signature_example' # str | Authentication signature for request (optional)

try:
    # View all routes of a particular type for a direction of travel
    api_response = api_instance.directions_for_direction_and_type(direction_id, route_type, token=token, devid=devid, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectionsApi->directions_for_direction_and_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction_id** | **int**| Identifier of direction of travel; values returned by Directions API - /v3/directions/route/{route_id} | 
 **route_type** | **int**| Number identifying transport mode; values returned via RouteTypes API | 
 **token** | **str**| Please ignore | [optional] 
 **devid** | **str**| Your developer id | [optional] 
 **signature** | **str**| Authentication signature for request | [optional] 

### Return type

[**V3DirectionsResponse**](V3DirectionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directions_for_route**
> V3DirectionsResponse directions_for_route(route_id, token=token, devid=devid, signature=signature)

View directions that a route travels in

### Example
```python
from __future__ import print_function
import time
import ptvapi
from ptvapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ptvapi.DirectionsApi()
route_id = 56 # int | Identifier of route; values returned by Routes API - v3/routes
token = 'token_example' # str | Please ignore (optional)
devid = 'devid_example' # str | Your developer id (optional)
signature = 'signature_example' # str | Authentication signature for request (optional)

try:
    # View directions that a route travels in
    api_response = api_instance.directions_for_route(route_id, token=token, devid=devid, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectionsApi->directions_for_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **int**| Identifier of route; values returned by Routes API - v3/routes | 
 **token** | **str**| Please ignore | [optional] 
 **devid** | **str**| Your developer id | [optional] 
 **signature** | **str**| Authentication signature for request | [optional] 

### Return type

[**V3DirectionsResponse**](V3DirectionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

