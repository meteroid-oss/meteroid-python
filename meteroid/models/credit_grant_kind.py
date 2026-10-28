# this file is @generated
import typing as t

from ..serialization import StrEnum


class CreditGrantKind(StrEnum):
    """The group a grant is shown in, from where it came from and what it pays:
    - INCLUDED: credit a subscription's plan includes, which renews with it;
    - PREPAID: credit bought (purchases, top-ups, paid packs, credit paid for outside Meteroid);
    - BONUS: credit given (the bonus part of discounted credit, promo codes, welcome credit);
    - ACCOUNT_BALANCE: the customer's money that pays any invoice (credit notes, returned invoices,
      the balance carried from before credit grants, credit added for any charge)."""

    INCLUDED = "INCLUDED"
    PREPAID = "PREPAID"
    BONUS = "BONUS"
    ACCOUNT_BALANCE = "ACCOUNT_BALANCE"


CreditGrantKindLiteral: t.TypeAlias = t.Literal[
    "INCLUDED", "PREPAID", "BONUS", "ACCOUNT_BALANCE"
]
"""The values of :class:`CreditGrantKind`, which arguments take as plain strings too."""
