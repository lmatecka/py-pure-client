# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.37
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_37 import models

class FleetMember(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'fleet': 'FixedReferenceWithTypeAndLocation',
        'member': 'FixedReferenceWithTypeAndLocation',
        'status': 'str',
        'status_details': 'str'
    }

    attribute_map = {
        'fleet': 'fleet',
        'member': 'member',
        'status': 'status',
        'status_details': 'status_details'
    }

    required_args = {
    }

    def __init__(
        self,
        fleet=None,  # type: models.FixedReferenceWithTypeAndLocation
        member=None,  # type: models.FixedReferenceWithTypeAndLocation
        status=None,  # type: str
        status_details=None,  # type: str
    ):
        """
        Keyword args:
            fleet (FixedReferenceWithTypeAndLocation)
            member (FixedReferenceWithTypeAndLocation)
            status (str): Current fleet membership status Valid values are one of: `joining`, `joined`, or `removing` A status of `joining` indicates that the member is attempting to join the fleet. A status of `joined` indicates that the member has joined the fleet. A status of `removing` indicates that the member is being removed from the fleet.
            status_details (str): Describes the error, if any.
        """
        if fleet is not None:
            self.fleet = fleet
        if member is not None:
            self.member = member
        if status is not None:
            self.status = status
        if status_details is not None:
            self.status_details = status_details

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `FleetMember`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `FleetMember`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `FleetMember`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `FleetMember`".format(key))
        object.__delattr__(self, key)

    def keys(self):
        return self.attribute_map.keys()

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
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
        if issubclass(FleetMember, dict):
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
        if not isinstance(other, FleetMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
