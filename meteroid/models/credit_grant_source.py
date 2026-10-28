# this file is @generated
import typing as t

from ..serialization import StrEnum


class CreditGrantSource(StrEnum):
    """The values of `CreditGrantSource`; others are kept as received."""

    MANUAL = "MANUAL"
    PURCHASE = "PURCHASE"
    PLAN = "PLAN"
    CREDIT_NOTE = "CREDIT_NOTE"
    ADJUSTMENT = "ADJUSTMENT"
    MIGRATED = "MIGRATED"
    ROLLOVER = "ROLLOVER"
    COUPON = "COUPON"
    OVERPAYMENT = "OVERPAYMENT"


CreditGrantSourceLiteral: t.TypeAlias = t.Literal[
    "MANUAL",
    "PURCHASE",
    "PLAN",
    "CREDIT_NOTE",
    "ADJUSTMENT",
    "MIGRATED",
    "ROLLOVER",
    "COUPON",
    "OVERPAYMENT",
]
"""The values of :class:`CreditGrantSource`, which arguments take as plain strings too."""
