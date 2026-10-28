# this file is @generated
import typing as t

from ..serialization import StrEnum


class CreditAppliesTo(StrEnum):
    """Which charges credit pays: ALL pays any part of an invoice, USAGE only its usage charges."""

    ALL = "ALL"
    USAGE = "USAGE"


CreditAppliesToLiteral: t.TypeAlias = t.Literal["ALL", "USAGE"]
"""The values of :class:`CreditAppliesTo`, which arguments take as plain strings too."""
