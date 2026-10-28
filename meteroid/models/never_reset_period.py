# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class NeverResetPeriod(BaseModel):
    """Never resets — counts all usage since the subscription was activated."""

    type: t.Literal["NEVER"] = "NEVER"
