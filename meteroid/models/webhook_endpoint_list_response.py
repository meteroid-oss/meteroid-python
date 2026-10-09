# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .webhook_endpoint import WebhookEndpoint


@dataclasses.dataclass(kw_only=True)
class WebhookEndpointListResponse(BaseModel):
    """The `WebhookEndpointListResponse` object."""

    data: list[WebhookEndpoint]
