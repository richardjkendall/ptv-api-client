# V3Disruption

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disruption_id** | **int** | Disruption information identifier | [optional] 
**title** | **str** | Headline title summarising disruption information | [optional] 
**url** | **str** | URL of relevant article on PTV website | [optional] 
**description** | **str** | Description of the disruption | [optional] 
**disruption_status** | **str** | Status of the disruption (e.g. \&quot;Planned\&quot;, \&quot;Current\&quot;) | [optional] 
**disruption_type** | **str** | Type of disruption | [optional] 
**published_on** | **datetime** | Date and time disruption information is published on PTV website, in ISO 8601 UTC format | [optional] 
**last_updated** | **datetime** | Date and time disruption information was last updated by PTV, in ISO 8601 UTC format | [optional] 
**from_date** | **datetime** | Date and time at which disruption begins, in ISO 8601 UTC format | [optional] 
**to_date** | **datetime** | Date and time at which disruption ends, in ISO 8601 UTC format (returns null if unknown) | [optional] 
**routes** | [**list[V3DisruptionRoute]**](V3DisruptionRoute.md) | Route relevant to a disruption (if applicable) | [optional] 
**stops** | [**list[V3DisruptionStop]**](V3DisruptionStop.md) | Stop relevant to a disruption (if applicable) | [optional] 
**colour** | **str** |  | [optional] 
**display_on_board** | **bool** |  | [optional] 
**display_status** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


