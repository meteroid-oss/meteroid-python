# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .customer_portal_scope import CustomerPortalScope


@dataclasses.dataclass(kw_only=True)
class CustomerPortalTokenRequest(BaseModel):
    """The `CustomerPortalTokenRequest` object."""

    expires_in_seconds: int | None | Unset = UNSET
    """Token lifetime in seconds. Defaults to 86400 (24 hours).
    Must be between 60 and 2592000 (30 days)."""

    scopes: list[CustomerPortalScope] | None | Unset = UNSET
    """Scopes granted to the token. Defaults to `["read", "manage"]`.
    Use `["read"]` for tokens that only read billing state, e.g. to gate features in a browser."""
