# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from decimal import Decimal

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .billing_period_enum import BillingPeriodEnum
    from .credit_pack_expiry import CreditPackExpiry
    from .credit_pack_rollover import CreditPackRollover


@dataclasses.dataclass(kw_only=True)
class CreditPlanFee(BaseModel):
    """Credit pack: charged `unit_price` × `quantity` in advance each billing period, it grants
    `credit_amount` × `quantity` of credit, in the plan currency or in `credit_unit_id`, once paid.
    A zero `unit_price` makes it credit included with the plan (promotional). A currency pack
    priced below its credit (e.g. 500.00 buys 550.00) grants the price paid as paid credit and the
    difference as promotional bonus credit, which applies before tax."""

    cadence: BillingPeriodEnum

    credit_amount: Decimal

    quantity: int

    type: t.Literal["CREDIT"] = "CREDIT"

    unit_price: Decimal

    credit_unit_id: str | None | Unset = UNSET
    """The credit unit `credit_amount` is granted in; absent grants the plan currency. The pack is
    paid in the plan currency, and taxed when sold if it grants a credit unit."""

    expiry: CreditPackExpiry | None | Unset = UNSET

    once: bool | None = None
    """When true, the pack is billed and its credit granted once, on the subscription's first
    invoice, instead of every period (e.g. a welcome credit). A plan change grants it on the
    next invoice only if the subscription never received a one-time credit of the same
    product; credit packs billed every period don't count. Cannot be combined with `rollover`."""

    rollover: CreditPackRollover | None | Unset = UNSET
