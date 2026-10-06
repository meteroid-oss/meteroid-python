# this file is @generated
import typing as t

from ..serialization import StrEnum


class ReversalKind(StrEnum):
    """Why a payment was involuntarily clawed back."""

    REFUND = "REFUND"
    CHARGEBACK = "CHARGEBACK"
    DEBTOR_RECALL = "DEBTOR_RECALL"
    INSUFFICIENT_FUNDS = "INSUFFICIENT_FUNDS"
    MANDATE_INVALID = "MANDATE_INVALID"
    RETURNED = "RETURNED"
    DISPUTE = "DISPUTE"
    OTHER = "OTHER"


ReversalKindLiteral: t.TypeAlias = t.Literal[
    "REFUND",
    "CHARGEBACK",
    "DEBTOR_RECALL",
    "INSUFFICIENT_FUNDS",
    "MANDATE_INVALID",
    "RETURNED",
    "DISPUTE",
    "OTHER",
]
"""The values of :class:`ReversalKind`, which arguments take as plain strings too."""
