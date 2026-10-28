# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from decimal import Decimal

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class PackagePricing(BaseModel):
    """The `PackagePricing` object."""

    block_size: int

    rate: Decimal

    type: t.Literal["PACKAGE"] = "PACKAGE"
