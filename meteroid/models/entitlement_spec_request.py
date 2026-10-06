# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .entitlement_value import EntitlementValue
    from .feature_id import FeatureId


@dataclasses.dataclass(kw_only=True)
class EntitlementSpecRequest(BaseModel):
    """One entitlement to create: which feature, and the value granted by the entity."""

    feature_id: FeatureId

    value: EntitlementValue
