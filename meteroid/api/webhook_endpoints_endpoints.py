# this file is @generated
"""Webhook endpoints endpoints API."""

from __future__ import annotations

import builtins
import typing as t

from .. import models as _models
from ..models import (
    CreatedWebhookEndpoint,
    CreateWebhookEndpointRequest,
    UpdateWebhookEndpointRequest,
    WebhookDelivery,
    WebhookDeliveryListResponse,
    WebhookDeliveryStatus,
    WebhookEndpoint,
    WebhookEndpointListResponse,
    WebhookEndpointSecret,
    WebhookHeaderInput,
)
from ..serialization import UNSET, Unset, to_json_value
from ._pages import (
    AsyncWebhookEndpointsEndpointsListDeliveriesPage,
    WebhookEndpointsEndpointsListDeliveriesPage,
)
from ._pagination import (
    AsyncPaginator,
    PagePaging,
    step,
)
from ._response import async_to_raw_response_wrapper, to_raw_response_wrapper
from .common import (
    ApiBaseAsync,
    ApiBaseSync,
    ApiRequest,
    Timeout,
    decode_response,
    serialize_query_params,
)


class AsyncWebhookEndpointsEndpoints(ApiBaseAsync):
    """Webhook endpoints endpoints API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncWebhookEndpointsEndpointsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncWebhookEndpointsEndpointsWithRawResponse(self)

    async def list(
        self,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> WebhookEndpointListResponse:
        """List webhook endpoints"""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/webhooks/endpoints",
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
        return decode_response(response, WebhookEndpointListResponse)

    async def create(
        self,
        *,
        url: str,
        description: str | None | Unset = UNSET,
        event_types: builtins.list[str] | None = None,
        headers: builtins.list[WebhookHeaderInput] | None = None,
        rate_limit_per_sec: int | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreatedWebhookEndpoint:
        """Create a webhook endpoint

        The signing secret is returned once, in this response only.

        :param event_types: Event types to subscribe to. Omit or leave empty to receive every event type.
        :param headers: Custom headers sent with every delivery.
        :param rate_limit_per_sec: Deliveries started per second, at most (1 to 1000).
        :param url: HTTPS destination. Private and loopback addresses are rejected unless the instance is configured to allow them."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/webhooks/endpoints",
                json_body=to_json_value(
                    CreateWebhookEndpointRequest(
                        description=description,
                        event_types=event_types,
                        headers=headers,
                        rate_limit_per_sec=rate_limit_per_sec,
                        url=url,
                    ),
                    CreateWebhookEndpointRequest,
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
        return decode_response(response, CreatedWebhookEndpoint)

    async def retrieve(
        self,
        endpoint_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> WebhookEndpoint:
        """Get a webhook endpoint"""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/webhooks/endpoints/{endpoint_id}",
                path_params={
                    "endpoint_id": endpoint_id,
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
        return decode_response(response, WebhookEndpoint)

    async def delete(
        self,
        endpoint_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Delete a webhook endpoint

        The endpoint is archived and its pending deliveries are cancelled."""
        await self._request(
            ApiRequest(
                method="delete",
                path="/api/v1/webhooks/endpoints/{endpoint_id}",
                path_params={
                    "endpoint_id": endpoint_id,
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
        endpoint_id: str,
        *,
        description: str | None | Unset = UNSET,
        disabled: bool | None | Unset = UNSET,
        event_types: builtins.list[str] | None | Unset = UNSET,
        headers: builtins.list[WebhookHeaderInput] | None | Unset = UNSET,
        rate_limit_per_sec: int | None | Unset = UNSET,
        url: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> WebhookEndpoint:
        """Update a webhook endpoint

        Omitted fields are left untouched. Re-enabling a disabled endpoint resets its
        consecutive failure count.

        :param description: Omit to leave unchanged; send `null` or an empty string to clear.
        :param disabled: Re-enabling an endpoint also resets its consecutive failure count.
        :param event_types: Replaces the subscription list. An empty array subscribes to every event type.
        :param headers: Replaces the custom header list. An empty array removes every header.
        :param rate_limit_per_sec: Omit to leave unchanged; send `null` to remove the rate limit."""
        response = await self._request(
            ApiRequest(
                method="patch",
                path="/api/v1/webhooks/endpoints/{endpoint_id}",
                path_params={
                    "endpoint_id": endpoint_id,
                },
                json_body=to_json_value(
                    UpdateWebhookEndpointRequest(
                        description=description,
                        disabled=disabled,
                        event_types=event_types,
                        headers=headers,
                        rate_limit_per_sec=rate_limit_per_sec,
                        url=url,
                    ),
                    UpdateWebhookEndpointRequest,
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
        return decode_response(response, WebhookEndpoint)

    def list_deliveries(
        self,
        endpoint_id: str,
        *,
        status: WebhookDeliveryStatus | None = None,
        page: int | None = None,
        per_page: int | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> AsyncPaginator[
        WebhookDelivery, AsyncWebhookEndpointsEndpointsListDeliveriesPage
    ]:
        """List deliveries for a webhook endpoint

        :param status: Only return deliveries in this state.
        :param page: Page number (0-indexed)
        :param per_page: Number of items per page"""

        async def fetch(page_param: int | None) -> WebhookDeliveryListResponse:
            response = await self._request(
                ApiRequest(
                    method="get",
                    path="/api/v1/webhooks/endpoints/{endpoint_id}/deliveries",
                    path_params={
                        "endpoint_id": endpoint_id,
                    },
                    query_params=serialize_query_params(
                        {
                            "status": status,
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
            return decode_response(response, WebhookDeliveryListResponse)

        paging = PagePaging[WebhookDeliveryListResponse, WebhookDelivery](
            items=lambda body: body.data,
            total_pages=lambda body: step(
                body.pagination_meta, lambda v: v.total_pages
            ),
            first_page=0,
        )
        return AsyncPaginator(
            lambda: AsyncWebhookEndpointsEndpointsListDeliveriesPage._first(
                fetch, page, paging
            )
        )

    async def rotate_secret(
        self,
        endpoint_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> WebhookEndpointSecret:
        """Rotate a webhook endpoint secret

        The previous secret keeps signing alongside the new one for 24 hours, so consumers
        can roll over without dropping events."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/webhooks/endpoints/{endpoint_id}/rotate-secret",
                path_params={
                    "endpoint_id": endpoint_id,
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
        return decode_response(response, WebhookEndpointSecret)

    async def retrieve_secret(
        self,
        endpoint_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> WebhookEndpointSecret:
        """Reveal a webhook endpoint secret"""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/webhooks/endpoints/{endpoint_id}/secret",
                path_params={
                    "endpoint_id": endpoint_id,
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
        return decode_response(response, WebhookEndpointSecret)


class AsyncWebhookEndpointsEndpointsWithRawResponse:
    """The methods of :class:`AsyncWebhookEndpointsEndpoints`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncWebhookEndpointsEndpoints) -> None:
        self.list = async_to_raw_response_wrapper(resource.list)
        self.create = async_to_raw_response_wrapper(resource.create)
        self.retrieve = async_to_raw_response_wrapper(resource.retrieve)
        self.delete = async_to_raw_response_wrapper(resource.delete)
        self.update = async_to_raw_response_wrapper(resource.update)
        self.list_deliveries = async_to_raw_response_wrapper(resource.list_deliveries)
        self.rotate_secret = async_to_raw_response_wrapper(resource.rotate_secret)
        self.retrieve_secret = async_to_raw_response_wrapper(resource.retrieve_secret)


class WebhookEndpointsEndpoints(ApiBaseSync):
    """Webhook endpoints endpoints API."""

    @property
    def with_raw_response(self) -> WebhookEndpointsEndpointsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return WebhookEndpointsEndpointsWithRawResponse(self)

    def list(
        self,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> WebhookEndpointListResponse:
        """List webhook endpoints"""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/webhooks/endpoints",
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
        return decode_response(response, WebhookEndpointListResponse)

    def create(
        self,
        *,
        url: str,
        description: str | None | Unset = UNSET,
        event_types: builtins.list[str] | None = None,
        headers: builtins.list[WebhookHeaderInput] | None = None,
        rate_limit_per_sec: int | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreatedWebhookEndpoint:
        """Create a webhook endpoint

        The signing secret is returned once, in this response only.

        :param event_types: Event types to subscribe to. Omit or leave empty to receive every event type.
        :param headers: Custom headers sent with every delivery.
        :param rate_limit_per_sec: Deliveries started per second, at most (1 to 1000).
        :param url: HTTPS destination. Private and loopback addresses are rejected unless the instance is configured to allow them."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/webhooks/endpoints",
                json_body=to_json_value(
                    CreateWebhookEndpointRequest(
                        description=description,
                        event_types=event_types,
                        headers=headers,
                        rate_limit_per_sec=rate_limit_per_sec,
                        url=url,
                    ),
                    CreateWebhookEndpointRequest,
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
        return decode_response(response, CreatedWebhookEndpoint)

    def retrieve(
        self,
        endpoint_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> WebhookEndpoint:
        """Get a webhook endpoint"""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/webhooks/endpoints/{endpoint_id}",
                path_params={
                    "endpoint_id": endpoint_id,
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
        return decode_response(response, WebhookEndpoint)

    def delete(
        self,
        endpoint_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Delete a webhook endpoint

        The endpoint is archived and its pending deliveries are cancelled."""
        self._request(
            ApiRequest(
                method="delete",
                path="/api/v1/webhooks/endpoints/{endpoint_id}",
                path_params={
                    "endpoint_id": endpoint_id,
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
        endpoint_id: str,
        *,
        description: str | None | Unset = UNSET,
        disabled: bool | None | Unset = UNSET,
        event_types: builtins.list[str] | None | Unset = UNSET,
        headers: builtins.list[WebhookHeaderInput] | None | Unset = UNSET,
        rate_limit_per_sec: int | None | Unset = UNSET,
        url: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> WebhookEndpoint:
        """Update a webhook endpoint

        Omitted fields are left untouched. Re-enabling a disabled endpoint resets its
        consecutive failure count.

        :param description: Omit to leave unchanged; send `null` or an empty string to clear.
        :param disabled: Re-enabling an endpoint also resets its consecutive failure count.
        :param event_types: Replaces the subscription list. An empty array subscribes to every event type.
        :param headers: Replaces the custom header list. An empty array removes every header.
        :param rate_limit_per_sec: Omit to leave unchanged; send `null` to remove the rate limit."""
        response = self._request(
            ApiRequest(
                method="patch",
                path="/api/v1/webhooks/endpoints/{endpoint_id}",
                path_params={
                    "endpoint_id": endpoint_id,
                },
                json_body=to_json_value(
                    UpdateWebhookEndpointRequest(
                        description=description,
                        disabled=disabled,
                        event_types=event_types,
                        headers=headers,
                        rate_limit_per_sec=rate_limit_per_sec,
                        url=url,
                    ),
                    UpdateWebhookEndpointRequest,
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
        return decode_response(response, WebhookEndpoint)

    def list_deliveries(
        self,
        endpoint_id: str,
        *,
        status: WebhookDeliveryStatus | None = None,
        page: int | None = None,
        per_page: int | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> WebhookEndpointsEndpointsListDeliveriesPage:
        """List deliveries for a webhook endpoint

        :param status: Only return deliveries in this state.
        :param page: Page number (0-indexed)
        :param per_page: Number of items per page"""

        def fetch(page_param: int | None) -> WebhookDeliveryListResponse:
            response = self._request(
                ApiRequest(
                    method="get",
                    path="/api/v1/webhooks/endpoints/{endpoint_id}/deliveries",
                    path_params={
                        "endpoint_id": endpoint_id,
                    },
                    query_params=serialize_query_params(
                        {
                            "status": status,
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
            return decode_response(response, WebhookDeliveryListResponse)

        paging = PagePaging[WebhookDeliveryListResponse, WebhookDelivery](
            items=lambda body: body.data,
            total_pages=lambda body: step(
                body.pagination_meta, lambda v: v.total_pages
            ),
            first_page=0,
        )
        return WebhookEndpointsEndpointsListDeliveriesPage._first(fetch, page, paging)

    def rotate_secret(
        self,
        endpoint_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> WebhookEndpointSecret:
        """Rotate a webhook endpoint secret

        The previous secret keeps signing alongside the new one for 24 hours, so consumers
        can roll over without dropping events."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/webhooks/endpoints/{endpoint_id}/rotate-secret",
                path_params={
                    "endpoint_id": endpoint_id,
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
        return decode_response(response, WebhookEndpointSecret)

    def retrieve_secret(
        self,
        endpoint_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> WebhookEndpointSecret:
        """Reveal a webhook endpoint secret"""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/webhooks/endpoints/{endpoint_id}/secret",
                path_params={
                    "endpoint_id": endpoint_id,
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
        return decode_response(response, WebhookEndpointSecret)


class WebhookEndpointsEndpointsWithRawResponse:
    """The methods of :class:`WebhookEndpointsEndpoints`, returning an :class:`APIResponse`."""

    def __init__(self, resource: WebhookEndpointsEndpoints) -> None:
        self.list = to_raw_response_wrapper(resource.list)
        self.create = to_raw_response_wrapper(resource.create)
        self.retrieve = to_raw_response_wrapper(resource.retrieve)
        self.delete = to_raw_response_wrapper(resource.delete)
        self.update = to_raw_response_wrapper(resource.update)
        self.list_deliveries = to_raw_response_wrapper(resource.list_deliveries)
        self.rotate_secret = to_raw_response_wrapper(resource.rotate_secret)
        self.retrieve_secret = to_raw_response_wrapper(resource.retrieve_secret)
