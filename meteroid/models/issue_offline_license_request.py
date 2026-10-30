# this file is @generated
from __future__ import annotations

import dataclasses

from ..serialization import UNSET, BaseModel, Unset


@dataclasses.dataclass(kw_only=True)
class IssueOfflineLicenseRequest(BaseModel):
    """The `IssueOfflineLicenseRequest` object."""

    valid_days: int
    """Lifetime of the offline license, 1 to 400 days."""

    instance_id: str | None | Unset = UNSET
    """The installation's id as it reports it, up to 255 characters without spaces: the license
    names it (`aud`) and stays bound to it. Without one, the license is not tied to one."""
