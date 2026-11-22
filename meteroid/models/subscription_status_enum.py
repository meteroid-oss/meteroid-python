# this file is @generated
import typing as t

from ..serialization import StrEnum


class SubscriptionStatusEnum(StrEnum):
    """`PendingCharge`, `Paused`, `Suspended`, `Superseded` and `Errored` stay in the published
    schema; no subscription holds them any more, and a filter on them lists none."""

    PENDING_ACTIVATION = "PENDING_ACTIVATION"
    PENDING_CHARGE = "PENDING_CHARGE"
    TRIAL_ACTIVE = "TRIAL_ACTIVE"
    ACTIVE = "ACTIVE"
    TRIAL_EXPIRED = "TRIAL_EXPIRED"
    PAUSED = "PAUSED"
    SUSPENDED = "SUSPENDED"
    CANCELLED = "CANCELLED"
    ABORTED = "ABORTED"
    COMPLETED = "COMPLETED"
    SUPERSEDED = "SUPERSEDED"
    ERRORED = "ERRORED"


SubscriptionStatusEnumLiteral: t.TypeAlias = t.Literal[
    "PENDING_ACTIVATION",
    "PENDING_CHARGE",
    "TRIAL_ACTIVE",
    "ACTIVE",
    "TRIAL_EXPIRED",
    "PAUSED",
    "SUSPENDED",
    "CANCELLED",
    "ABORTED",
    "COMPLETED",
    "SUPERSEDED",
    "ERRORED",
]
"""The values of :class:`SubscriptionStatusEnum`, which arguments take as plain strings too."""
