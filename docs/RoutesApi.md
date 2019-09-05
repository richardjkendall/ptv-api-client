# ptvapi.RoutesApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**routes_one_or_more_routes**](RoutesApi.md#routes_one_or_more_routes) | **GET** /v3/routes | View route names and numbers for all routes
[**routes_route_from_id**](RoutesApi.md#routes_route_from_id) | **GET** /v3/routes/{route_id} | View route name and number for specific route ID


# **routes_one_or_more_routes**
> V3RouteResponse routes_one_or_more_routes(route_types=route_types, route_name=route_name, token=token, devid=devid, signature=signature)

View route names and numbers for all routes

### Example
```python
from __future__ import print_function
import time
import ptvapi
from ptvapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ptvapi.RoutesApi()
route_types = [56] # list[int] | Filter by route_type; values returned via RouteTypes API (optional)
route_name = 'route_name_example' # str | Filter by name  of route (accepts partial route name matches) (optional)
token = 'token_example' # str | Please ignore (optional)
devid = 'devid_example' # str | Your developer id (optional)
signature = 'signature_example' # str | Authentication signature for request (optional)

try:
    # View route names and numbers for all routes
    api_response = api_instance.routes_one_or_more_routes(route_types=route_types, route_name=route_name, token=token, devid=devid, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->routes_one_or_more_routes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_types** | [**list[int]**](int.md)| Filter by route_type; values returned via RouteTypes API | [optional] 
 **route_name** | **str**| Filter by name  of route (accepts partial route name matches) | [optional] 
 **token** | **str**| Please ignore | [optional] 
 **devid** | **str**| Your developer id | [optional] 
 **signature** | **str**| Authentication signature for request | [optional] 

### Return type

[**V3RouteResponse**](V3RouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **routes_route_from_id**
> V3RouteResponse routes_route_from_id(route_id, token=token, devid=devid, signature=signature)

View route name and number for specific route ID

### Example
```python
from __future__ import print_function
import time
import ptvapi
from ptvapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ptvapi.RoutesApi()
route_id = 56 # int | Identifier of route; values returned by Departures, Directions and Disruptions APIs
token = 'token_example' # str | Please ignore (optional)
devid = 'devid_example' # str | Your developer id (optional)
signature = 'signature_example' # str | Authentication signature for request (optional)

try:
    # View route name and number for specific route ID
    api_response = api_instance.routes_route_from_id(route_id, token=token, devid=devid, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->routes_route_from_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **int**| Identifier of route; values returned by Departures, Directions and Disruptions APIs | 
 **token** | **str**| Please ignore | [optional] 
 **devid** | **str**| Your developer id | [optional] 
 **signature** | **str**| Authentication signature for request | [optional] 

### Return type

[**V3RouteResponse**](V3RouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

