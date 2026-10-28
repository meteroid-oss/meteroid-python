# this file is @generated
from __future__ import annotations

import typing as t

from ..serialization import Discriminator, UnknownVariant
from .credit_caps import CreditCaps
from .credit_exhausted_rule_invoice_variant import CreditExhaustedRuleInvoiceVariant
from .credit_exhausted_rule_pause_variant import CreditExhaustedRulePauseVariant

CreditExhaustedRule: t.TypeAlias = t.Annotated[
    CreditExhaustedRuleInvoiceVariant
    | CreditExhaustedRulePauseVariant
    | CreditCaps
    | UnknownVariant,
    Discriminator(
        "type",
        {
            "invoice": CreditExhaustedRuleInvoiceVariant,
            "pause": CreditExhaustedRulePauseVariant,
            "invoice_up_to": CreditCaps,
        },
    ),
]
"""What usage does once the credit it draws on runs out, for every denomination (currency or
credit unit) the plan charges usage in. A customer's wallet can override it.

Told apart by `type`; a variant this SDK version does not know is an `UnknownVariant`."""
