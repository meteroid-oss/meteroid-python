# this file is @generated
import typing as t

from ..serialization import StrEnum


class ScheduledEventType(StrEnum):
    """The values of `ScheduledEventType`; others are kept as received."""

    PLAN_CHANGE = "PLAN_CHANGE"
    CANCEL = "CANCEL"
    AMENDMENT = "AMENDMENT"


ScheduledEventTypeLiteral: t.TypeAlias = t.Literal["PLAN_CHANGE", "CANCEL", "AMENDMENT"]
"""The values of :class:`ScheduledEventType`, which arguments take as plain strings too."""
