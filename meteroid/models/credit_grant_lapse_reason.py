# this file is @generated
import typing as t

from ..serialization import StrEnum


class CreditGrantLapseReason(StrEnum):
    """Why a credit grant's unspent credit lapsed."""

    EXPIRED = "EXPIRED"
    SUBSCRIPTION_ENDED = "SUBSCRIPTION_ENDED"


CreditGrantLapseReasonLiteral: t.TypeAlias = t.Literal["EXPIRED", "SUBSCRIPTION_ENDED"]
"""The values of :class:`CreditGrantLapseReason`, which arguments take as plain strings too."""
