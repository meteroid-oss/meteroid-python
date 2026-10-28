# this file is @generated
import typing as t

from ..serialization import StrEnum


class AutoTopUpStatus(StrEnum):
    """The values of `AutoTopUpStatus`; others are kept as received."""

    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    SUSPENDED = "SUSPENDED"


AutoTopUpStatusLiteral: t.TypeAlias = t.Literal["ACTIVE", "DISABLED", "SUSPENDED"]
"""The values of :class:`AutoTopUpStatus`, which arguments take as plain strings too."""
