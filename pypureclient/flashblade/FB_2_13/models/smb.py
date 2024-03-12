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

class Smb(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enabled': 'bool',
        'client_policy': 'ReferenceWritable',
        'share_policy': 'ReferenceWritable',
        'continuous_availability_enabled': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'client_policy': 'client_policy',
        'share_policy': 'share_policy',
        'continuous_availability_enabled': 'continuous_availability_enabled'
    }

    required_args = {
    }

    def __init__(
        self,
        enabled=None,  # type: bool
        client_policy=None,  # type: models.ReferenceWritable
        share_policy=None,  # type: models.ReferenceWritable
        continuous_availability_enabled=None,  # type: bool
    ):
        """
        Keyword args:
            enabled (bool): If set to `true`, enables access to the file system over the SMB protocol. If not specified, defaults to `false`.
            client_policy (ReferenceWritable): The SMB Client policy for the file system. Setting a policy here grants access permissions (e.g. read-only or read-write) to the file system via SMB on a per-client basis. If no policy is set here, no client will have access. Use \"\" to clear.
            share_policy (ReferenceWritable): The SMB Share policy for the file system. Setting a policy here grants access permissions (e.g. allow or deny Full Control, Change, and/or Read) to the file system via SMB on a per-user / per-group basis. If no policy is set here, no user or group will have access. Use \"\" to clear.
            continuous_availability_enabled (bool): If set to `true`, the file system will be continuously available during disruptive scenarios such as network disruption, blades failover, etc. If not specified, defaults to `true`.
        """
        if enabled is not None:
            self.enabled = enabled
        if client_policy is not None:
            self.client_policy = client_policy
        if share_policy is not None:
            self.share_policy = share_policy
        if continuous_availability_enabled is not None:
            self.continuous_availability_enabled = continuous_availability_enabled

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Smb`".format(key))
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
        if issubclass(Smb, dict):
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
        if not isinstance(other, Smb):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
