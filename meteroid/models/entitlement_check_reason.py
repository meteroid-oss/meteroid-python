# this file is @generated
import typing as t

from ..serialization import StrEnum


class EntitlementCheckReason(StrEnum):
    """The values of `EntitlementCheckReason`; others are kept as received."""

    WITHIN_LIMIT = "WITHIN_LIMIT"
    LIMIT_REACHED = "LIMIT_REACHED"
    NO_ENTITLEMENT = "NO_ENTITLEMENT"
    DISABLED = "DISABLED"
    BUDGET_EXCEEDED = "BUDGET_EXCEEDED"
    INSUFFICIENT_BALANCE = "INSUFFICIENT_BALANCE"
    TOO_MANY_GROUPS = "TOO_MANY_GROUPS"


EntitlementCheckReasonLiteral: t.TypeAlias = t.Literal[
    "WITHIN_LIMIT",
    "LIMIT_REACHED",
    "NO_ENTITLEMENT",
    "DISABLED",
    "BUDGET_EXCEEDED",
    "INSUFFICIENT_BALANCE",
    "TOO_MANY_GROUPS",
]
"""The values of :class:`EntitlementCheckReason`, which arguments take as plain strings too."""
