# this file is @generated
import typing as t

from ..serialization import StrEnum


class LedgerEntryType(StrEnum):
    """The values of `LedgerEntryType`; others are kept as received."""

    CREDIT = "CREDIT"
    INVOICE_APPLICATION = "INVOICE_APPLICATION"
    INVOICE_RETURN = "INVOICE_RETURN"
    CREDIT_REVERSAL = "CREDIT_REVERSAL"
    CREDIT_REINSTATEMENT = "CREDIT_REINSTATEMENT"
    CREDIT_EXPIRY = "CREDIT_EXPIRY"
    CREDIT_ROLLOVER = "CREDIT_ROLLOVER"


LedgerEntryTypeLiteral: t.TypeAlias = t.Literal[
    "CREDIT",
    "INVOICE_APPLICATION",
    "INVOICE_RETURN",
    "CREDIT_REVERSAL",
    "CREDIT_REINSTATEMENT",
    "CREDIT_EXPIRY",
    "CREDIT_ROLLOVER",
]
"""The values of :class:`LedgerEntryType`, which arguments take as plain strings too."""
