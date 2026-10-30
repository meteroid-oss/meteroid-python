# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .license import License


@dataclasses.dataclass(kw_only=True)
class LicenseListResponse(BaseModel):
    """The `LicenseListResponse` object."""

    data: list[License]
