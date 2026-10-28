# this file is @generated
from __future__ import annotations

import typing as t

from ..serialization import Discriminator, UnknownVariant
from .credit_discount import CreditDiscount
from .fixed_discount import FixedDiscount
from .percentage_discount import PercentageDiscount

CouponDiscount: t.TypeAlias = t.Annotated[
    PercentageDiscount | FixedDiscount | CreditDiscount | UnknownVariant,
    Discriminator(
        "type",
        {
            "PERCENTAGE": PercentageDiscount,
            "FIXED": FixedDiscount,
            "CREDIT": CreditDiscount,
        },
    ),
]
"""Told apart by `type`; a variant this SDK version does not know is an `UnknownVariant`."""
