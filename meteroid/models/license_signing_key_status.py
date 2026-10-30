# this file is @generated
import typing as t

from ..serialization import StrEnum


class LicenseSigningKeyStatus(StrEnum):
    """The values of `LicenseSigningKeyStatus`; others are kept as received."""

    ACTIVE = "ACTIVE"
    RETIRED = "RETIRED"


LicenseSigningKeyStatusLiteral: t.TypeAlias = t.Literal["ACTIVE", "RETIRED"]
"""The values of :class:`LicenseSigningKeyStatus`, which arguments take as plain strings too."""
