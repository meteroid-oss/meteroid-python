# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .connected_account import ConnectedAccount
    from .onboarding_link_response import OnboardingLinkResponse


@dataclasses.dataclass(kw_only=True)
class CreateConnectedAccountResponse(BaseModel):
    """The created account (same fields as `ConnectedAccount`) plus its onboarding link."""

    _FLATTENED: t.ClassVar[tuple[str, ...]] = ("connected_account",)

    connected_account: ConnectedAccount

    onboarding_link: OnboardingLinkResponse
