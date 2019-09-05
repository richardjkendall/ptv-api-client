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


class V3StopStaffing(object):
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
        'fri_am_from': 'str',
        'fri_am_to': 'str',
        'fri_pm_from': 'str',
        'fri_pm_to': 'str',
        'mon_am_from': 'str',
        'mon_am_to': 'str',
        'mon_pm_from': 'str',
        'mon_pm_to': 'str',
        'ph_additional_text': 'str',
        'ph_from': 'str',
        'ph_to': 'str',
        'sat_am_from': 'str',
        'sat_am_to': 'str',
        'sat_pm_from': 'str',
        'sat_pm_to': 'str',
        'sun_am_from': 'str',
        'sun_am_to': 'str',
        'sun_pm_from': 'str',
        'sun_pm_to': 'str',
        'thu_am_from': 'str',
        'thu_am_to': 'str',
        'thu_pm_from': 'str',
        'thu_pm_to': 'str',
        'tue_am_from': 'str',
        'tue_am_to': 'str',
        'tue_pm_from': 'str',
        'tue_pm_to': 'str',
        'wed_am_from': 'str',
        'wed_am_to': 'str',
        'wed_pm_from': 'str',
        'wed_pm_to': 'str'
    }

    attribute_map = {
        'fri_am_from': 'fri_am_from',
        'fri_am_to': 'fri_am_to',
        'fri_pm_from': 'fri_pm_from',
        'fri_pm_to': 'fri_pm_to',
        'mon_am_from': 'mon_am_from',
        'mon_am_to': 'mon_am_to',
        'mon_pm_from': 'mon_pm_from',
        'mon_pm_to': 'mon_pm_to',
        'ph_additional_text': 'ph_additional_text',
        'ph_from': 'ph_from',
        'ph_to': 'ph_to',
        'sat_am_from': 'sat_am_from',
        'sat_am_to': 'sat_am_to',
        'sat_pm_from': 'sat_pm_from',
        'sat_pm_to': 'sat_pm_to',
        'sun_am_from': 'sun_am_from',
        'sun_am_to': 'sun_am_to',
        'sun_pm_from': 'sun_pm_from',
        'sun_pm_to': 'sun_pm_to',
        'thu_am_from': 'thu_am_from',
        'thu_am_to': 'thu_am_to',
        'thu_pm_from': 'thu_pm_from',
        'thu_pm_to': 'thu_pm_to',
        'tue_am_from': 'tue_am_from',
        'tue_am_to': 'tue_am_to',
        'tue_pm_from': 'tue_pm_from',
        'tue_pm_to': 'tue_pm_to',
        'wed_am_from': 'wed_am_from',
        'wed_am_to': 'wed_am_to',
        'wed_pm_from': 'wed_pm_from',
        'wed_pm_to': 'wed_pm_To'
    }

    def __init__(self, fri_am_from=None, fri_am_to=None, fri_pm_from=None, fri_pm_to=None, mon_am_from=None, mon_am_to=None, mon_pm_from=None, mon_pm_to=None, ph_additional_text=None, ph_from=None, ph_to=None, sat_am_from=None, sat_am_to=None, sat_pm_from=None, sat_pm_to=None, sun_am_from=None, sun_am_to=None, sun_pm_from=None, sun_pm_to=None, thu_am_from=None, thu_am_to=None, thu_pm_from=None, thu_pm_to=None, tue_am_from=None, tue_am_to=None, tue_pm_from=None, tue_pm_to=None, wed_am_from=None, wed_am_to=None, wed_pm_from=None, wed_pm_to=None):  # noqa: E501
        """V3StopStaffing - a model defined in Swagger"""  # noqa: E501

        self._fri_am_from = None
        self._fri_am_to = None
        self._fri_pm_from = None
        self._fri_pm_to = None
        self._mon_am_from = None
        self._mon_am_to = None
        self._mon_pm_from = None
        self._mon_pm_to = None
        self._ph_additional_text = None
        self._ph_from = None
        self._ph_to = None
        self._sat_am_from = None
        self._sat_am_to = None
        self._sat_pm_from = None
        self._sat_pm_to = None
        self._sun_am_from = None
        self._sun_am_to = None
        self._sun_pm_from = None
        self._sun_pm_to = None
        self._thu_am_from = None
        self._thu_am_to = None
        self._thu_pm_from = None
        self._thu_pm_to = None
        self._tue_am_from = None
        self._tue_am_to = None
        self._tue_pm_from = None
        self._tue_pm_to = None
        self._wed_am_from = None
        self._wed_am_to = None
        self._wed_pm_from = None
        self._wed_pm_to = None
        self.discriminator = None

        if fri_am_from is not None:
            self.fri_am_from = fri_am_from
        if fri_am_to is not None:
            self.fri_am_to = fri_am_to
        if fri_pm_from is not None:
            self.fri_pm_from = fri_pm_from
        if fri_pm_to is not None:
            self.fri_pm_to = fri_pm_to
        if mon_am_from is not None:
            self.mon_am_from = mon_am_from
        if mon_am_to is not None:
            self.mon_am_to = mon_am_to
        if mon_pm_from is not None:
            self.mon_pm_from = mon_pm_from
        if mon_pm_to is not None:
            self.mon_pm_to = mon_pm_to
        if ph_additional_text is not None:
            self.ph_additional_text = ph_additional_text
        if ph_from is not None:
            self.ph_from = ph_from
        if ph_to is not None:
            self.ph_to = ph_to
        if sat_am_from is not None:
            self.sat_am_from = sat_am_from
        if sat_am_to is not None:
            self.sat_am_to = sat_am_to
        if sat_pm_from is not None:
            self.sat_pm_from = sat_pm_from
        if sat_pm_to is not None:
            self.sat_pm_to = sat_pm_to
        if sun_am_from is not None:
            self.sun_am_from = sun_am_from
        if sun_am_to is not None:
            self.sun_am_to = sun_am_to
        if sun_pm_from is not None:
            self.sun_pm_from = sun_pm_from
        if sun_pm_to is not None:
            self.sun_pm_to = sun_pm_to
        if thu_am_from is not None:
            self.thu_am_from = thu_am_from
        if thu_am_to is not None:
            self.thu_am_to = thu_am_to
        if thu_pm_from is not None:
            self.thu_pm_from = thu_pm_from
        if thu_pm_to is not None:
            self.thu_pm_to = thu_pm_to
        if tue_am_from is not None:
            self.tue_am_from = tue_am_from
        if tue_am_to is not None:
            self.tue_am_to = tue_am_to
        if tue_pm_from is not None:
            self.tue_pm_from = tue_pm_from
        if tue_pm_to is not None:
            self.tue_pm_to = tue_pm_to
        if wed_am_from is not None:
            self.wed_am_from = wed_am_from
        if wed_am_to is not None:
            self.wed_am_to = wed_am_to
        if wed_pm_from is not None:
            self.wed_pm_from = wed_pm_from
        if wed_pm_to is not None:
            self.wed_pm_to = wed_pm_to

    @property
    def fri_am_from(self):
        """Gets the fri_am_from of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The fri_am_from of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._fri_am_from

    @fri_am_from.setter
    def fri_am_from(self, fri_am_from):
        """Sets the fri_am_from of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param fri_am_from: The fri_am_from of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._fri_am_from = fri_am_from

    @property
    def fri_am_to(self):
        """Gets the fri_am_to of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The fri_am_to of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._fri_am_to

    @fri_am_to.setter
    def fri_am_to(self, fri_am_to):
        """Sets the fri_am_to of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param fri_am_to: The fri_am_to of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._fri_am_to = fri_am_to

    @property
    def fri_pm_from(self):
        """Gets the fri_pm_from of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The fri_pm_from of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._fri_pm_from

    @fri_pm_from.setter
    def fri_pm_from(self, fri_pm_from):
        """Sets the fri_pm_from of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param fri_pm_from: The fri_pm_from of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._fri_pm_from = fri_pm_from

    @property
    def fri_pm_to(self):
        """Gets the fri_pm_to of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The fri_pm_to of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._fri_pm_to

    @fri_pm_to.setter
    def fri_pm_to(self, fri_pm_to):
        """Sets the fri_pm_to of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param fri_pm_to: The fri_pm_to of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._fri_pm_to = fri_pm_to

    @property
    def mon_am_from(self):
        """Gets the mon_am_from of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The mon_am_from of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._mon_am_from

    @mon_am_from.setter
    def mon_am_from(self, mon_am_from):
        """Sets the mon_am_from of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param mon_am_from: The mon_am_from of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._mon_am_from = mon_am_from

    @property
    def mon_am_to(self):
        """Gets the mon_am_to of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The mon_am_to of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._mon_am_to

    @mon_am_to.setter
    def mon_am_to(self, mon_am_to):
        """Sets the mon_am_to of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param mon_am_to: The mon_am_to of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._mon_am_to = mon_am_to

    @property
    def mon_pm_from(self):
        """Gets the mon_pm_from of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The mon_pm_from of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._mon_pm_from

    @mon_pm_from.setter
    def mon_pm_from(self, mon_pm_from):
        """Sets the mon_pm_from of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param mon_pm_from: The mon_pm_from of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._mon_pm_from = mon_pm_from

    @property
    def mon_pm_to(self):
        """Gets the mon_pm_to of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The mon_pm_to of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._mon_pm_to

    @mon_pm_to.setter
    def mon_pm_to(self, mon_pm_to):
        """Sets the mon_pm_to of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param mon_pm_to: The mon_pm_to of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._mon_pm_to = mon_pm_to

    @property
    def ph_additional_text(self):
        """Gets the ph_additional_text of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The ph_additional_text of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._ph_additional_text

    @ph_additional_text.setter
    def ph_additional_text(self, ph_additional_text):
        """Sets the ph_additional_text of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param ph_additional_text: The ph_additional_text of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._ph_additional_text = ph_additional_text

    @property
    def ph_from(self):
        """Gets the ph_from of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The ph_from of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._ph_from

    @ph_from.setter
    def ph_from(self, ph_from):
        """Sets the ph_from of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param ph_from: The ph_from of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._ph_from = ph_from

    @property
    def ph_to(self):
        """Gets the ph_to of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The ph_to of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._ph_to

    @ph_to.setter
    def ph_to(self, ph_to):
        """Sets the ph_to of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param ph_to: The ph_to of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._ph_to = ph_to

    @property
    def sat_am_from(self):
        """Gets the sat_am_from of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The sat_am_from of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._sat_am_from

    @sat_am_from.setter
    def sat_am_from(self, sat_am_from):
        """Sets the sat_am_from of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param sat_am_from: The sat_am_from of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._sat_am_from = sat_am_from

    @property
    def sat_am_to(self):
        """Gets the sat_am_to of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The sat_am_to of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._sat_am_to

    @sat_am_to.setter
    def sat_am_to(self, sat_am_to):
        """Sets the sat_am_to of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param sat_am_to: The sat_am_to of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._sat_am_to = sat_am_to

    @property
    def sat_pm_from(self):
        """Gets the sat_pm_from of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The sat_pm_from of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._sat_pm_from

    @sat_pm_from.setter
    def sat_pm_from(self, sat_pm_from):
        """Sets the sat_pm_from of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param sat_pm_from: The sat_pm_from of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._sat_pm_from = sat_pm_from

    @property
    def sat_pm_to(self):
        """Gets the sat_pm_to of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The sat_pm_to of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._sat_pm_to

    @sat_pm_to.setter
    def sat_pm_to(self, sat_pm_to):
        """Sets the sat_pm_to of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param sat_pm_to: The sat_pm_to of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._sat_pm_to = sat_pm_to

    @property
    def sun_am_from(self):
        """Gets the sun_am_from of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The sun_am_from of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._sun_am_from

    @sun_am_from.setter
    def sun_am_from(self, sun_am_from):
        """Sets the sun_am_from of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param sun_am_from: The sun_am_from of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._sun_am_from = sun_am_from

    @property
    def sun_am_to(self):
        """Gets the sun_am_to of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The sun_am_to of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._sun_am_to

    @sun_am_to.setter
    def sun_am_to(self, sun_am_to):
        """Sets the sun_am_to of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param sun_am_to: The sun_am_to of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._sun_am_to = sun_am_to

    @property
    def sun_pm_from(self):
        """Gets the sun_pm_from of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The sun_pm_from of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._sun_pm_from

    @sun_pm_from.setter
    def sun_pm_from(self, sun_pm_from):
        """Sets the sun_pm_from of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param sun_pm_from: The sun_pm_from of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._sun_pm_from = sun_pm_from

    @property
    def sun_pm_to(self):
        """Gets the sun_pm_to of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The sun_pm_to of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._sun_pm_to

    @sun_pm_to.setter
    def sun_pm_to(self, sun_pm_to):
        """Sets the sun_pm_to of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param sun_pm_to: The sun_pm_to of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._sun_pm_to = sun_pm_to

    @property
    def thu_am_from(self):
        """Gets the thu_am_from of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The thu_am_from of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._thu_am_from

    @thu_am_from.setter
    def thu_am_from(self, thu_am_from):
        """Sets the thu_am_from of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param thu_am_from: The thu_am_from of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._thu_am_from = thu_am_from

    @property
    def thu_am_to(self):
        """Gets the thu_am_to of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The thu_am_to of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._thu_am_to

    @thu_am_to.setter
    def thu_am_to(self, thu_am_to):
        """Sets the thu_am_to of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param thu_am_to: The thu_am_to of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._thu_am_to = thu_am_to

    @property
    def thu_pm_from(self):
        """Gets the thu_pm_from of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The thu_pm_from of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._thu_pm_from

    @thu_pm_from.setter
    def thu_pm_from(self, thu_pm_from):
        """Sets the thu_pm_from of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param thu_pm_from: The thu_pm_from of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._thu_pm_from = thu_pm_from

    @property
    def thu_pm_to(self):
        """Gets the thu_pm_to of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The thu_pm_to of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._thu_pm_to

    @thu_pm_to.setter
    def thu_pm_to(self, thu_pm_to):
        """Sets the thu_pm_to of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param thu_pm_to: The thu_pm_to of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._thu_pm_to = thu_pm_to

    @property
    def tue_am_from(self):
        """Gets the tue_am_from of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The tue_am_from of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._tue_am_from

    @tue_am_from.setter
    def tue_am_from(self, tue_am_from):
        """Sets the tue_am_from of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param tue_am_from: The tue_am_from of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._tue_am_from = tue_am_from

    @property
    def tue_am_to(self):
        """Gets the tue_am_to of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The tue_am_to of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._tue_am_to

    @tue_am_to.setter
    def tue_am_to(self, tue_am_to):
        """Sets the tue_am_to of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param tue_am_to: The tue_am_to of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._tue_am_to = tue_am_to

    @property
    def tue_pm_from(self):
        """Gets the tue_pm_from of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The tue_pm_from of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._tue_pm_from

    @tue_pm_from.setter
    def tue_pm_from(self, tue_pm_from):
        """Sets the tue_pm_from of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param tue_pm_from: The tue_pm_from of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._tue_pm_from = tue_pm_from

    @property
    def tue_pm_to(self):
        """Gets the tue_pm_to of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The tue_pm_to of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._tue_pm_to

    @tue_pm_to.setter
    def tue_pm_to(self, tue_pm_to):
        """Sets the tue_pm_to of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param tue_pm_to: The tue_pm_to of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._tue_pm_to = tue_pm_to

    @property
    def wed_am_from(self):
        """Gets the wed_am_from of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The wed_am_from of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._wed_am_from

    @wed_am_from.setter
    def wed_am_from(self, wed_am_from):
        """Sets the wed_am_from of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param wed_am_from: The wed_am_from of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._wed_am_from = wed_am_from

    @property
    def wed_am_to(self):
        """Gets the wed_am_to of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The wed_am_to of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._wed_am_to

    @wed_am_to.setter
    def wed_am_to(self, wed_am_to):
        """Sets the wed_am_to of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param wed_am_to: The wed_am_to of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._wed_am_to = wed_am_to

    @property
    def wed_pm_from(self):
        """Gets the wed_pm_from of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The wed_pm_from of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._wed_pm_from

    @wed_pm_from.setter
    def wed_pm_from(self, wed_pm_from):
        """Sets the wed_pm_from of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param wed_pm_from: The wed_pm_from of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._wed_pm_from = wed_pm_from

    @property
    def wed_pm_to(self):
        """Gets the wed_pm_to of this V3StopStaffing.  # noqa: E501

        Stop staffing hours  # noqa: E501

        :return: The wed_pm_to of this V3StopStaffing.  # noqa: E501
        :rtype: str
        """
        return self._wed_pm_to

    @wed_pm_to.setter
    def wed_pm_to(self, wed_pm_to):
        """Sets the wed_pm_to of this V3StopStaffing.

        Stop staffing hours  # noqa: E501

        :param wed_pm_to: The wed_pm_to of this V3StopStaffing.  # noqa: E501
        :type: str
        """

        self._wed_pm_to = wed_pm_to

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
        if issubclass(V3StopStaffing, dict):
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
        if not isinstance(other, V3StopStaffing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
