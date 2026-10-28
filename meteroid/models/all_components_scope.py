# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class AllComponentsScope(BaseModel):
    """Every revenue line counts toward the floor."""

    type: t.Literal["all_components"] = "all_components"
