# this file is @generated
import typing as t

from ..serialization import StrEnum


class ActorType(StrEnum):
    """The values of `ActorType`; others are kept as received."""

    USER = "USER"
    CUSTOMER = "CUSTOMER"
    SYSTEM = "SYSTEM"
    API_KEY = "API_KEY"
    OAUTH_APP = "OAUTH_APP"


ActorTypeLiteral: t.TypeAlias = t.Literal[
    "USER", "CUSTOMER", "SYSTEM", "API_KEY", "OAUTH_APP"
]
"""The values of :class:`ActorType`, which arguments take as plain strings too."""
