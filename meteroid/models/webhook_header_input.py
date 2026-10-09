# this file is @generated
from __future__ import annotations

import dataclasses

from ..serialization import UNSET, BaseModel, Unset


@dataclasses.dataclass(kw_only=True)
class WebhookHeaderInput(BaseModel):
    """A custom header to send with every delivery. A sensitive header is write-only:
    it is never returned, and on update sending it without a value keeps its value."""

    name: str

    sensitive: bool | None = None

    value: str | None | Unset = UNSET
