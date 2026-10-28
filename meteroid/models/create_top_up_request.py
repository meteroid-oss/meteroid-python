# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t
from datetime import datetime

from ..serialization import UNSET, BaseModel, Unset

if t.TYPE_CHECKING:
    from .currency import Currency
    from .top_up_collection import TopUpCollection


@dataclasses.dataclass(kw_only=True)
class CreateTopUpRequest(BaseModel):
    """Credit sold to the customer, charged or invoiced."""

    amount: int
    """Credit to buy, positive, applying to ALL charges. In minor units of `currency`, charged
    one for one without tax: the usage it pays is taxed on the invoice that bills it. With
    `credit_unit`, in minor units of that unit (e.g. 500000 is 5,000.00 credits of a unit with
    precision 2), charged at the unit's price per credit in the customer's currency, plus tax
    under the unit's product."""

    collection: TopUpCollection | None = None
    """CHARGE (default) charges a saved payment method now; SEND_INVOICE issues an invoice and
    grants the credit once it is paid."""

    credit_unit: str | None | Unset = UNSET
    """Buy credits of this credit unit (its code) instead of money; excludes `currency`. They are
    charged in the customer's currency at the customer's agreed price for the unit (the
    wallet's `unit_price`), else its list price, plus tax, under the unit's product."""

    currency: Currency | None | Unset = UNSET

    expires_at: datetime | None | Unset = UNSET
    """Absolute expiry of the purchased credit; unset never expires."""

    payment_method_id: str | None | Unset = UNSET
    """CHARGE only; defaults to the customer's default payment method."""

    unit_price: str | None | Unset = UNSET
    """With `credit_unit`: the negotiated price of one credit for this purchase, in major units of
    the customer's currency, as a decimal string (e.g. "0.0008"). Defaults to the wallet's
    `unit_price` when set, else the list price; the unit must still have a list price in that
    currency."""
