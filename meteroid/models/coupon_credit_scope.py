# this file is @generated
import typing as t

from ..serialization import StrEnum


class CouponCreditScope(StrEnum):
    """Which subscriptions a promotional credit coupon's credit pays."""

    CUSTOMER = "CUSTOMER"
    SUBSCRIPTION = "SUBSCRIPTION"


CouponCreditScopeLiteral: t.TypeAlias = t.Literal["CUSTOMER", "SUBSCRIPTION"]
"""The values of :class:`CouponCreditScope`, which arguments take as plain strings too."""
