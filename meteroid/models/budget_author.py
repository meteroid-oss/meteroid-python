# this file is @generated
import typing as t

from ..serialization import StrEnum


class BudgetAuthor(StrEnum):
    """Who set the budget: you (TENANT) or the customer, from the portal (CUSTOMER)."""

    TENANT = "TENANT"
    CUSTOMER = "CUSTOMER"


BudgetAuthorLiteral: t.TypeAlias = t.Literal["TENANT", "CUSTOMER"]
"""The values of :class:`BudgetAuthor`, which arguments take as plain strings too."""
