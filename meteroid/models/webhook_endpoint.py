# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .webhook_endpoint_disabled_reason import WebhookEndpointDisabledReason
    from .webhook_endpoint_id import WebhookEndpointId
    from .webhook_header import WebhookHeader


@dataclasses.dataclass(kw_only=True)
class WebhookEndpoint(BaseModel):
    """A destination Meteroid POSTs signed event payloads to."""

    consecutive_failures: int
    """Failures since the last success, reset to 0 on any 2xx."""

    created_at: datetime

    disabled: bool

    event_types: list[str]
    """Subscribed event types. Empty means every event type."""

    headers: list[WebhookHeader]
    """Custom headers sent with every delivery."""

    id: WebhookEndpointId

    max_in_flight: int
    """How many deliveries this endpoint may have in flight at once. Read-only; it is
    set from the tenant's environment when the endpoint is created."""

    needs_setup: bool
    """A sensitive header still waits for its value; the endpoint cannot be enabled
    until it is set."""

    url: str

    description: str | None = None

    disabled_reason: WebhookEndpointDisabledReason | None = None

    last_failure_at: datetime | None = None

    last_success_at: datetime | None = None

    paused_until: datetime | None = None
    """The endpoint was unreachable several times in a row: nothing is sent before
    this time, then it is retried one delivery at a time until it answers again."""

    rate_limit_per_sec: int | None = None
    """Deliveries started per second, at most."""

    updated_at: datetime | None = None
