# this file is @generated
import typing as t

from ..serialization import StrEnum


class TopUpCollection(StrEnum):
    """How a top-up is paid: CHARGE a saved payment method now, or SEND_INVOICE and grant the credit
    once the invoice is paid."""

    CHARGE = "CHARGE"
    SEND_INVOICE = "SEND_INVOICE"


TopUpCollectionLiteral: t.TypeAlias = t.Literal["CHARGE", "SEND_INVOICE"]
"""The values of :class:`TopUpCollection`, which arguments take as plain strings too."""
