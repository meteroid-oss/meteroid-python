# this file is @generated
import typing as t

from ..serialization import StrEnum


class UsageAtZero(StrEnum):
    """What a customer's usage does once the credit it can use runs out: what the subscription's plan
    says (`FOLLOW_PLAN`), or always or never refused for this customer."""

    FOLLOW_PLAN = "FOLLOW_PLAN"
    ALWAYS_PAUSE = "ALWAYS_PAUSE"
    NEVER_PAUSE = "NEVER_PAUSE"


UsageAtZeroLiteral: t.TypeAlias = t.Literal[
    "FOLLOW_PLAN", "ALWAYS_PAUSE", "NEVER_PAUSE"
]
"""The values of :class:`UsageAtZero`, which arguments take as plain strings too."""
