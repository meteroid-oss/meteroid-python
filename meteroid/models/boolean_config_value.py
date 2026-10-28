# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class BooleanConfigValue(BaseModel):
    """A boolean config value."""

    kind: t.Literal["BOOLEAN"] = "BOOLEAN"

    value: bool
