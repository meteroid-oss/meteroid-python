# this file is @generated
import typing as t

from ..serialization import StrEnum


class ListCustomerUsageCostsGranularity(StrEnum):
    """The values of `ListCustomerUsageCostsGranularity`; others are kept as received."""

    HOUR = "HOUR"
    DAY = "DAY"
    MONTH = "MONTH"


ListCustomerUsageCostsGranularityLiteral: t.TypeAlias = t.Literal[
    "HOUR", "DAY", "MONTH"
]
"""The values of :class:`ListCustomerUsageCostsGranularity`, which arguments take as plain strings too."""
