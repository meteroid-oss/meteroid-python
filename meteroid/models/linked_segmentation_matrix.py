# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class LinkedSegmentationMatrix(BaseModel):
    """The `LinkedSegmentationMatrix` object."""

    dimension1_key: str

    dimension2_key: str

    type: t.Literal["LINKED"] = "LINKED"

    values: dict[str, list[str]]
