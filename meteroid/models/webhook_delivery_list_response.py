# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .pagination_response import PaginationResponse
    from .webhook_delivery import WebhookDelivery


@dataclasses.dataclass(kw_only=True)
class WebhookDeliveryListResponse(BaseModel):
    """The `WebhookDeliveryListResponse` object."""

    data: list[WebhookDelivery]

    pagination_meta: PaginationResponse
