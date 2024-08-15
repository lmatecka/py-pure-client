# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.15, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_15 import models

class WormDataPolicyRetentionConfig(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'mode': 'str',
        'min_retention': 'int',
        'max_retention': 'int',
        'default_retention': 'int',
        'retention_lock': 'str'
    }

    attribute_map = {
        'mode': 'mode',
        'min_retention': 'min_retention',
        'max_retention': 'max_retention',
        'default_retention': 'default_retention',
        'retention_lock': 'retention_lock'
    }

    required_args = {
    }

    def __init__(
        self,
        mode=None,  # type: str
        min_retention=None,  # type: int
        max_retention=None,  # type: int
        default_retention=None,  # type: int
        retention_lock=None,  # type: str
    ):
        """
        Keyword args:
            mode (str): The type of the retention lock. Valid values is `compliance`.
            min_retention (int): Minimum retention period, in milliseconds.
            max_retention (int): Maximum retention period, in milliseconds.
            default_retention (int): Default retention period, in milliseconds. If the access time is not specified when committing a file, then the default retention period is applied.
            retention_lock (str): If set to `locked`, then the value of retention attributes or policy attributes are not allowed to change. If set to `unlocked`, then the value of the retention attributes and policy attributes are allowed to change. Valid values are `unlocked` and `locked`. It is always allowed to change from `unlocked` to `locked`. Contact Pure Technical Services to change from `locked` to `unlocked`.
        """
        if mode is not None:
            self.mode = mode
        if min_retention is not None:
            self.min_retention = min_retention
        if max_retention is not None:
            self.max_retention = max_retention
        if default_retention is not None:
            self.default_retention = default_retention
        if retention_lock is not None:
            self.retention_lock = retention_lock

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `WormDataPolicyRetentionConfig`".format(key))
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
        if issubclass(WormDataPolicyRetentionConfig, dict):
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
        if not isinstance(other, WormDataPolicyRetentionConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
