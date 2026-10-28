# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from decimal import Decimal

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class NumberConfigValue(BaseModel):
    """A number config value (decimal, encoded as a string)."""

    kind: t.Literal["NUMBER"] = "NUMBER"

    value: Decimal
