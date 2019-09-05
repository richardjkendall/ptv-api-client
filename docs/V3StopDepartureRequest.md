# V3StopDepartureRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**route_type** | **int** | Number identifying transport mode; values returned via RouteTypes API | [optional] 
**stop_id** | **int** | Identifier of stop; values returned by Stops API | [optional] 
**max_results** | **int** | Maximum number of results returned | [optional] 
**gtfs** | **bool** | Indicates that stop_id parameter will accept \&quot;GTFS stop_id\&quot; data and route_directions[x].route_id parameters will accept route_gtfs_id data | [optional] 
**route_directions** | [**list[V3StopDepartureRequestRouteDirection]**](V3StopDepartureRequestRouteDirection.md) | The route directions to find departures for at this stop. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


