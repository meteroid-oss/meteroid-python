# this file is @generated
import typing as t

from ..serialization import StrEnum


class CreditGrantType(StrEnum):
    """PAID credit was bought, through Meteroid or outside it, and applies after tax like a payment.
    PROMOTIONAL credit was given (included with a plan, a coupon, bonus credit, a goodwill grant):
    it applies before tax, like a discount, so it is spent before paid credit. Credit-unit grants
    are drawn together, whatever their type."""

    PAID = "PAID"
    PROMOTIONAL = "PROMOTIONAL"


CreditGrantTypeLiteral: t.TypeAlias = t.Literal["PAID", "PROMOTIONAL"]
"""The values of :class:`CreditGrantType`, which arguments take as plain strings too."""
