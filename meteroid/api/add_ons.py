# this file is @generated
"""Add ons API."""

from __future__ import annotations

import functools
import typing as t

from .. import models as _models
from ..models import (
    AddOn,
    AddOnListResponse,
    CreateAddOnRequest,
    PriceId,
    ProductId,
    UpdateAddOnRequest,
)
from ..serialization import UNSET, Unset, to_json_value
from ._pages import (
    AddOnsListPage,
    AsyncAddOnsListPage,
)
from ._pagination import (
    AsyncPaginator,
    PagePaging,
    step,
)
from ._response import async_to_raw_response_wrapper, to_raw_response_wrapper
from .add_ons_entitlements import (
    AddOnsEntitlements,
    AddOnsEntitlementsWithRawResponse,
    AsyncAddOnsEntitlements,
    AsyncAddOnsEntitlementsWithRawResponse,
)
from .common import (
    ApiBaseAsync,
    ApiBaseSync,
    ApiRequest,
    Timeout,
    decode_response,
    serialize_query_params,
)


class AsyncAddOns(ApiBaseAsync):
    """Add ons API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncAddOnsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncAddOnsWithRawResponse(self)

    @functools.cached_property
    def entitlements(self) -> AsyncAddOnsEntitlements:
        """The entitlements API."""
        return AsyncAddOnsEntitlements(self._cfg, self._httpx_client)

    def list(
        self,
        *,
        search: str | None = None,
        currency: str | None = None,
        include_archived: bool | None = None,
        order_by: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> AsyncPaginator[AddOn, AsyncAddOnsListPage]:
        """List add-ons

        :param include_archived: Include archived add-ons in the results (default: false)
        :param order_by: Sort order. Format: `column.direction`. Allowed columns: `name`, `created_at`. Direction: `asc` or `desc`. Default: `created_at.desc`.
        :param page: Page number (0-indexed)
        :param per_page: Number of items per page"""

        async def fetch(page_param: int | None) -> AddOnListResponse:
            response = await self._request(
                ApiRequest(
                    method="get",
                    path="/api/v1/addons",
                    query_params=serialize_query_params(
                        {
                            "search": search,
                            "currency": currency,
                            "include_archived": include_archived,
                            "order_by": order_by,
                            "page": page_param,
                            "per_page": per_page,
                        },
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
            return decode_response(response, AddOnListResponse)

        paging = PagePaging[AddOnListResponse, AddOn](
            items=lambda body: body.data,
            total_pages=lambda body: step(
                body.pagination_meta, lambda v: v.total_pages
            ),
            first_page=0,
        )
        return AsyncPaginator(lambda: AsyncAddOnsListPage._first(fetch, page, paging))

    async def create(
        self,
        *,
        name: str,
        price_id: PriceId,
        product_id: ProductId,
        description: str | None | Unset = UNSET,
        max_instances_per_subscription: int | None | Unset = UNSET,
        self_serviceable: bool | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> AddOn:
        """Create an add-on"""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/addons",
                json_body=to_json_value(
                    CreateAddOnRequest(
                        description=description,
                        max_instances_per_subscription=max_instances_per_subscription,
                        name=name,
                        price_id=price_id,
                        product_id=product_id,
                        self_serviceable=self_serviceable,
                    ),
                    CreateAddOnRequest,
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
        return decode_response(response, AddOn)

    async def retrieve(
        self,
        addon_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> AddOn:
        """Get add-on details"""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/addons/{addon_id}",
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
        return decode_response(response, AddOn)

    async def update(
        self,
        addon_id: str,
        *,
        description: str | None | Unset = UNSET,
        max_instances_per_subscription: int | None | Unset = UNSET,
        name: str | None | Unset = UNSET,
        price_id: PriceId | None | Unset = UNSET,
        self_serviceable: bool | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> AddOn:
        """Update an add-on"""
        response = await self._request(
            ApiRequest(
                method="patch",
                path="/api/v1/addons/{addon_id}",
                path_params={
                    "addon_id": addon_id,
                },
                json_body=to_json_value(
                    UpdateAddOnRequest(
                        description=description,
                        max_instances_per_subscription=max_instances_per_subscription,
                        name=name,
                        price_id=price_id,
                        self_serviceable=self_serviceable,
                    ),
                    UpdateAddOnRequest,
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
        return decode_response(response, AddOn)

    async def archive(
        self,
        addon_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Archive an add-on"""
        await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/addons/{addon_id}/archive",
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

    async def unarchive(
        self,
        addon_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Unarchive an add-on"""
        await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/addons/{addon_id}/unarchive",
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


class AsyncAddOnsWithRawResponse:
    """The methods of :class:`AsyncAddOns`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncAddOns) -> None:
        self._resource = resource
        self.list = async_to_raw_response_wrapper(resource.list)
        self.create = async_to_raw_response_wrapper(resource.create)
        self.retrieve = async_to_raw_response_wrapper(resource.retrieve)
        self.update = async_to_raw_response_wrapper(resource.update)
        self.archive = async_to_raw_response_wrapper(resource.archive)
        self.unarchive = async_to_raw_response_wrapper(resource.unarchive)

    @property
    def entitlements(self) -> AsyncAddOnsEntitlementsWithRawResponse:
        """The entitlements API."""
        return AsyncAddOnsEntitlementsWithRawResponse(self._resource.entitlements)


