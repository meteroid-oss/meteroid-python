# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .feature_id import FeatureId


@dataclasses.dataclass(kw_only=True)
class EntitlementCheckFeature(BaseModel):
    """The `EntitlementCheckFeature` object."""

    code: str

    id: FeatureId
