# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .entitlement_value import EntitlementValue


@dataclasses.dataclass(kw_only=True)
class UpdateEntitlementRequest(BaseModel):
    """The `UpdateEntitlementRequest` object."""

    value: EntitlementValue | None | Unset = UNSET
