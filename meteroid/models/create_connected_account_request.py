# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .country_code import CountryCode
    from .onboarding_mode import OnboardingMode


@dataclasses.dataclass(kw_only=True)
class CreateConnectedAccountRequest(BaseModel):
    """The `CreateConnectedAccountRequest` object."""

    email: str

    organization_name: str

    country: CountryCode | None | Unset = UNSET

    metadata: t.Any = None

    mode: OnboardingMode | None | Unset = UNSET

    redirect_url: str | None | Unset = UNSET
