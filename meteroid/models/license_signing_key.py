# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .license_signing_key_status import LicenseSigningKeyStatus


@dataclasses.dataclass(kw_only=True)
class LicenseSigningKey(BaseModel):
    """The `LicenseSigningKey` object."""

    created_at: datetime

    kid: str
    """The key id, the `kid` header of the licenses it signs."""

    public_key_pem: str
    """Ed25519 public key, PEM-encoded."""

    status: LicenseSigningKeyStatus

    retired_at: datetime | None = None
