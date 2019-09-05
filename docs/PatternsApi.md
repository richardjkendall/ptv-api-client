# ptvapi.PatternsApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patterns_get_pattern_by_run**](PatternsApi.md#patterns_get_pattern_by_run) | **GET** /v3/pattern/run/{run_id}/route_type/{route_type} | View the stopping pattern for a specific trip/service run


# **patterns_get_pattern_by_run**
> V3StoppingPattern patterns_get_pattern_by_run(run_id, route_type, expand, stop_id=stop_id, date_utc=date_utc, token=token, devid=devid, signature=signature)

View the stopping pattern for a specific trip/service run

### Example
```python
from __future__ import print_function
import time
import ptvapi
from ptvapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ptvapi.PatternsApi()
run_id = 56 # int | Identifier of a trip/service run; values returned by Runs API - /v3/route/{route_id} and Departures API
route_type = 56 # int | Number identifying transport mode; values returned via RouteTypes API
expand = ['expand_example'] # list[str] | Objects to be returned in full (i.e. expanded) - options include: all, stop, route, run, direction, disruption. By default disruptions are expanded.
stop_id = 56 # int | Filter by stop_id; values returned by Stops API (optional)
date_utc = '2013-10-20T19:20:30+01:00' # datetime | Filter by the date and time of the request (ISO 8601 UTC format) (optional)
token = 'token_example' # str | Please ignore (optional)
devid = 'devid_example' # str | Your developer id (optional)
signature = 'signature_example' # str | Authentication signature for request (optional)

try:
    # View the stopping pattern for a specific trip/service run
    api_response = api_instance.patterns_get_pattern_by_run(run_id, route_type, expand, stop_id=stop_id, date_utc=date_utc, token=token, devid=devid, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PatternsApi->patterns_get_pattern_by_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **int**| Identifier of a trip/service run; values returned by Runs API - /v3/route/{route_id} and Departures API | 
 **route_type** | **int**| Number identifying transport mode; values returned via RouteTypes API | 
 **expand** | [**list[str]**](str.md)| Objects to be returned in full (i.e. expanded) - options include: all, stop, route, run, direction, disruption. By default disruptions are expanded. | 
 **stop_id** | **int**| Filter by stop_id; values returned by Stops API | [optional] 
 **date_utc** | **datetime**| Filter by the date and time of the request (ISO 8601 UTC format) | [optional] 
 **token** | **str**| Please ignore | [optional] 
 **devid** | **str**| Your developer id | [optional] 
 **signature** | **str**| Authentication signature for request | [optional] 

### Return type

[**V3StoppingPattern**](V3StoppingPattern.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

