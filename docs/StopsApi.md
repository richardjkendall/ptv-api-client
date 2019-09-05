# ptvapi.StopsApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stops_stop_details**](StopsApi.md#stops_stop_details) | **GET** /v3/stops/{stop_id}/route_type/{route_type} | View facilities at a specific stop (Metro and V/Line stations only)
[**stops_stops_by_geolocation**](StopsApi.md#stops_stops_by_geolocation) | **GET** /v3/stops/location/{latitude},{longitude} | View all stops near a specific location
[**stops_stops_for_route**](StopsApi.md#stops_stops_for_route) | **GET** /v3/stops/route/{route_id}/route_type/{route_type} | View all stops on a specific route


# **stops_stop_details**
> V3StopResponse stops_stop_details(stop_id, route_type, stop_location=stop_location, stop_amenities=stop_amenities, stop_accessibility=stop_accessibility, stop_contact=stop_contact, stop_ticket=stop_ticket, gtfs=gtfs, stop_staffing=stop_staffing, stop_disruptions=stop_disruptions, token=token, devid=devid, signature=signature)

View facilities at a specific stop (Metro and V/Line stations only)

### Example
```python
from __future__ import print_function
import time
import ptvapi
from ptvapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ptvapi.StopsApi()
stop_id = 56 # int | Identifier of stop; values returned by Stops API
route_type = 56 # int | Number identifying transport mode; values returned via RouteTypes API
stop_location = true # bool | Indicates if stop location information will be returned (default = false) (optional)
stop_amenities = true # bool | Indicates if stop amenity information will be returned (default = false) (optional)
stop_accessibility = true # bool | Indicates if stop accessibility information will be returned (default = false) (optional)
stop_contact = true # bool | Indicates if stop contact information will be returned (default = false) (optional)
stop_ticket = true # bool | Indicates if stop ticket information will be returned (default = false) (optional)
gtfs = true # bool | Incdicates whether the stop_id is a GTFS ID or not (optional)
stop_staffing = true # bool | Indicates if stop staffing information will be returned (default = false) (optional)
stop_disruptions = true # bool | Indicates if stop disruption information will be returned (default = false) (optional)
token = 'token_example' # str | Please ignore (optional)
devid = 'devid_example' # str | Your developer id (optional)
signature = 'signature_example' # str | Authentication signature for request (optional)

try:
    # View facilities at a specific stop (Metro and V/Line stations only)
    api_response = api_instance.stops_stop_details(stop_id, route_type, stop_location=stop_location, stop_amenities=stop_amenities, stop_accessibility=stop_accessibility, stop_contact=stop_contact, stop_ticket=stop_ticket, gtfs=gtfs, stop_staffing=stop_staffing, stop_disruptions=stop_disruptions, token=token, devid=devid, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StopsApi->stops_stop_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stop_id** | **int**| Identifier of stop; values returned by Stops API | 
 **route_type** | **int**| Number identifying transport mode; values returned via RouteTypes API | 
 **stop_location** | **bool**| Indicates if stop location information will be returned (default &#x3D; false) | [optional] 
 **stop_amenities** | **bool**| Indicates if stop amenity information will be returned (default &#x3D; false) | [optional] 
 **stop_accessibility** | **bool**| Indicates if stop accessibility information will be returned (default &#x3D; false) | [optional] 
 **stop_contact** | **bool**| Indicates if stop contact information will be returned (default &#x3D; false) | [optional] 
 **stop_ticket** | **bool**| Indicates if stop ticket information will be returned (default &#x3D; false) | [optional] 
 **gtfs** | **bool**| Incdicates whether the stop_id is a GTFS ID or not | [optional] 
 **stop_staffing** | **bool**| Indicates if stop staffing information will be returned (default &#x3D; false) | [optional] 
 **stop_disruptions** | **bool**| Indicates if stop disruption information will be returned (default &#x3D; false) | [optional] 
 **token** | **str**| Please ignore | [optional] 
 **devid** | **str**| Your developer id | [optional] 
 **signature** | **str**| Authentication signature for request | [optional] 

### Return type

[**V3StopResponse**](V3StopResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stops_stops_by_geolocation**
> V3StopsByDistanceResponse stops_stops_by_geolocation(latitude, longitude, route_types=route_types, max_results=max_results, max_distance=max_distance, stop_disruptions=stop_disruptions, token=token, devid=devid, signature=signature)

View all stops near a specific location

### Example
```python
from __future__ import print_function
import time
import ptvapi
from ptvapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ptvapi.StopsApi()
latitude = 3.4 # float | Geographic coordinate of latitude
longitude = 3.4 # float | Geographic coordinate of longitude
route_types = [56] # list[int] | Filter by route_type; values returned via RouteTypes API (optional)
max_results = 56 # int | Maximum number of results returned (default = 30) (optional)
max_distance = 1.2 # float | Filter by maximum distance (in metres) from location specified via latitude and longitude parameters (default = 300) (optional)
stop_disruptions = true # bool | Indicates if stop disruption information will be returned (default = false) (optional)
token = 'token_example' # str | Please ignore (optional)
devid = 'devid_example' # str | Your developer id (optional)
signature = 'signature_example' # str | Authentication signature for request (optional)

try:
    # View all stops near a specific location
    api_response = api_instance.stops_stops_by_geolocation(latitude, longitude, route_types=route_types, max_results=max_results, max_distance=max_distance, stop_disruptions=stop_disruptions, token=token, devid=devid, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StopsApi->stops_stops_by_geolocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **float**| Geographic coordinate of latitude | 
 **longitude** | **float**| Geographic coordinate of longitude | 
 **route_types** | [**list[int]**](int.md)| Filter by route_type; values returned via RouteTypes API | [optional] 
 **max_results** | **int**| Maximum number of results returned (default &#x3D; 30) | [optional] 
 **max_distance** | **float**| Filter by maximum distance (in metres) from location specified via latitude and longitude parameters (default &#x3D; 300) | [optional] 
 **stop_disruptions** | **bool**| Indicates if stop disruption information will be returned (default &#x3D; false) | [optional] 
 **token** | **str**| Please ignore | [optional] 
 **devid** | **str**| Your developer id | [optional] 
 **signature** | **str**| Authentication signature for request | [optional] 

### Return type

[**V3StopsByDistanceResponse**](V3StopsByDistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stops_stops_for_route**
> V3StopsOnRouteResponse stops_stops_for_route(route_id, route_type, direction_id=direction_id, stop_disruptions=stop_disruptions, token=token, devid=devid, signature=signature)

View all stops on a specific route

### Example
```python
from __future__ import print_function
import time
import ptvapi
from ptvapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ptvapi.StopsApi()
route_id = 56 # int | Identifier of route; values returned by Routes API - v3/routes
route_type = 56 # int | Number identifying transport mode; values returned via RouteTypes API
direction_id = 56 # int | An optional direction; values returned by Directions API. When this is set, stop sequence information is returned in the response. (optional)
stop_disruptions = true # bool | Indicates if stop disruption information will be returned (default = false) (optional)
token = 'token_example' # str | Please ignore (optional)
devid = 'devid_example' # str | Your developer id (optional)
signature = 'signature_example' # str | Authentication signature for request (optional)

try:
    # View all stops on a specific route
    api_response = api_instance.stops_stops_for_route(route_id, route_type, direction_id=direction_id, stop_disruptions=stop_disruptions, token=token, devid=devid, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StopsApi->stops_stops_for_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **int**| Identifier of route; values returned by Routes API - v3/routes | 
 **route_type** | **int**| Number identifying transport mode; values returned via RouteTypes API | 
 **direction_id** | **int**| An optional direction; values returned by Directions API. When this is set, stop sequence information is returned in the response. | [optional] 
 **stop_disruptions** | **bool**| Indicates if stop disruption information will be returned (default &#x3D; false) | [optional] 
 **token** | **str**| Please ignore | [optional] 
 **devid** | **str**| Your developer id | [optional] 
 **signature** | **str**| Authentication signature for request | [optional] 

### Return type

[**V3StopsOnRouteResponse**](V3StopsOnRouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

