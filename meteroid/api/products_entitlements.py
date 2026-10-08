# this file is @generated
"""Products entitlements API."""

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


class AsyncProductsEntitlements(ApiBaseAsync):
    """Products entitlements API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncProductsEntitlementsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncProductsEntitlementsWithRawResponse(self)

    async def list(
        self,
        product_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> ResolvedEntitlementListResponse:
        """List product entitlements"""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/products/{product_id}/entitlements",
                path_params={
                    "product_id": product_id,
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
        product_id: str,
        *,
        entitlements: builtins.list[EntitlementSpecRequest],
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> EntitlementListResponse:
        """Create product entitlements

        A product has no entitlement rows of its own: its entitlements are the feature-level
        defaults of the features scoped to it, which is what `GET` on this path resolves. Every
        spec must therefore target a feature belonging to `product_id`. Features that already
        carry a default entitlement are skipped.

        Specs are validated up front, but the writes are not atomic: each feature is written on
        its own, so a failure part-way can leave earlier specs committed. Retrying is safe."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/products/{product_id}/entitlements",
                path_params={
                    "product_id": product_id,
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


class AsyncProductsEntitlementsWithRawResponse:
    """The methods of :class:`AsyncProductsEntitlements`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncProductsEntitlements) -> None:
        self.list = async_to_raw_response_wrapper(resource.list)
        self.create = async_to_raw_response_wrapper(resource.create)


class ProductsEntitlements(ApiBaseSync):
    """Products entitlements API."""

    @property
    def with_raw_response(self) -> ProductsEntitlementsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return ProductsEntitlementsWithRawResponse(self)

    def list(
        self,
        product_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> ResolvedEntitlementListResponse:
        """List product entitlements"""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/products/{product_id}/entitlements",
                path_params={
                    "product_id": product_id,
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
        product_id: str,
        *,
        entitlements: builtins.list[EntitlementSpecRequest],
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> EntitlementListResponse:
        """Create product entitlements

        A product has no entitlement rows of its own: its entitlements are the feature-level
        defaults of the features scoped to it, which is what `GET` on this path resolves. Every
        spec must therefore target a feature belonging to `product_id`. Features that already
        carry a default entitlement are skipped.

        Specs are validated up front, but the writes are not atomic: each feature is written on
        its own, so a failure part-way can leave earlier specs committed. Retrying is safe."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/products/{product_id}/entitlements",
                path_params={
                    "product_id": product_id,
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


class ProductsEntitlementsWithRawResponse:
    """The methods of :class:`ProductsEntitlements`, returning an :class:`APIResponse`."""

    def __init__(self, resource: ProductsEntitlements) -> None:
        self.list = to_raw_response_wrapper(resource.list)
        self.create = to_raw_response_wrapper(resource.create)
