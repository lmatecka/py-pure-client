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

class NetworkAccessPolicyRule(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'client': 'str',
        'effect': 'str',
        'interfaces': 'list[str]',
        'policy': 'FixedReference',
        'policy_version': 'str',
        'index': 'int'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'client': 'client',
        'effect': 'effect',
        'interfaces': 'interfaces',
        'policy': 'policy',
        'policy_version': 'policy_version',
        'index': 'index'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        client=None,  # type: str
        effect=None,  # type: str
        interfaces=None,  # type: List[str]
        policy=None,  # type: models.FixedReference
        policy_version=None,  # type: str
        index=None,  # type: int
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            client (str): Specifies the clients that will be permitted or denied access to the interface. Accepted notations include a single IP address, subnet in CIDR notation, or all clients (specified as `*`). The default value is `*` if not specified.
            effect (str): If set to `allow`, the specified client will be permitted to access the specified interfaces. If set to `deny`, the specified client will be denied access to them. Valid values include `allow` and `deny`.
            interfaces (list[str]): Specifies which product interfaces this rule applies to, whether it is permitting or denying access. Valid values include `management-ssh`, `management-rest-api`, `management-web-ui`, `snmp`, and `local-network-superuser-password-access`.
            policy (FixedReference): The policy to which this rule belongs.
            policy_version (str): The policy's version. This can be used when updating the resource to ensure there aren't any updates to the policy since the resource was read.
            index (int): The index within the policy. The `index` indicates the order the rules are evaluated. NOTE: It is recommended to use the query param `before_rule_id` to do reordering to avoid concurrency issues, but changing `index` is also supported. `index` can not be changed if `before_rule_id` or `before_rule_name` are specified.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if client is not None:
            self.client = client
        if effect is not None:
            self.effect = effect
        if interfaces is not None:
            self.interfaces = interfaces
        if policy is not None:
            self.policy = policy
        if policy_version is not None:
            self.policy_version = policy_version
        if index is not None:
            self.index = index

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `NetworkAccessPolicyRule`".format(key))
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
        if issubclass(NetworkAccessPolicyRule, dict):
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
        if not isinstance(other, NetworkAccessPolicyRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
