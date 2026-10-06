# this file is @generated
from __future__ import annotations

import dataclasses

from ..serialization import UNSET, BaseModel, Unset


@dataclasses.dataclass(kw_only=True)
class UpdateFeatureRequest(BaseModel):
    """Partial update. Code, feature type and product are immutable."""

    description: str | None | Unset = UNSET
    """Omit to leave unchanged; send `null` to clear."""

    name: str | None | Unset = UNSET
