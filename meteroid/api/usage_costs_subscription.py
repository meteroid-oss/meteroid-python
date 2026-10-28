# this file is @generated
"""Usage costs subscription API."""

from __future__ import annotations

import typing as t
from datetime import datetime

from .. import models as _models
from ..models import (
    ListSubscriptionUsageCostsGranularity,
    UsageCostListResponse,
    UsageEventListResponse,
)
from ..serialization import UNSET, Unset
from ._response import async_to_raw_response_wrapper, to_raw_response_wrapper
from .common import (
    ApiBaseAsync,
    ApiBaseSync,
    ApiRequest,
    Timeout,
    decode_response,
    serialize_query_params,
)


class AsyncUsageCostsSubscription(ApiBaseAsync):
    """Usage costs subscription API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncUsageCostsSubscriptionWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncUsageCostsSubscriptionWithRawResponse(self)

    async def list_costs(
        self,
        subscription_id: str,
        *,
        metric: str,
        granularity: ListSubscriptionUsageCostsGranularity,
        from_: datetime,
        to: datetime,
        group_by: str | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> UsageCostListResponse:
        """List a subscription's usage costs over time

        The subscription's usage of one billable metric and what it costs, as for a customer but
        counting only the events the subscription bills (see its usage filter) and only its own billing
        periods. The range is at most 93 days.

        Beta: the request and response shapes of this endpoint may change before general availability.

        :param metric: Billable metric, by ID or code.
        :param group_by: Event property to split the usage by.
        :param from_: Start of the range, inclusive.
        :param to: End of the range, exclusive. At most 93 days after `from`."""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/usage/subscription/{subscription_id}/costs",
                path_params={
                    "subscription_id": subscription_id,
                },
                query_params=serialize_query_params(
                    {
                        "metric": metric,
                        "group_by": group_by,
                        "granularity": granularity,
                        "from": from_,
                        "to": to,
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
        return decode_response(response, UsageCostListResponse)

    async def list_events(
        self,
        subscription_id: str,
        *,
        metric: str,
        from_: datetime,
        to: datetime,
        cursor: str | None = None,
        limit: int | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> UsageEventListResponse:
        """List a subscription's usage events with their cost

        The events of one billable metric that the subscription bills, oldest first: with a usage
        filter, only the customer's events matching it; without, those no other subscription's filter
        claims. Costs are as for the customer's events. The range is at most 93 days.

        Beta: the request and response shapes of this endpoint may change before general availability.

        :param metric: Billable metric, by ID or code.
        :param from_: Start of the range, inclusive.
        :param to: End of the range, exclusive. At most 93 days after `from`.
        :param cursor: The `next_cursor` of the previous page.
        :param limit: Page size, 100 by default and 500 at most."""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/usage/subscription/{subscription_id}/events",
                path_params={
                    "subscription_id": subscription_id,
                },
                query_params=serialize_query_params(
                    {
                        "metric": metric,
                        "from": from_,
                        "to": to,
                        "cursor": cursor,
                        "limit": limit,
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
        return decode_response(response, UsageEventListResponse)


class AsyncUsageCostsSubscriptionWithRawResponse:
    """The methods of :class:`AsyncUsageCostsSubscription`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncUsageCostsSubscription) -> None:
        self.list_costs = async_to_raw_response_wrapper(resource.list_costs)
        self.list_events = async_to_raw_response_wrapper(resource.list_events)


class UsageCostsSubscription(ApiBaseSync):
    """Usage costs subscription API."""

    @property
    def with_raw_response(self) -> UsageCostsSubscriptionWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return UsageCostsSubscriptionWithRawResponse(self)

    def list_costs(
        self,
        subscription_id: str,
        *,
        metric: str,
        granularity: ListSubscriptionUsageCostsGranularity,
        from_: datetime,
        to: datetime,
        group_by: str | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> UsageCostListResponse:
        """List a subscription's usage costs over time

        The subscription's usage of one billable metric and what it costs, as for a customer but
        counting only the events the subscription bills (see its usage filter) and only its own billing
        periods. The range is at most 93 days.

        Beta: the request and response shapes of this endpoint may change before general availability.

        :param metric: Billable metric, by ID or code.
        :param group_by: Event property to split the usage by.
        :param from_: Start of the range, inclusive.
        :param to: End of the range, exclusive. At most 93 days after `from`."""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/usage/subscription/{subscription_id}/costs",
                path_params={
                    "subscription_id": subscription_id,
                },
                query_params=serialize_query_params(
                    {
                        "metric": metric,
                        "group_by": group_by,
                        "granularity": granularity,
                        "from": from_,
                        "to": to,
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
        return decode_response(response, UsageCostListResponse)

    def list_events(
        self,
        subscription_id: str,
        *,
        metric: str,
        from_: datetime,
        to: datetime,
        cursor: str | None = None,
        limit: int | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> UsageEventListResponse:
        """List a subscription's usage events with their cost

        The events of one billable metric that the subscription bills, oldest first: with a usage
        filter, only the customer's events matching it; without, those no other subscription's filter
        claims. Costs are as for the customer's events. The range is at most 93 days.

        Beta: the request and response shapes of this endpoint may change before general availability.

        :param metric: Billable metric, by ID or code.
        :param from_: Start of the range, inclusive.
        :param to: End of the range, exclusive. At most 93 days after `from`.
        :param cursor: The `next_cursor` of the previous page.
        :param limit: Page size, 100 by default and 500 at most."""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/usage/subscription/{subscription_id}/events",
                path_params={
                    "subscription_id": subscription_id,
                },
                query_params=serialize_query_params(
                    {
                        "metric": metric,
                        "from": from_,
                        "to": to,
                        "cursor": cursor,
                        "limit": limit,
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
        return decode_response(response, UsageEventListResponse)


class UsageCostsSubscriptionWithRawResponse:
    """The methods of :class:`UsageCostsSubscription`, returning an :class:`APIResponse`."""

    def __init__(self, resource: UsageCostsSubscription) -> None:
        self.list_costs = to_raw_response_wrapper(resource.list_costs)
        self.list_events = to_raw_response_wrapper(resource.list_events)
