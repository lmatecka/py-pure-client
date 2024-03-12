# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.13, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_13 import models

class ApiToken(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'created_at': 'int',
        'expires_at': 'int',
        'token': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'expires_at': 'expires_at',
        'token': 'token'
    }

    required_args = {
    }

    def __init__(
        self,
        created_at=None,  # type: int
        expires_at=None,  # type: int
        token=None,  # type: str
    ):
        """
        Keyword args:
            created_at (int): Creation time in milliseconds since the UNIX epoch.
            expires_at (int): Expiration time in milliseconds since the UNIX epoch.
            token (str): An Admin API token. A newly-created token is visible as the result of the POST operation which created it. An existing token is visible when `expose_api_token` is `true` and it is being requested by the user to whom it belongs. In all other cases, the token will be masked.
        """
        if created_at is not None:
            self.created_at = created_at
        if expires_at is not None:
            self.expires_at = expires_at
        if token is not None:
            self.token = token

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ApiToken`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            return None
        else:
            return value

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
        if issubclass(ApiToken, dict):
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
        if not isinstance(other, ApiToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
