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

class VolumeBatchPost(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'destroyed': 'bool',
        'priority_adjustment': 'PriorityAdjustment',
        'provisioned': 'int',
        'qos': 'Qos',
        'source': 'Reference',
        'subtype': 'str',
        'protocol_endpoint': 'ProtocolEndpoint',
        'add_to_protection_groups': 'list[Reference]',
        'name': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'destroyed': 'destroyed',
        'priority_adjustment': 'priority_adjustment',
        'provisioned': 'provisioned',
        'qos': 'qos',
        'source': 'source',
        'subtype': 'subtype',
        'protocol_endpoint': 'protocol_endpoint',
        'add_to_protection_groups': 'add_to_protection_groups',
        'name': 'name',
        'tags': 'tags'
    }

    required_args = {
    }

    def __init__(
        self,
        destroyed=None,  # type: bool
        priority_adjustment=None,  # type: models.PriorityAdjustment
        provisioned=None,  # type: int
        qos=None,  # type: models.Qos
        source=None,  # type: models.Reference
        subtype=None,  # type: str
        protocol_endpoint=None,  # type: models.ProtocolEndpoint
        add_to_protection_groups=None,  # type: List[models.Reference]
        name=None,  # type: str
        tags=None,  # type: List[models.Tag]
    ):
        """
        Keyword args:
            destroyed (bool): If set to `true`, destroys a resource. Once set to `true`, the `time_remaining` value will display the amount of time left until the destroyed resource is permanently eradicated. Before the `time_remaining` period has elapsed, the destroyed resource can be recovered by setting `destroyed=false`. Once the `time_remaining` period has elapsed, the resource is permanently eradicated and can no longer be recovered.
            priority_adjustment (PriorityAdjustment): Adjusts volume priority.
            provisioned (int): Sets the virtual size of the volume, measured in bytes.
            qos (Qos): Sets QoS limits.
            source (Reference): The source volume of a volume copy.
            subtype (str): The type of volume. Valid values are `protocol_endpoint` and `regular`.
            protocol_endpoint (ProtocolEndpoint): Sets the properties that are specific to protocol endpoints. This can only be used in conjunction to `subtype=protocol_endpoint`.
            add_to_protection_groups (list[Reference]): Specifies a list of protection groups that will protect the volume.
            name (str): Specifies the name of the volume.
            tags (list[Tag]): Specifies the list of tags to be upserted on this volume.
        """
        if destroyed is not None:
            self.destroyed = destroyed
        if priority_adjustment is not None:
            self.priority_adjustment = priority_adjustment
        if provisioned is not None:
            self.provisioned = provisioned
        if qos is not None:
            self.qos = qos
        if source is not None:
            self.source = source
        if subtype is not None:
            self.subtype = subtype
        if protocol_endpoint is not None:
            self.protocol_endpoint = protocol_endpoint
        if add_to_protection_groups is not None:
            self.add_to_protection_groups = add_to_protection_groups
        if name is not None:
            self.name = name
        if tags is not None:
            self.tags = tags

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VolumeBatchPost`".format(key))
        if key == "provisioned" and value is not None:
            if value > 4503599627370496:
                raise ValueError("Invalid value for `provisioned`, value must be less than or equal to `4503599627370496`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VolumeBatchPost`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VolumeBatchPost`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VolumeBatchPost`".format(key))
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
        if issubclass(VolumeBatchPost, dict):
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
        if not isinstance(other, VolumeBatchPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
