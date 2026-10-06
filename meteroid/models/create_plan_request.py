# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .billing_config import BillingConfig
    from .entitlement_spec_request import EntitlementSpecRequest
    from .plan_add_on_input import PlanAddOnInput
    from .plan_status_enum import PlanStatusEnum
    from .plan_type_enum import PlanTypeEnum
    from .price_component_input import PriceComponentInput
    from .product_family_id import ProductFamilyId
    from .trial_config import TrialConfig


@dataclasses.dataclass(kw_only=True)
class CreatePlanRequest(BaseModel):
    """The `CreatePlanRequest` object."""

    components: list[PriceComponentInput]

    currency: str

    name: str

    plan_type: PlanTypeEnum

    product_family_id: ProductFamilyId

    status: PlanStatusEnum

    add_ons: list[PlanAddOnInput] | None = None

    billing: BillingConfig | None | Unset = UNSET

    description: str | None | Unset = UNSET

    entitlements: list[EntitlementSpecRequest] | None = None
    """Entitlements to attach to this plan's version. Replacing a published plan creates a
    new version, and entitlements belong to a version, so passing them here keeps them
    attached to whichever version the call produces."""

    self_service_rank: int | None | Unset = UNSET

    tax_inclusive: bool | None = None
    """The plan's amounts are quoted tax-included ("9.99 incl. VAT"): tax is carved out of
    them at invoice time instead of being added on top, so the customer pays the quoted
    price whatever rate applies. A customer who bears no tax (reverse charge, exempt,
    export) still pays it in full. Defaults to `false`."""

    trial: TrialConfig | None | Unset = UNSET
