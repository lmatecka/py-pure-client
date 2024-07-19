# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_8 import models

class ProtectionGroupSnapshotPatch(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'created': 'int',
        'destroyed': 'bool',
        'pod': 'FixedReference',
        'source': 'FixedReference',
        'space': 'Space',
        'suffix': 'str',
        'time_remaining': 'int'
    }

    attribute_map = {
        'name': 'name',
        'created': 'created',
        'destroyed': 'destroyed',
        'pod': 'pod',
        'source': 'source',
        'space': 'space',
        'suffix': 'suffix',
        'time_remaining': 'time_remaining'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        created=None,  # type: int
        destroyed=None,  # type: bool
        pod=None,  # type: models.FixedReference
        source=None,  # type: models.FixedReference
        space=None,  # type: models.Space
        suffix=None,  # type: str
        time_remaining=None,  # type: int
    ):
        """
        Keyword args:
            name (str): A user-specified name. The name must be locally unique and can be changed.
            created (int): The snapshot creation time of the original snapshot source. Measured in milliseconds since the UNIX epoch.
            destroyed (bool): Returns a value of `true` if the protection group snapshot has been destroyed and is pending eradication. The `time_remaining` value displays the amount of time left until the destroyed snapshot is permanently eradicated. Before the `time_remaining` period has elapsed, the destroyed snapshot can be recovered by setting `destroyed=false`. Once the `time_remaining` period has elapsed, the snapshot is permanently eradicated and can no longer be recovered.
            pod (FixedReference): The pod in which the protection group of the protection group snapshot resides.
            source (FixedReference): The original protection group from which this snapshot was taken. For a replicated protection group snapshot being viewed on the target side, the `source` is the replica protection group.
            space (Space): Returns provisioned size and physical storage consumption data for each protection group.
            suffix (str)
            time_remaining (int): The amount of time left until the destroyed snapshot is permanently eradicated. Measured in milliseconds. Before the `time_remaining` period has elapsed, the destroyed snapshot can be recovered by setting `destroyed=false`.
        """
        if name is not None:
            self.name = name
        if created is not None:
            self.created = created
        if destroyed is not None:
            self.destroyed = destroyed
        if pod is not None:
            self.pod = pod
        if source is not None:
            self.source = source
        if space is not None:
            self.space = space
        if suffix is not None:
            self.suffix = suffix
        if time_remaining is not None:
            self.time_remaining = time_remaining

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ProtectionGroupSnapshotPatch`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ProtectionGroupSnapshotPatch`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ProtectionGroupSnapshotPatch`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ProtectionGroupSnapshotPatch`".format(key))
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
        if issubclass(ProtectionGroupSnapshotPatch, dict):
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
        if not isinstance(other, ProtectionGroupSnapshotPatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
