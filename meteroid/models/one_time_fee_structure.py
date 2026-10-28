# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class OneTimeFeeStructure(BaseModel):
    """The `OneTimeFeeStructure` object."""

    type: t.Literal["ONE_TIME"] = "ONE_TIME"
