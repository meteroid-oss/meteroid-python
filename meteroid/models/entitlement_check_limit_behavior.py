# this file is @generated
import typing as t

from ..serialization import StrEnum


class EntitlementCheckLimitBehavior(StrEnum):
    """The values of `EntitlementCheckLimitBehavior`; others are kept as received."""

    TRACK = "TRACK"
    SOFT = "SOFT"
    HARD = "HARD"


EntitlementCheckLimitBehaviorLiteral: t.TypeAlias = t.Literal["TRACK", "SOFT", "HARD"]
"""The values of :class:`EntitlementCheckLimitBehavior`, which arguments take as plain strings too."""
