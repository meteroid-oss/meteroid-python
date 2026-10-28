# this file is @generated
import typing as t

from ..serialization import StrEnum


class AutoTopUpMethod(StrEnum):
    """The values of `AutoTopUpMethod`; others are kept as received."""

    FIXED = "FIXED"
    TO_TARGET = "TO_TARGET"


AutoTopUpMethodLiteral: t.TypeAlias = t.Literal["FIXED", "TO_TARGET"]
"""The values of :class:`AutoTopUpMethod`, which arguments take as plain strings too."""
