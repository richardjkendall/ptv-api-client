# V3StopDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disruption_ids** | **list[int]** | Disruption information identifier(s) | [optional] 
**station_type** | **str** | Type of metropolitan train station (i.e. \&quot;Premium\&quot;, \&quot;Host\&quot; or \&quot;Unstaffed\&quot; station); returns null for V/Line train | [optional] 
**station_description** | **str** | The definition applicable to the station_type; returns null for V/Line train | [optional] 
**route_type** | **int** | Transport mode identifier | [optional] 
**stop_location** | [**V3StopLocation**](V3StopLocation.md) | Location details of the stop | [optional] 
**stop_amenities** | [**V3StopAmenityDetails**](V3StopAmenityDetails.md) | Amenity and facility details at the stop | [optional] 
**stop_accessibility** | [**V3StopAccessibility**](V3StopAccessibility.md) | Facilities relating to the accessibility of the stop | [optional] 
**stop_staffing** | [**V3StopStaffing**](V3StopStaffing.md) | Staffing details for the stop | [optional] 
**stop_id** | **int** | Stop identifier | [optional] 
**stop_name** | **str** | Name of stop | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


