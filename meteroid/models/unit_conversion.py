# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .unit_conversion_rounding_enum import UnitConversionRoundingEnum


@dataclasses.dataclass(kw_only=True)
class UnitConversion(BaseModel):
    """Converts the aggregated usage into the unit prices are set in, e.g. tokens priced per 1M.
    The usage is divided by `factor`, then rounded. Rounding applies to each priced group's
    total for the billing period: each group of a segmented or grouped metric, and each matrix
    cell, is rounded on its own, never each event."""

    factor: int
    """Raw units per priced unit, e.g. `1000000` to price per 1M."""

    rounding: UnitConversionRoundingEnum
