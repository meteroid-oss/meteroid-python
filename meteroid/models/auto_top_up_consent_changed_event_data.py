# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .actor import Actor
    from .customer_id import CustomerId


@dataclasses.dataclass(kw_only=True)
class AutoTopUpConsentChangedEventData(BaseModel):
    """The authorization of a wallet's automatic top-up was given, changed or withdrawn."""

    actor: Actor
    """Who gave, changed or withdrew the authorization."""

    changed_at: datetime
    """When the authorization changed."""

    currency: str
    """The wallet's currency (ISO 4217) or credit unit code."""

    customer_id: CustomerId

    enabled: bool
    """Whether automatic top-up is authorized after this change."""

    configuration_revision: str | None = None
    """Identifies the terms authorized now, without disclosing payment details; absent when
    withdrawn."""

    consent_attested_at: datetime | None = None
    """When that attestation was made."""

    consent_attested_by: Actor | None = None

    previous_configuration_revision: str | None = None
    """Identifies the terms authorized before the change; absent when none were."""
