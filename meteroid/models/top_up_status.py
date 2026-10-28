# this file is @generated
import typing as t

from ..serialization import StrEnum


class TopUpStatus(StrEnum):
    """The values of `TopUpStatus`; others are kept as received."""

    SUCCEEDED = "SUCCEEDED"
    PENDING = "PENDING"
    REQUIRES_CUSTOMER_ACTION = "REQUIRES_CUSTOMER_ACTION"
    AWAITING_PAYMENT = "AWAITING_PAYMENT"


TopUpStatusLiteral: t.TypeAlias = t.Literal[
    "SUCCEEDED", "PENDING", "REQUIRES_CUSTOMER_ACTION", "AWAITING_PAYMENT"
]
"""The values of :class:`TopUpStatus`, which arguments take as plain strings too."""
