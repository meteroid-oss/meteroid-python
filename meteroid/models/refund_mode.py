# this file is @generated
import typing as t

from ..serialization import StrEnum


class RefundMode(StrEnum):
    """How a voluntary refund was issued: through the provider, or recorded after a wire or cash
    movement made outside Meteroid."""

    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"


RefundModeLiteral: t.TypeAlias = t.Literal["ONLINE", "OFFLINE"]
"""The values of :class:`RefundMode`, which arguments take as plain strings too."""
