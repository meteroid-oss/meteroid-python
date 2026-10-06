# this file is @generated
"""Entitlements API."""

from __future__ import annotations

import typing as t

from .. import models as _models
from ..models import (
    Entitlement,
    EntitlementValue,
    UpdateEntitlementRequest,
)
from ..serialization import UNSET, Unset, to_json_value
from ._response import async_to_raw_response_wrapper, to_raw_response_wrapper
from .common import (
    ApiBaseAsync,
    ApiBaseSync,
    ApiRequest,
    Timeout,
    decode_response,
)


class AsyncEntitlements(ApiBaseAsync):
    """Entitlements API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncEntitlementsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncEntitlementsWithRawResponse(self)

    async def retrieve(
        self,
        entitlement_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Entitlement:
        """Get entitlement details"""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/entitlements/{entitlement_id}",
                path_params={
                    "entitlement_id": entitlement_id,
                },
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
        return decode_response(response, Entitlement)

    async def delete(
        self,
        entitlement_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Delete an entitlement"""
        await self._request(
            ApiRequest(
                method="delete",
                path="/api/v1/entitlements/{entitlement_id}",
                path_params={
                    "entitlement_id": entitlement_id,
                },
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )

    async def update(
        self,
        entitlement_id: str,
        *,
        value: EntitlementValue | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Entitlement:
        """Update an entitlement

        The new value must match the feature's declared type."""
        response = await self._request(
            ApiRequest(
                method="patch",
                path="/api/v1/entitlements/{entitlement_id}",
                path_params={
                    "entitlement_id": entitlement_id,
                },
                json_body=to_json_value(
                    UpdateEntitlementRequest(
                        value=value,
                    ),
                    UpdateEntitlementRequest,
                ),
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
        return decode_response(response, Entitlement)


class AsyncEntitlementsWithRawResponse:
    """The methods of :class:`AsyncEntitlements`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncEntitlements) -> None:
        self.retrieve = async_to_raw_response_wrapper(resource.retrieve)
        self.delete = async_to_raw_response_wrapper(resource.delete)
        self.update = async_to_raw_response_wrapper(resource.update)


class Entitlements(ApiBaseSync):
    """Entitlements API."""

    @property
    def with_raw_response(self) -> EntitlementsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return EntitlementsWithRawResponse(self)

    def retrieve(
        self,
        entitlement_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Entitlement:
        """Get entitlement details"""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/entitlements/{entitlement_id}",
                path_params={
                    "entitlement_id": entitlement_id,
                },
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
        return decode_response(response, Entitlement)

    def delete(
        self,
        entitlement_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Delete an entitlement"""
        self._request(
            ApiRequest(
                method="delete",
                path="/api/v1/entitlements/{entitlement_id}",
                path_params={
                    "entitlement_id": entitlement_id,
                },
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )

    def update(
        self,
        entitlement_id: str,
        *,
        value: EntitlementValue | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Entitlement:
        """Update an entitlement

        The new value must match the feature's declared type."""
        response = self._request(
            ApiRequest(
                method="patch",
                path="/api/v1/entitlements/{entitlement_id}",
                path_params={
                    "entitlement_id": entitlement_id,
                },
                json_body=to_json_value(
                    UpdateEntitlementRequest(
                        value=value,
                    ),
                    UpdateEntitlementRequest,
                ),
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
        return decode_response(response, Entitlement)


class EntitlementsWithRawResponse:
    """The methods of :class:`Entitlements`, returning an :class:`APIResponse`."""

    def __init__(self, resource: Entitlements) -> None:
        self.retrieve = to_raw_response_wrapper(resource.retrieve)
        self.delete = to_raw_response_wrapper(resource.delete)
        self.update = to_raw_response_wrapper(resource.update)
