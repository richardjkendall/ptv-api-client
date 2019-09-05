# ptvapi.RunsApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**runs_for_route**](RunsApi.md#runs_for_route) | **GET** /v3/runs/route/{route_id} | View all trip/service runs for a specific route ID
[**runs_for_route_and_route_type**](RunsApi.md#runs_for_route_and_route_type) | **GET** /v3/runs/route/{route_id}/route_type/{route_type} | View all trip/service runs for a specific route ID and route type
[**runs_for_run**](RunsApi.md#runs_for_run) | **GET** /v3/runs/{run_id} | View all trip/service runs for a specific run ID
[**runs_for_run_and_route_type**](RunsApi.md#runs_for_run_and_route_type) | **GET** /v3/runs/{run_id}/route_type/{route_type} | View the trip/service run for a specific run ID and route type


# **runs_for_route**
> V3RunsResponse runs_for_route(route_id, token=token, devid=devid, signature=signature)

View all trip/service runs for a specific route ID

### Example
```python
from __future__ import print_function
import time
import ptvapi
from ptvapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ptvapi.RunsApi()
route_id = 56 # int | Identifier of route; values returned by Routes API - v3/routes.
token = 'token_example' # str | Please ignore (optional)
devid = 'devid_example' # str | Your developer id (optional)
signature = 'signature_example' # str | Authentication signature for request (optional)

try:
    # View all trip/service runs for a specific route ID
    api_response = api_instance.runs_for_route(route_id, token=token, devid=devid, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunsApi->runs_for_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **int**| Identifier of route; values returned by Routes API - v3/routes. | 
 **token** | **str**| Please ignore | [optional] 
 **devid** | **str**| Your developer id | [optional] 
 **signature** | **str**| Authentication signature for request | [optional] 

### Return type

[**V3RunsResponse**](V3RunsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **runs_for_route_and_route_type**
> V3RunsResponse runs_for_route_and_route_type(route_id, route_type, token=token, devid=devid, signature=signature)

View all trip/service runs for a specific route ID and route type

### Example
```python
from __future__ import print_function
import time
import ptvapi
from ptvapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ptvapi.RunsApi()
route_id = 56 # int | Identifier of route; values returned by Routes API - v3/routes.
route_type = 56 # int | Number identifying transport mode; values returned via RouteTypes API
token = 'token_example' # str | Please ignore (optional)
devid = 'devid_example' # str | Your developer id (optional)
signature = 'signature_example' # str | Authentication signature for request (optional)

try:
    # View all trip/service runs for a specific route ID and route type
    api_response = api_instance.runs_for_route_and_route_type(route_id, route_type, token=token, devid=devid, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunsApi->runs_for_route_and_route_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **int**| Identifier of route; values returned by Routes API - v3/routes. | 
 **route_type** | **int**| Number identifying transport mode; values returned via RouteTypes API | 
 **token** | **str**| Please ignore | [optional] 
 **devid** | **str**| Your developer id | [optional] 
 **signature** | **str**| Authentication signature for request | [optional] 

### Return type

[**V3RunsResponse**](V3RunsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **runs_for_run**
> V3RunsResponse runs_for_run(run_id, token=token, devid=devid, signature=signature)

View all trip/service runs for a specific run ID

### Example
```python
from __future__ import print_function
import time
import ptvapi
from ptvapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ptvapi.RunsApi()
run_id = 56 # int | Identifier of a trip/service run; values returned by Runs API - /v3/route/{route_id} and Departures API
token = 'token_example' # str | Please ignore (optional)
devid = 'devid_example' # str | Your developer id (optional)
signature = 'signature_example' # str | Authentication signature for request (optional)

try:
    # View all trip/service runs for a specific run ID
    api_response = api_instance.runs_for_run(run_id, token=token, devid=devid, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunsApi->runs_for_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **int**| Identifier of a trip/service run; values returned by Runs API - /v3/route/{route_id} and Departures API | 
 **token** | **str**| Please ignore | [optional] 
 **devid** | **str**| Your developer id | [optional] 
 **signature** | **str**| Authentication signature for request | [optional] 

### Return type

[**V3RunsResponse**](V3RunsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **runs_for_run_and_route_type**
> V3RunResponse runs_for_run_and_route_type(run_id, route_type, token=token, devid=devid, signature=signature)

View the trip/service run for a specific run ID and route type

### Example
```python
from __future__ import print_function
import time
import ptvapi
from ptvapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ptvapi.RunsApi()
run_id = 56 # int | Identifier of a trip/service run; values returned by Runs API - /v3/route/{route_id} and Departures API
route_type = 56 # int | Number identifying transport mode; values returned via RouteTypes API
token = 'token_example' # str | Please ignore (optional)
devid = 'devid_example' # str | Your developer id (optional)
signature = 'signature_example' # str | Authentication signature for request (optional)

try:
    # View the trip/service run for a specific run ID and route type
    api_response = api_instance.runs_for_run_and_route_type(run_id, route_type, token=token, devid=devid, signature=signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunsApi->runs_for_run_and_route_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **int**| Identifier of a trip/service run; values returned by Runs API - /v3/route/{route_id} and Departures API | 
 **route_type** | **int**| Number identifying transport mode; values returned via RouteTypes API | 
 **token** | **str**| Please ignore | [optional] 
 **devid** | **str**| Your developer id | [optional] 
 **signature** | **str**| Authentication signature for request | [optional] 

### Return type

[**V3RunResponse**](V3RunResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

