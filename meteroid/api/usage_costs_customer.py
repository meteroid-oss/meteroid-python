# this file is @generated
"""Usage costs customer API."""

from __future__ import annotations

import typing as t
from datetime import datetime

from .. import models as _models
from ..models import (
    ListCustomerUsageCostsGranularity,
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


class AsyncUsageCostsCustomer(ApiBaseAsync):
    """Usage costs customer API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncUsageCostsCustomerWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncUsageCostsCustomerWithRawResponse(self)

    async def list_costs(
        self,
        customer_id: str,
        *,
        metric: str,
        granularity: ListCustomerUsageCostsGranularity,
        from_: datetime,
        to: datetime,
        group_by: str | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> UsageCostListResponse:
        """List a customer's usage costs over time

        A customer's usage of one billable metric and what it costs, per hour, day or month, optionally
        split by an event property, summed across the subscriptions that bill it. Buckets are cut at UTC
        boundaries and only cover the customer's billing periods. Per-unit and matrix pricing give exact
        costs. For pricing that depends on the whole period's usage (tiered, volume, package, capacity),
        a bucket's cost is what it adds to the period's price so far and `exact` is false. The range is
        at most 93 days.

        Beta: the request and response shapes of this endpoint may change before general availability.

        :param metric: Billable metric, by ID or code.
        :param group_by: Event property to split the usage by.
        :param from_: Start of the range, inclusive.
        :param to: End of the range, exclusive. At most 93 days after `from`."""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/usage/customer/{customer_id}/costs",
                path_params={
                    "customer_id": customer_id,
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
        customer_id: str,
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
        """List a customer's usage events with their cost

        A customer's events for one billable metric, oldest first, each with the units it adds and what
        they cost at the price in force. The cost is exact for per-unit and matrix pricing and absent
        for pricing that depends on the whole period's usage (tiered, volume, package, capacity) and for
        aggregations that cannot be split per event. The range is at most 93 days.

        Beta: the request and response shapes of this endpoint may change before general availability.

        :param metric: Billable metric, by ID or code.
        :param from_: Start of the range, inclusive.
        :param to: End of the range, exclusive. At most 93 days after `from`.
        :param cursor: The `next_cursor` of the previous page.
        :param limit: Page size, 100 by default and 500 at most."""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/usage/customer/{customer_id}/events",
                path_params={
                    "customer_id": customer_id,
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


class AsyncUsageCostsCustomerWithRawResponse:
    """The methods of :class:`AsyncUsageCostsCustomer`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncUsageCostsCustomer) -> None:
        self.list_costs = async_to_raw_response_wrapper(resource.list_costs)
        self.list_events = async_to_raw_response_wrapper(resource.list_events)


class UsageCostsCustomer(ApiBaseSync):
    """Usage costs customer API."""

    @property
    def with_raw_response(self) -> UsageCostsCustomerWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return UsageCostsCustomerWithRawResponse(self)

    def list_costs(
        self,
        customer_id: str,
        *,
        metric: str,
        granularity: ListCustomerUsageCostsGranularity,
        from_: datetime,
        to: datetime,
        group_by: str | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> UsageCostListResponse:
        """List a customer's usage costs over time

        A customer's usage of one billable metric and what it costs, per hour, day or month, optionally
        split by an event property, summed across the subscriptions that bill it. Buckets are cut at UTC
        boundaries and only cover the customer's billing periods. Per-unit and matrix pricing give exact
        costs. For pricing that depends on the whole period's usage (tiered, volume, package, capacity),
        a bucket's cost is what it adds to the period's price so far and `exact` is false. The range is
        at most 93 days.

        Beta: the request and response shapes of this endpoint may change before general availability.

        :param metric: Billable metric, by ID or code.
        :param group_by: Event property to split the usage by.
        :param from_: Start of the range, inclusive.
        :param to: End of the range, exclusive. At most 93 days after `from`."""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/usage/customer/{customer_id}/costs",
                path_params={
                    "customer_id": customer_id,
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
        customer_id: str,
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
        """List a customer's usage events with their cost

        A customer's events for one billable metric, oldest first, each with the units it adds and what
        they cost at the price in force. The cost is exact for per-unit and matrix pricing and absent
        for pricing that depends on the whole period's usage (tiered, volume, package, capacity) and for
        aggregations that cannot be split per event. The range is at most 93 days.

        Beta: the request and response shapes of this endpoint may change before general availability.

        :param metric: Billable metric, by ID or code.
        :param from_: Start of the range, inclusive.
        :param to: End of the range, exclusive. At most 93 days after `from`.
        :param cursor: The `next_cursor` of the previous page.
        :param limit: Page size, 100 by default and 500 at most."""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/usage/customer/{customer_id}/events",
                path_params={
                    "customer_id": customer_id,
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


class UsageCostsCustomerWithRawResponse:
    """The methods of :class:`UsageCostsCustomer`, returning an :class:`APIResponse`."""

    def __init__(self, resource: UsageCostsCustomer) -> None:
        self.list_costs = to_raw_response_wrapper(resource.list_costs)
        self.list_events = to_raw_response_wrapper(resource.list_events)
