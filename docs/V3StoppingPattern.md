# V3StoppingPattern

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disruptions** | [**list[V3Disruption]**](V3Disruption.md) | Disruption information applicable to relevant routes or stops | [optional] 
**departures** | [**list[V3Departure]**](V3Departure.md) | Timetabled and real-time service departures | [optional] 
**stops** | [**dict(str, V3ResultStop)**](V3ResultStop.md) | A train station, tram stop, bus stop, regional coach stop or Night Bus stop | [optional] 
**routes** | [**dict(str, V3Route)**](V3Route.md) | Train lines, tram routes, bus routes, regional coach routes, Night Bus routes | [optional] 
**runs** | [**dict(str, V3Run)**](V3Run.md) | Individual trips/services of a route | [optional] 
**directions** | [**dict(str, V3Direction)**](V3Direction.md) | Directions of travel of route | [optional] 
**status** | [**V3Status**](V3Status.md) | API Status / Metadata | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


