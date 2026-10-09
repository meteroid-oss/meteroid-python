# this file is @generated
from __future__ import annotations

import dataclasses

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class WebhookHeader(BaseModel):
    """A custom header sent with every delivery. A sensitive header never returns its
    value; `set` says whether it has one."""

    name: str

    sensitive: bool

    set: bool

    value: str | None = None
