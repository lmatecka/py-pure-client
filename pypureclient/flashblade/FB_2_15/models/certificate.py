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

class Certificate(object):
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
        'certificate': 'str',
        'certificate_type': 'str',
        'common_name': 'str',
        'country': 'str',
        'email': 'str',
        'intermediate_certificate': 'str',
        'issued_by': 'str',
        'issued_to': 'str',
        'key_size': 'int',
        'locality': 'str',
        'organization': 'str',
        'organizational_unit': 'str',
        'state': 'str',
        'status': 'str',
        'subject_alternative_names': 'list[str]',
        'valid_from': 'str',
        'valid_to': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'certificate': 'certificate',
        'certificate_type': 'certificate_type',
        'common_name': 'common_name',
        'country': 'country',
        'email': 'email',
        'intermediate_certificate': 'intermediate_certificate',
        'issued_by': 'issued_by',
        'issued_to': 'issued_to',
        'key_size': 'key_size',
        'locality': 'locality',
        'organization': 'organization',
        'organizational_unit': 'organizational_unit',
        'state': 'state',
        'status': 'status',
        'subject_alternative_names': 'subject_alternative_names',
        'valid_from': 'valid_from',
        'valid_to': 'valid_to'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        certificate=None,  # type: str
        certificate_type=None,  # type: str
        common_name=None,  # type: str
        country=None,  # type: str
        email=None,  # type: str
        intermediate_certificate=None,  # type: str
        issued_by=None,  # type: str
        issued_to=None,  # type: str
        key_size=None,  # type: int
        locality=None,  # type: str
        organization=None,  # type: str
        organizational_unit=None,  # type: str
        state=None,  # type: str
        status=None,  # type: str
        subject_alternative_names=None,  # type: List[str]
        valid_from=None,  # type: str
        valid_to=None,  # type: str
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            certificate (str): The text of the certificate.
            certificate_type (str): The type of certificate. Possible values are `appliance` and `external`. Certificates of type `appliance` are used by the array to verify its identity to clients. Certificates of type `external` are used by the array to identify external servers to which it is configured to communicate.
            common_name (str): FQDN or management IP address of the current array.
            country (str): The country field listed in the certificate.
            email (str): The email field listed in the certificate.
            intermediate_certificate (str): Intermediate certificate chains.
            issued_by (str): Who issued this certificate.
            issued_to (str): Who this certificate was issued to.
            key_size (int): The size of the private key for this certificate in bits.
            locality (str): The locality field listed in the certificate.
            organization (str): The organization field listed in the certificate.
            organizational_unit (str): The organizational unit field listed in the certificate.
            state (str): The state/province field listed in the certificate.
            status (str): The type of certificate. Valid values are `self-signed` and `imported`.
            subject_alternative_names (list[str]): The alternative names that are secured by this certificate. Alternative names may be IP addresses, DNS names, or URIs.
            valid_from (str): The start date of when this certificate is valid.
            valid_to (str): The end date of when this certificate is valid.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if certificate is not None:
            self.certificate = certificate
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if common_name is not None:
            self.common_name = common_name
        if country is not None:
            self.country = country
        if email is not None:
            self.email = email
        if intermediate_certificate is not None:
            self.intermediate_certificate = intermediate_certificate
        if issued_by is not None:
            self.issued_by = issued_by
        if issued_to is not None:
            self.issued_to = issued_to
        if key_size is not None:
            self.key_size = key_size
        if locality is not None:
            self.locality = locality
        if organization is not None:
            self.organization = organization
        if organizational_unit is not None:
            self.organizational_unit = organizational_unit
        if state is not None:
            self.state = state
        if status is not None:
            self.status = status
        if subject_alternative_names is not None:
            self.subject_alternative_names = subject_alternative_names
        if valid_from is not None:
            self.valid_from = valid_from
        if valid_to is not None:
            self.valid_to = valid_to

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Certificate`".format(key))
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
        if issubclass(Certificate, dict):
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
        if not isinstance(other, Certificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
