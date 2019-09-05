# coding: utf-8

"""
    PTV Timetable API - Version 3

    The PTV Timetable API provides direct access to Public Transport Victoria’s public transport timetable data.    The API returns scheduled timetable, route and stop data for all metropolitan and regional train, tram and bus services in Victoria, including Night Network(Night Train and Night Tram data are included in metropolitan train and tram services data, respectively, whereas Night Bus is a separate route type).    The API also returns real-time data for metropolitan train, tram and bus services (where this data is made available to PTV), as well as disruption information, stop facility information, and access to myki ticket outlet data.    This Swagger is for Version 3 of the PTV Timetable API. By using this documentation you agree to comply with the licence and terms of service.    Train timetable data is updated daily, while the remaining data is updated weekly, taking into account any planned timetable changes (for example, due to holidays or planned disruptions). The PTV timetable API is the same API used by PTV for its apps. To access the most up to date data PTV has (including real-time data) you must use the API dynamically.    You can access the PTV Timetable API through a HTTP or HTTPS interface, as follows:        base URL / version number / API name / query string  The base URL is either:    *  http://timetableapi.ptv.vic.gov.au  or    *  https://timetableapi.ptv.vic.gov.au    The Swagger JSON file is available at http://timetableapi.ptv.vic.gov.au/swagger/docs/v3    Frequently asked questions are available on the PTV website at http://ptv.vic.gov.au/apifaq    Links to the following information are also provided on the PTV website at http://ptv.vic.gov.au/ptv-timetable-api/  * How to register for an API key and calculate a signature  * PTV Timetable API V2 to V3 Migration Guide  * Documentation for Version 2 of the PTV Timetable API  * PTV Timetable API Data Quality Statement    All information about how to use the API is in this documentation. PTV cannot provide technical support for the API.    Credits: This page has been based on Steve Bennett's http://opentransportdata.org/, used with permission.    # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ptvapi
from ptvapi.api.disruptions_api import DisruptionsApi  # noqa: E501
from ptvapi.rest import ApiException


class TestDisruptionsApi(unittest.TestCase):
    """DisruptionsApi unit test stubs"""

    def setUp(self):
        self.api = ptvapi.api.disruptions_api.DisruptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_disruptions_get_all_disruptions(self):
        """Test case for disruptions_get_all_disruptions

        View all disruptions for all route types  # noqa: E501
        """
        pass

    def test_disruptions_get_disruption_by_id(self):
        """Test case for disruptions_get_disruption_by_id

        View a specific disruption  # noqa: E501
        """
        pass

    def test_disruptions_get_disruption_modes(self):
        """Test case for disruptions_get_disruption_modes

        Get all disruption modes  # noqa: E501
        """
        pass

    def test_disruptions_get_disruptions_by_route(self):
        """Test case for disruptions_get_disruptions_by_route

        View all disruptions for a particular route  # noqa: E501
        """
        pass

    def test_disruptions_get_disruptions_by_route_and_stop(self):
        """Test case for disruptions_get_disruptions_by_route_and_stop

        View all disruptions for a particular route and stop  # noqa: E501
        """
        pass

    def test_disruptions_get_disruptions_by_stop(self):
        """Test case for disruptions_get_disruptions_by_stop

        View all disruptions for a particular stop  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
