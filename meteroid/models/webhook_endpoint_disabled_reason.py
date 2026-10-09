# this file is @generated
import typing as t

from ..serialization import StrEnum


class WebhookEndpointDisabledReason(StrEnum):
    """The values of `WebhookEndpointDisabledReason`; others are kept as received."""

    MANUAL = "MANUAL"
    AUTO_FAILURES = "AUTO_FAILURES"
    GONE = "GONE"


WebhookEndpointDisabledReasonLiteral: t.TypeAlias = t.Literal[
    "MANUAL", "AUTO_FAILURES", "GONE"
]
"""The values of :class:`WebhookEndpointDisabledReason`, which arguments take as plain strings too."""
