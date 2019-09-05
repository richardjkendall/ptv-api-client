# V3BulkDeparturesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responses** | [**list[V3BulkDeparturesUpdateResponse]**](V3BulkDeparturesUpdateResponse.md) | Contains departures for the requested stop and route(s). It includes details as to the route_direction and whether it is still valid. | [optional] 
**stops** | [**dict(str, V3BulkDeparturesStopResponse)**](V3BulkDeparturesStopResponse.md) | A train station, tram stop, bus stop, regional coach stop or Night Bus stop | [optional] 
**routes** | [**list[V3Route]**](V3Route.md) | Train lines, tram routes, bus routes, regional coach routes, Night Bus routes | [optional] 
**runs** | [**list[V3Run]**](V3Run.md) | Individual trips/services of a route | [optional] 
**directions** | [**list[V3Direction]**](V3Direction.md) | Directions of travel of route | [optional] 
**disruptions** | [**dict(str, V3Disruption)**](V3Disruption.md) | Disruption information applicable to relevant routes or stops | [optional] 
**status** | [**V3Status**](V3Status.md) | API Status / Metadata | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


