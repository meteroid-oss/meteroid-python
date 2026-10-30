# this file is @generated
from __future__ import annotations

import dataclasses

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class RevokeLicenseRequest(BaseModel):
    """The `RevokeLicenseRequest` object."""

    immediately: bool | None = None
    """Stop at once: the installation drops its license on its next refresh. Otherwise the
    license keeps working until it expires, and is not renewed."""
