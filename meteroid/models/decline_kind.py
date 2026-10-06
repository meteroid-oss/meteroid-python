# this file is @generated
import typing as t

from ..serialization import StrEnum


class DeclineKind(StrEnum):
    """Why the payment provider declined a charge."""

    INSUFFICIENT_FUNDS = "INSUFFICIENT_FUNDS"
    DO_NOT_HONOR = "DO_NOT_HONOR"
    CARD_EXPIRED = "CARD_EXPIRED"
    AUTHENTICATION_REQUIRED = "AUTHENTICATION_REQUIRED"
    MANDATE_INACTIVE = "MANDATE_INACTIVE"
    FRAUD = "FRAUD"
    PROCESSING_ERROR = "PROCESSING_ERROR"
    OTHER = "OTHER"


DeclineKindLiteral: t.TypeAlias = t.Literal[
    "INSUFFICIENT_FUNDS",
    "DO_NOT_HONOR",
    "CARD_EXPIRED",
    "AUTHENTICATION_REQUIRED",
    "MANDATE_INACTIVE",
    "FRAUD",
    "PROCESSING_ERROR",
    "OTHER",
]
"""The values of :class:`DeclineKind`, which arguments take as plain strings too."""
