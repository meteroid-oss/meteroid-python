# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .license import License


@dataclasses.dataclass(kw_only=True)
class IssueLicenseResponse(BaseModel):
    """The `IssueLicenseResponse` object."""

    license: License

    activation_code: str | None = None
    """Online: one-time code the customer enters in their installation to activate the license."""

    offline_license: str | None = None
    """Offline: the signed license (a JWT) to install in the installation."""
