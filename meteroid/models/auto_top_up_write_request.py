# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .auto_top_up_method import AutoTopUpMethod


@dataclasses.dataclass(kw_only=True)
class AutoTopUpWriteRequest(BaseModel):
    """An automatic top-up's terms, replaced as a whole. FIXED needs `amount` and no `target`;
    TO_TARGET needs `target` above `threshold` and no `amount`; amounts are positive."""

    method: AutoTopUpMethod
    """FIXED buys `amount` each time; TO_TARGET buys back up to `target`."""

    threshold: int
    """Tops up once the balance is at or below this, in minor units of the wallet."""

    amount: int | None | Unset = UNSET
    """FIXED only: credit bought each time, in minor units of the wallet."""

    at_current_price: bool | None = None
    """Credit unit wallets: authorize today's price per credit for these terms, which lifts a
    stop caused by a price increase. When false (the default) the terms keep the price they
    were authorized at, and a rule stopped by a price increase stays stopped.
    A price at or below the authorized one never stops the rule: top-ups charge it."""

    customer_consent_attested: bool | None = None
    """Attests that the customer agreed to automatic charges on these terms; recorded with the
    API key and the time. Required (true) when the terms turn automatic top-up on, including
    one the customer turned off, or change what it charges. Not needed to resend the stored
    terms unchanged, nor to change terms the customer confirmed in their portal: those stop
    until the customer confirms the new ones."""

    daily_cap: int | None | Unset = UNSET
    """Most charged in a rolling day, tax included. For a credit unit wallet caps are money, in
    minor units of the customer's currency."""

    maximum: int | None | Unset = UNSET
    """Largest single charge, in the same money as `minimum`."""

    minimum: int | None | Unset = UNSET
    """Smallest single charge. For a credit unit wallet it is money (the price before tax, in
    minor units of the customer's currency), like the caps; the threshold, amount and target
    are credits."""

    monthly_cap: int | None | Unset = UNSET
    """Most charged in a calendar month (UTC), tax included."""

    payment_method_id: str | None | Unset = UNSET
    """Defaults to the customer's default payment method: the customer's agreement, and your
    attestation of it, then cover whichever method is their default at each top-up."""

    target: int | None | Unset = UNSET
    """TO_TARGET only: the balance a top-up brings the wallet back to; must exceed `threshold`."""
