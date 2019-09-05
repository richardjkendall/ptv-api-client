# V3BulkDeparturesUpdateResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**departures** | [**list[V3Departure]**](V3Departure.md) | Timetabled and real-time service departures | [optional] 
**route_type** | **int** | Transport mode identifier | [optional] 
**stop_id** | **int** | Stop identifier | [optional] 
**requested_route_direction** | [**V3BulkDeparturesRouteDirectionResponse**](V3BulkDeparturesRouteDirectionResponse.md) | The route direction that these departures are for. Will be one of the requested route directions | [optional] 
**route_direction_status** | **int** | The status of the route direction (changed | unchanged).              If changed, requests should change the requested_route_direction for the route_direction supplied. | [optional] 
**route_direction** | [**V3BulkDeparturesRouteDirectionResponse**](V3BulkDeparturesRouteDirectionResponse.md) | The route direction found matching the requested_route_direction | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


