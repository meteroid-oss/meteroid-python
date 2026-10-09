# this file is @generated
"""Webhook endpoints API."""

from __future__ import annotations

import functools
import typing as t

from .. import models as _models
from ..models import (
    WebhookDelivery,
)
from ..serialization import UNSET, Unset
from ._response import async_to_raw_response_wrapper, to_raw_response_wrapper
from .common import (
    ApiBaseAsync,
    ApiBaseSync,
    ApiRequest,
    Timeout,
    decode_response,
)
from .webhook_endpoints_endpoints import (
    AsyncWebhookEndpointsEndpoints,
    AsyncWebhookEndpointsEndpointsWithRawResponse,
    WebhookEndpointsEndpoints,
    WebhookEndpointsEndpointsWithRawResponse,
)


class AsyncWebhookEndpoints(ApiBaseAsync):
    """Webhook endpoints API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncWebhookEndpointsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncWebhookEndpointsWithRawResponse(self)

    @functools.cached_property
    def endpoints(self) -> AsyncWebhookEndpointsEndpoints:
        """The endpoints API."""
        return AsyncWebhookEndpointsEndpoints(self._cfg, self._httpx_client)

    async def resend_webhook_delivery(
        self,
        delivery_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> WebhookDelivery:
        """Resend a webhook delivery

        Re-queues the same event for the same endpoint. Fails if the endpoint is disabled."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/webhooks/deliveries/{delivery_id}/resend",
                path_params={
                    "delivery_id": delivery_id,
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
        return decode_response(response, WebhookDelivery)


class AsyncWebhookEndpointsWithRawResponse:
    """The methods of :class:`AsyncWebhookEndpoints`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncWebhookEndpoints) -> None:
        self._resource = resource
        self.resend_webhook_delivery = async_to_raw_response_wrapper(
            resource.resend_webhook_delivery
        )

    @property
    def endpoints(self) -> AsyncWebhookEndpointsEndpointsWithRawResponse:
        """The endpoints API."""
        return AsyncWebhookEndpointsEndpointsWithRawResponse(self._resource.endpoints)


class WebhookEndpoints(ApiBaseSync):
    """Webhook endpoints API."""

    @property
    def with_raw_response(self) -> WebhookEndpointsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return WebhookEndpointsWithRawResponse(self)

    @functools.cached_property
    def endpoints(self) -> WebhookEndpointsEndpoints:
        """The endpoints API."""
        return WebhookEndpointsEndpoints(self._cfg, self._httpx_client)

    def resend_webhook_delivery(
        self,
        delivery_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> WebhookDelivery:
        """Resend a webhook delivery

        Re-queues the same event for the same endpoint. Fails if the endpoint is disabled."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/webhooks/deliveries/{delivery_id}/resend",
                path_params={
                    "delivery_id": delivery_id,
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
        return decode_response(response, WebhookDelivery)


class WebhookEndpointsWithRawResponse:
    """The methods of :class:`WebhookEndpoints`, returning an :class:`APIResponse`."""

    def __init__(self, resource: WebhookEndpoints) -> None:
        self._resource = resource
        self.resend_webhook_delivery = to_raw_response_wrapper(
            resource.resend_webhook_delivery
        )

    @property
    def endpoints(self) -> WebhookEndpointsEndpointsWithRawResponse:
        """The endpoints API."""
        return WebhookEndpointsEndpointsWithRawResponse(self._resource.endpoints)
