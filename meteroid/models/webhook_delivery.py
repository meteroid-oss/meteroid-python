# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .event_id import EventId
    from .webhook_delivery_id import WebhookDeliveryId
    from .webhook_delivery_status import WebhookDeliveryStatus
    from .webhook_endpoint_id import WebhookEndpointId


@dataclasses.dataclass(kw_only=True)
class WebhookDelivery(BaseModel):
    """One event queued for one endpoint, with the state of its retry cycle."""

    attempt_count: int

    created_at: datetime

    endpoint_id: WebhookEndpointId

    event_type: str

    id: WebhookDeliveryId

    manual: bool
    """True when the delivery was created by a resend or a test event."""

    message_id: EventId

    status: WebhookDeliveryStatus

    completed_at: datetime | None = None

    last_error: str | None = None

    last_response_status: int | None = None

    next_attempt_at: datetime | None = None
