# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel


@dataclasses.dataclass(kw_only=True)
class CreditExhaustedRulePauseVariant(BaseModel):
    """Access checks refuse usage once the credit the subscription can spend is used up."""

    type: t.Literal["pause"] = "pause"
