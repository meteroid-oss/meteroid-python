# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class ComponentsScope(BaseModel):
    """Component names — matched against `ReplacePlanRequest::components[].name`."""

    component_names: list[str]

    type: t.Literal["components"] = "components"
