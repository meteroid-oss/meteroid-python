# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .auto_top_up_write_request import AutoTopUpWriteRequest
    from .usage_at_zero import UsageAtZero


@dataclasses.dataclass(kw_only=True)
class PatchWalletRequest(BaseModel):
    """Partial update of a wallet's configuration: omit a field to leave it unchanged."""

    auto_top_up: AutoTopUpWriteRequest | None | Unset = UNSET

    low_balance_thresholds: list[int] | None | Unset = UNSET
    """Ascending, distinct, at most 5, non-negative. Omit to leave unchanged; an empty list
    clears every threshold."""

    unit_price: str | None | Unset = UNSET
    """Credit unit wallets: the price this customer agreed for one credit, in major units of the
    customer's currency, as a decimal string (positive, at most 12 decimal places). Purchases
    and automatic top-ups default to it instead of the list price. Omit to leave it unchanged;
    `null` returns the customer to the list price. A change applies to purchases quoted after
    it. An automatic top-up keeps running at the new price when it is at or below the price
    its terms were authorized at, and stops until they are confirmed again when it is above."""

    usage_at_zero: UsageAtZero | None | Unset = UNSET
