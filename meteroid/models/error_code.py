# this file is @generated
import typing as t

from ..serialization import StrEnum


class ErrorCode(StrEnum):
    """The values of `ErrorCode`; others are kept as received."""

    BAD_REQUEST = "BAD_REQUEST"
    NOT_FOUND = "NOT_FOUND"
    CONFLICT = "CONFLICT"
    FORBIDDEN = "FORBIDDEN"
    UNAUTHORIZED = "UNAUTHORIZED"
    TOKEN_EXPIRED = "TOKEN_EXPIRED"
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"


ErrorCodeLiteral: t.TypeAlias = t.Literal[
    "BAD_REQUEST",
    "NOT_FOUND",
    "CONFLICT",
    "FORBIDDEN",
    "UNAUTHORIZED",
    "TOKEN_EXPIRED",
    "TOO_MANY_REQUESTS",
    "INTERNAL_SERVER_ERROR",
]
"""The values of :class:`ErrorCode`, which arguments take as plain strings too."""
