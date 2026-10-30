# this file is @generated
import typing as t

from ..serialization import StrEnum


class LicenseStatus(StrEnum):
    """The values of `LicenseStatus`; others are kept as received."""

    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    REVOKED = "REVOKED"


LicenseStatusLiteral: t.TypeAlias = t.Literal["PENDING", "ACTIVE", "REVOKED"]
"""The values of :class:`LicenseStatus`, which arguments take as plain strings too."""
