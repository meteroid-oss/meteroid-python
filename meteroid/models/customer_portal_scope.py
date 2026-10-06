# this file is @generated
import typing as t

from ..serialization import StrEnum


class CustomerPortalScope(StrEnum):
    """What a customer portal token may do."""

    READ = "read"
    MANAGE = "manage"


CustomerPortalScopeLiteral: t.TypeAlias = t.Literal["read", "manage"]
"""The values of :class:`CustomerPortalScope`, which arguments take as plain strings too."""
