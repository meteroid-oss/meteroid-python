# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class CreditFeeStructure(BaseModel):
    """The `CreditFeeStructure` object."""

    type: t.Literal["CREDIT"] = "CREDIT"
