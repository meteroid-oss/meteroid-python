# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .entitlement_value import EntitlementValue
    from .feature_type import FeatureType
    from .product_id import ProductId


@dataclasses.dataclass(kw_only=True)
class CreateFeatureRequest(BaseModel):
    """The `CreateFeatureRequest` object."""

    code: str
    """Unique key used to reference this feature in your code. Cannot be changed after creation."""

    feature_type: FeatureType
    """Fixed at creation — a feature never changes type."""

    name: str

    description: str | None | Unset = UNSET

    entitlement: EntitlementValue | None | Unset = UNSET

    product_id: ProductId | None | Unset = UNSET
