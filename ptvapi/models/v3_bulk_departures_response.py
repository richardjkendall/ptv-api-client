# coding: utf-8

"""
    PTV Timetable API - Version 3

    The PTV Timetable API provides direct access to Public Transport Victoria’s public transport timetable data.    The API returns scheduled timetable, route and stop data for all metropolitan and regional train, tram and bus services in Victoria, including Night Network(Night Train and Night Tram data are included in metropolitan train and tram services data, respectively, whereas Night Bus is a separate route type).    The API also returns real-time data for metropolitan train, tram and bus services (where this data is made available to PTV), as well as disruption information, stop facility information, and access to myki ticket outlet data.    This Swagger is for Version 3 of the PTV Timetable API. By using this documentation you agree to comply with the licence and terms of service.    Train timetable data is updated daily, while the remaining data is updated weekly, taking into account any planned timetable changes (for example, due to holidays or planned disruptions). The PTV timetable API is the same API used by PTV for its apps. To access the most up to date data PTV has (including real-time data) you must use the API dynamically.    You can access the PTV Timetable API through a HTTP or HTTPS interface, as follows:        base URL / version number / API name / query string  The base URL is either:    *  http://timetableapi.ptv.vic.gov.au  or    *  https://timetableapi.ptv.vic.gov.au    The Swagger JSON file is available at http://timetableapi.ptv.vic.gov.au/swagger/docs/v3    Frequently asked questions are available on the PTV website at http://ptv.vic.gov.au/apifaq    Links to the following information are also provided on the PTV website at http://ptv.vic.gov.au/ptv-timetable-api/  * How to register for an API key and calculate a signature  * PTV Timetable API V2 to V3 Migration Guide  * Documentation for Version 2 of the PTV Timetable API  * PTV Timetable API Data Quality Statement    All information about how to use the API is in this documentation. PTV cannot provide technical support for the API.    Credits: This page has been based on Steve Bennett's http://opentransportdata.org/, used with permission.    # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ptvapi.models.v3_bulk_departures_stop_response import V3BulkDeparturesStopResponse  # noqa: F401,E501
from ptvapi.models.v3_bulk_departures_update_response import V3BulkDeparturesUpdateResponse  # noqa: F401,E501
from ptvapi.models.v3_direction import V3Direction  # noqa: F401,E501
from ptvapi.models.v3_disruption import V3Disruption  # noqa: F401,E501
from ptvapi.models.v3_route import V3Route  # noqa: F401,E501
from ptvapi.models.v3_run import V3Run  # noqa: F401,E501
from ptvapi.models.v3_status import V3Status  # noqa: F401,E501


class V3BulkDeparturesResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'responses': 'list[V3BulkDeparturesUpdateResponse]',
        'stops': 'dict(str, V3BulkDeparturesStopResponse)',
        'routes': 'list[V3Route]',
        'runs': 'list[V3Run]',
        'directions': 'list[V3Direction]',
        'disruptions': 'dict(str, V3Disruption)',
        'status': 'V3Status'
    }

    attribute_map = {
        'responses': 'responses',
        'stops': 'stops',
        'routes': 'routes',
        'runs': 'runs',
        'directions': 'directions',
        'disruptions': 'disruptions',
        'status': 'status'
    }

    def __init__(self, responses=None, stops=None, routes=None, runs=None, directions=None, disruptions=None, status=None):  # noqa: E501
        """V3BulkDeparturesResponse - a model defined in Swagger"""  # noqa: E501

        self._responses = None
        self._stops = None
        self._routes = None
        self._runs = None
        self._directions = None
        self._disruptions = None
        self._status = None
        self.discriminator = None

        if responses is not None:
            self.responses = responses
        if stops is not None:
            self.stops = stops
        if routes is not None:
            self.routes = routes
        if runs is not None:
            self.runs = runs
        if directions is not None:
            self.directions = directions
        if disruptions is not None:
            self.disruptions = disruptions
        if status is not None:
            self.status = status

    @property
    def responses(self):
        """Gets the responses of this V3BulkDeparturesResponse.  # noqa: E501

        Contains departures for the requested stop and route(s). It includes details as to the route_direction and whether it is still valid.  # noqa: E501

        :return: The responses of this V3BulkDeparturesResponse.  # noqa: E501
        :rtype: list[V3BulkDeparturesUpdateResponse]
        """
        return self._responses

    @responses.setter
    def responses(self, responses):
        """Sets the responses of this V3BulkDeparturesResponse.

        Contains departures for the requested stop and route(s). It includes details as to the route_direction and whether it is still valid.  # noqa: E501

        :param responses: The responses of this V3BulkDeparturesResponse.  # noqa: E501
        :type: list[V3BulkDeparturesUpdateResponse]
        """

        self._responses = responses

    @property
    def stops(self):
        """Gets the stops of this V3BulkDeparturesResponse.  # noqa: E501

        A train station, tram stop, bus stop, regional coach stop or Night Bus stop  # noqa: E501

        :return: The stops of this V3BulkDeparturesResponse.  # noqa: E501
        :rtype: dict(str, V3BulkDeparturesStopResponse)
        """
        return self._stops

    @stops.setter
    def stops(self, stops):
        """Sets the stops of this V3BulkDeparturesResponse.

        A train station, tram stop, bus stop, regional coach stop or Night Bus stop  # noqa: E501

        :param stops: The stops of this V3BulkDeparturesResponse.  # noqa: E501
        :type: dict(str, V3BulkDeparturesStopResponse)
        """

        self._stops = stops

    @property
    def routes(self):
        """Gets the routes of this V3BulkDeparturesResponse.  # noqa: E501

        Train lines, tram routes, bus routes, regional coach routes, Night Bus routes  # noqa: E501

        :return: The routes of this V3BulkDeparturesResponse.  # noqa: E501
        :rtype: list[V3Route]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this V3BulkDeparturesResponse.

        Train lines, tram routes, bus routes, regional coach routes, Night Bus routes  # noqa: E501

        :param routes: The routes of this V3BulkDeparturesResponse.  # noqa: E501
        :type: list[V3Route]
        """

        self._routes = routes

    @property
    def runs(self):
        """Gets the runs of this V3BulkDeparturesResponse.  # noqa: E501

        Individual trips/services of a route  # noqa: E501

        :return: The runs of this V3BulkDeparturesResponse.  # noqa: E501
        :rtype: list[V3Run]
        """
        return self._runs

    @runs.setter
    def runs(self, runs):
        """Sets the runs of this V3BulkDeparturesResponse.

        Individual trips/services of a route  # noqa: E501

        :param runs: The runs of this V3BulkDeparturesResponse.  # noqa: E501
        :type: list[V3Run]
        """

        self._runs = runs

    @property
    def directions(self):
        """Gets the directions of this V3BulkDeparturesResponse.  # noqa: E501

        Directions of travel of route  # noqa: E501

        :return: The directions of this V3BulkDeparturesResponse.  # noqa: E501
        :rtype: list[V3Direction]
        """
        return self._directions

    @directions.setter
    def directions(self, directions):
        """Sets the directions of this V3BulkDeparturesResponse.

        Directions of travel of route  # noqa: E501

        :param directions: The directions of this V3BulkDeparturesResponse.  # noqa: E501
        :type: list[V3Direction]
        """

        self._directions = directions

    @property
    def disruptions(self):
        """Gets the disruptions of this V3BulkDeparturesResponse.  # noqa: E501

        Disruption information applicable to relevant routes or stops  # noqa: E501

        :return: The disruptions of this V3BulkDeparturesResponse.  # noqa: E501
        :rtype: dict(str, V3Disruption)
        """
        return self._disruptions

    @disruptions.setter
    def disruptions(self, disruptions):
        """Sets the disruptions of this V3BulkDeparturesResponse.

        Disruption information applicable to relevant routes or stops  # noqa: E501

        :param disruptions: The disruptions of this V3BulkDeparturesResponse.  # noqa: E501
        :type: dict(str, V3Disruption)
        """

        self._disruptions = disruptions

    @property
    def status(self):
        """Gets the status of this V3BulkDeparturesResponse.  # noqa: E501

        API Status / Metadata  # noqa: E501

        :return: The status of this V3BulkDeparturesResponse.  # noqa: E501
        :rtype: V3Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V3BulkDeparturesResponse.

        API Status / Metadata  # noqa: E501

        :param status: The status of this V3BulkDeparturesResponse.  # noqa: E501
        :type: V3Status
        """

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V3BulkDeparturesResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V3BulkDeparturesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
