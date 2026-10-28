# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import date

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .create_subscription_add_on import CreateSubscriptionAddOn
    from .create_subscription_components import CreateSubscriptionComponents
    from .payment_methods_config import PaymentMethodsConfig
    from .plan_id import PlanId
    from .subscription_activation_condition_enum import (
        SubscriptionActivationConditionEnum,
    )
    from .usage_filter import UsageFilter


@dataclasses.dataclass(kw_only=True)
class SubscriptionCreateRequest(BaseModel):
    """The `SubscriptionCreateRequest` object."""

    activation_condition: SubscriptionActivationConditionEnum

    customer_id_or_alias: str

    plan_id: PlanId

    start_date: date

    add_ons: list[CreateSubscriptionAddOn] | None = None

    auto_advance_invoices: bool | None = None

    backdate_invoices: bool | None = None
    """Historical import mode: when true, invoices finalized for this subscription keep their
    billing-period date as the invoice date instead of being stamped with the emission date."""

    billing_day_anchor: int | None | Unset = UNSET

    charge_automatically: bool | None = None

    coupon_codes: list[str] | None = None
    """Codes of the coupons to apply. A code matches whatever the case of its ASCII letters; when
    several coupons differ from it only in that case, the one with exactly that code applies. A
    code that names no live coupon, or several differing only in case, refuses the request with
    400 listing the codes (unknown codes used to be ignored silently)."""

    custom_properties: t.Any = None
    """User-defined custom property values, keyed by definition `key`. Validated against the
    tenant's subscription definitions."""

    end_date: date | None = None

    invoice_memo: str | None = None

    net_terms: int | None = None

    payment_methods_config: PaymentMethodsConfig | None = None
    """Payment methods configuration. If not specified, inherits from the invoicing entity."""

    price_components: CreateSubscriptionComponents | None = None

    purchase_order: str | None | Unset = UNSET

    skip_past_invoices: bool | None = None
    """Migration mode: when true with a past start_date, skip creating invoices for past cycles.
    The subscription will be set to the current billing period with correct cycle_index."""

    trial_days: int | None = None

    usage_filter: UsageFilter | None = None
    """Bill only the customer's events whose property has this value. Omit to bill the events
    no usage filter of the customer's other subscriptions matches."""

    version: int | None = None
