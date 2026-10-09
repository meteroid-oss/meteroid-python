# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .webhook_header_input import WebhookHeaderInput


@dataclasses.dataclass(kw_only=True)
class UpdateWebhookEndpointRequest(BaseModel):
    """The `UpdateWebhookEndpointRequest` object."""

    description: str | None | Unset = UNSET
    """Omit to leave unchanged; send `null` or an empty string to clear."""

    disabled: bool | None | Unset = UNSET
    """Re-enabling an endpoint also resets its consecutive failure count."""

    event_types: list[str] | None | Unset = UNSET
    """Replaces the subscription list. An empty array subscribes to every event type."""

    headers: list[WebhookHeaderInput] | None | Unset = UNSET
    """Replaces the custom header list. An empty array removes every header."""

    rate_limit_per_sec: int | None | Unset = UNSET
    """Omit to leave unchanged; send `null` to remove the rate limit."""

    url: str | None | Unset = UNSET
