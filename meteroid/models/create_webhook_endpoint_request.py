# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .webhook_header_input import WebhookHeaderInput


@dataclasses.dataclass(kw_only=True)
class CreateWebhookEndpointRequest(BaseModel):
    """The `CreateWebhookEndpointRequest` object."""

    url: str
    """HTTPS destination. Private and loopback addresses are rejected unless the
    instance is configured to allow them."""

    description: str | None | Unset = UNSET

    event_types: list[str] | None = None
    """Event types to subscribe to. Omit or leave empty to receive every event type."""

    headers: list[WebhookHeaderInput] | None = None
    """Custom headers sent with every delivery."""

    rate_limit_per_sec: int | None | Unset = UNSET
    """Deliveries started per second, at most (1 to 1000)."""
