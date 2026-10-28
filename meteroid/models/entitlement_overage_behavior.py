# this file is @generated
import typing as t

from ..serialization import StrEnum


class EntitlementOverageBehavior(StrEnum):
    """What happens once usage reaches the limit."""

    BLOCK = "BLOCK"
    ALLOW = "ALLOW"


EntitlementOverageBehaviorLiteral: t.TypeAlias = t.Literal["BLOCK", "ALLOW"]
"""The values of :class:`EntitlementOverageBehavior`, which arguments take as plain strings too."""
