# this file is @generated
from __future__ import annotations

import dataclasses

from ..serialization import UNSET, BaseModel, Unset


@dataclasses.dataclass(kw_only=True)
class VoidEventRequest(BaseModel):
    """The `VoidEventRequest` object."""

    customer_alias: str | None | Unset = UNSET
    """External customer alias of the event. Set this or `customer_id`."""

    customer_id: str | None | Unset = UNSET
    """Meteroid customer ID of the event. Set this or `customer_alias`."""