class AddOns(ApiBaseSync):
    """Add ons API."""

    @property
    def with_raw_response(self) -> AddOnsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AddOnsWithRawResponse(self)

    @functools.cached_property
    def entitlements(self) -> AddOnsEntitlements:
        """The entitlements API."""
        return AddOnsEntitlements(self._cfg, self._httpx_client)

    def list(
        self,
        *,
        search: str | None = None,
        currency: str | None = None,
        include_archived: bool | None = None,
        order_by: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> AddOnsListPage:
        """List add-ons

        :param include_archived: Include archived add-ons in the results (default: false)
        :param order_by: Sort order. Format: `column.direction`. Allowed columns: `name`, `created_at`. Direction: `asc` or `desc`. Default: `created_at.desc`.
        :param page: Page number (0-indexed)
        :param per_page: Number of items per page"""

        def fetch(page_param: int | None) -> AddOnListResponse:
            response = self._request(
                ApiRequest(
                    method="get",
                    path="/api/v1/addons",
                    query_params=serialize_query_params(
                        {
                            "search": search,
                            "currency": currency,
                            "include_archived": include_archived,
                            "order_by": order_by,
                            "page": page_param,
                            "per_page": per_page,
                        },
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
            return decode_response(response, AddOnListResponse)

        paging = PagePaging[AddOnListResponse, AddOn](
            items=lambda body: body.data,
            total_pages=lambda body: step(
                body.pagination_meta, lambda v: v.total_pages
            ),
            first_page=0,
        )
        return AddOnsListPage._first(fetch, page, paging)

    def create(
        self,
        *,
        name: str,
        price_id: PriceId,
        product_id: ProductId,
        description: str | None | Unset = UNSET,
        max_instances_per_subscription: int | None | Unset = UNSET,
        self_serviceable: bool | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> AddOn:
        """Create an add-on"""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/addons",
                json_body=to_json_value(
                    CreateAddOnRequest(
                        description=description,
                        max_instances_per_subscription=max_instances_per_subscription,
                        name=name,
                        price_id=price_id,
                        product_id=product_id,
                        self_serviceable=self_serviceable,
                    ),
                    CreateAddOnRequest,
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
        return decode_response(response, AddOn)

    def retrieve(
        self,
        addon_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> AddOn:
        """Get add-on details"""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/addons/{addon_id}",
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
        return decode_response(response, AddOn)

    def update(
        self,
        addon_id: str,
        *,
        description: str | None | Unset = UNSET,
        max_instances_per_subscription: int | None | Unset = UNSET,
        name: str | None | Unset = UNSET,
        price_id: PriceId | None | Unset = UNSET,
        self_serviceable: bool | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> AddOn:
        """Update an add-on"""
        response = self._request(
            ApiRequest(
                method="patch",
                path="/api/v1/addons/{addon_id}",
                path_params={
                    "addon_id": addon_id,
                },
                json_body=to_json_value(
                    UpdateAddOnRequest(
                        description=description,
                        max_instances_per_subscription=max_instances_per_subscription,
                        name=name,
                        price_id=price_id,
                        self_serviceable=self_serviceable,
                    ),
                    UpdateAddOnRequest,
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
        return decode_response(response, AddOn)

    def archive(
        self,
        addon_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Archive an add-on"""
        self._request(
            ApiRequest(
                method="post",
                path="/api/v1/addons/{addon_id}/archive",
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

    def unarchive(
        self,
        addon_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Unarchive an add-on"""
        self._request(
            ApiRequest(
                method="post",
                path="/api/v1/addons/{addon_id}/unarchive",
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


class AddOnsWithRawResponse:
    """The methods of :class:`AddOns`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AddOns) -> None:
        self._resource = resource
        self.list = to_raw_response_wrapper(resource.list)
        self.create = to_raw_response_wrapper(resource.create)
        self.retrieve = to_raw_response_wrapper(resource.retrieve)
        self.update = to_raw_response_wrapper(resource.update)
        self.archive = to_raw_response_wrapper(resource.archive)
        self.unarchive = to_raw_response_wrapper(resource.unarchive)

    @property
    def entitlements(self) -> AddOnsEntitlementsWithRawResponse:
        """The entitlements API."""
        return AddOnsEntitlementsWithRawResponse(self._resource.entitlements)
