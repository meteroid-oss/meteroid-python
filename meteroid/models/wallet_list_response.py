# this file is @generated
from __future__ import annotations

import dataclasses
import typing as t

from ..serialization import BaseModel

if t.TYPE_CHECKING:
    from .wallet import Wallet


@dataclasses.dataclass(kw_only=True)
class WalletListResponse(BaseModel):
    """A customer's wallets, the customer's own currency first."""

    data: list[Wallet]
