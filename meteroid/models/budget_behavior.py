# this file is @generated
import typing as t

from ..serialization import StrEnum


class BudgetBehavior(StrEnum):
    """What reaching the amount does. A SOFT budget only sends alerts; a HARD budget also makes the
    entitlement check answer BUDGET_EXCEEDED for the features whose usage counts in its spend. A
    HARD budget on one subscription refuses the checks naming that subscription, and the checks
    naming none once every subscription charging the feature's metric is refused by its own."""

    SOFT = "SOFT"
    HARD = "HARD"


BudgetBehaviorLiteral: t.TypeAlias = t.Literal["SOFT", "HARD"]
"""The values of :class:`BudgetBehavior`, which arguments take as plain strings too."""
