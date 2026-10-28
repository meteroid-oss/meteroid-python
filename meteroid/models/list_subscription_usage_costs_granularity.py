# this file is @generated
import typing as t

from ..serialization import StrEnum


class ListSubscriptionUsageCostsGranularity(StrEnum):
    """The values of `ListSubscriptionUsageCostsGranularity`; others are kept as received."""

    HOUR = "HOUR"
    DAY = "DAY"
    MONTH = "MONTH"


ListSubscriptionUsageCostsGranularityLiteral: t.TypeAlias = t.Literal[
    "HOUR", "DAY", "MONTH"
]
"""The values of :class:`ListSubscriptionUsageCostsGranularity`, which arguments take as plain strings too."""
