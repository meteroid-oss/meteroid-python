# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .entitlement_spec_request import EntitlementSpecRequest


@dataclasses.dataclass(kw_only=True)
class CreateEntitlementsRequest(BaseModel):
    """Entitlements already present on the entity are skipped, so the call can be replayed."""

    entitlements: list[EntitlementSpecRequest]
