# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .webhook_endpoint import WebhookEndpoint


@dataclasses.dataclass(kw_only=True)
class CreatedWebhookEndpoint(BaseModel):
    """The signing secret is returned in full here and never again outside the reveal
    and rotate endpoints."""

    _FLATTENED: t.ClassVar[tuple[str, ...]] = ("webhook_endpoint",)

    webhook_endpoint: WebhookEndpoint

    secret: str
