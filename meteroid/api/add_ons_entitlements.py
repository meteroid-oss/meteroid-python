# this file is @generated
"""Add ons entitlements API."""

from __future__ import annotations

import builtins
import typing as t

from .. import models as _models
from ..models import (
    CreateEntitlementsRequest,
    EntitlementListResponse,
    EntitlementSpecRequest,
    ResolvedEntitlementListResponse,
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


class AsyncAddOnsEntitlements(ApiBaseAsync):
    """Add ons entitlements API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncAddOnsEntitlementsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncAddOnsEntitlementsWithRawResponse(self)

    async def list(
        self,
        addon_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> ResolvedEntitlementListResponse:
        """List add-on entitlements"""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/addons/{addon_id}/entitlements",
                path_params={
                    "addon_id": addon_id,
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
        return decode_response(response, ResolvedEntitlementListResponse)

    async def create(
        self,
        addon_id: str,
        *,
        entitlements: builtins.list[EntitlementSpecRequest],
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> EntitlementListResponse:
        """Create add-on entitlements

        Entitlements already present on this add-on are skipped."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/addons/{addon_id}/entitlements",
                path_params={
                    "addon_id": addon_id,
                },
                json_body=to_json_value(
                    CreateEntitlementsRequest(
                        entitlements=entitlements,
                    ),
                    CreateEntitlementsRequest,
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
        return decode_response(response, EntitlementListResponse)


class AsyncAddOnsEntitlementsWithRawResponse:
    """The methods of :class:`AsyncAddOnsEntitlements`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncAddOnsEntitlements) -> None:
        self.list = async_to_raw_response_wrapper(resource.list)
        self.create = async_to_raw_response_wrapper(resource.create)


class AddOnsEntitlements(ApiBaseSync):
    """Add ons entitlements API."""

    @property
    def with_raw_response(self) -> AddOnsEntitlementsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AddOnsEntitlementsWithRawResponse(self)

    def list(
        self,
        addon_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> ResolvedEntitlementListResponse:
        """List add-on entitlements"""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/addons/{addon_id}/entitlements",
                path_params={
                    "addon_id": addon_id,
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
        return decode_response(response, ResolvedEntitlementListResponse)

    def create(
        self,
        addon_id: str,
        *,
        entitlements: builtins.list[EntitlementSpecRequest],
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> EntitlementListResponse:
        """Create add-on entitlements

        Entitlements already present on this add-on are skipped."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/addons/{addon_id}/entitlements",
                path_params={
                    "addon_id": addon_id,
                },
                json_body=to_json_value(
                    CreateEntitlementsRequest(
                        entitlements=entitlements,
                    ),
                    CreateEntitlementsRequest,
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
        return decode_response(response, EntitlementListResponse)


class AddOnsEntitlementsWithRawResponse:
    """The methods of :class:`AddOnsEntitlements`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AddOnsEntitlements) -> None:
        self.list = to_raw_response_wrapper(resource.list)
        self.create = to_raw_response_wrapper(resource.create)
