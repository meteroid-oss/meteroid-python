# this file is @generated
import typing as t

from ..serialization import StrEnum


class CreditExpiryUnit(StrEnum):
    """The values of `CreditExpiryUnit`; others are kept as received."""

    DAY = "DAY"
    MONTH = "MONTH"
    BILLING_PERIOD = "BILLING_PERIOD"


CreditExpiryUnitLiteral: t.TypeAlias = t.Literal["DAY", "MONTH", "BILLING_PERIOD"]
"""The values of :class:`CreditExpiryUnit`, which arguments take as plain strings too."""
