# this file is @generated
import typing as t

from ..serialization import StrEnum


class CreditGrantStatus(StrEnum):
    """The values of `CreditGrantStatus`; others are kept as received."""

    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    DEPLETED = "DEPLETED"
    EXPIRED = "EXPIRED"


CreditGrantStatusLiteral: t.TypeAlias = t.Literal[
    "PENDING", "ACTIVE", "DEPLETED", "EXPIRED"
]
"""The values of :class:`CreditGrantStatus`, which arguments take as plain strings too."""
