# this file is @generated
import typing as t

from ..serialization import StrEnum


class WebhookDeliveryStatus(StrEnum):
    """The values of `WebhookDeliveryStatus`; others are kept as received."""

    PENDING = "PENDING"
    IN_FLIGHT = "IN_FLIGHT"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


WebhookDeliveryStatusLiteral: t.TypeAlias = t.Literal[
    "PENDING", "IN_FLIGHT", "SUCCEEDED", "FAILED", "CANCELLED"
]
"""The values of :class:`WebhookDeliveryStatus`, which arguments take as plain strings too."""
