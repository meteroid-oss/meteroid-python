# this file is @generated
import typing as t

from ..serialization import StrEnum


class UsageCostUnit(StrEnum):
    """What a cost is counted in."""

    CURRENCY = "CURRENCY"
    CREDIT_UNIT = "CREDIT_UNIT"


UsageCostUnitLiteral: t.TypeAlias = t.Literal["CURRENCY", "CREDIT_UNIT"]
"""The values of :class:`UsageCostUnit`, which arguments take as plain strings too."""
