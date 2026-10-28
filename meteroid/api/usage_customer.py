# this file is @generated
"""Usage customer API."""

from __future__ import annotations

import typing as t
from datetime import date

from .. import models as _models
from ..models import (
    BillableMetricId,
    UnattributedUsageResponse,
    UsageResponse,
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


class AsyncUsageCustomer(ApiBaseAsync):
    """Usage customer API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncUsageCustomerWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncUsageCustomerWithRawResponse(self)

    async def retrieve(
        self,
        customer_id: str,
        *,
        start_date: date,
        end_date: date,
        metric_id: BillableMetricId | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> UsageResponse:
        """Get customer usage

        Retrieve aggregated usage data for a customer over a specified period."""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/usage/customer/{customer_id}",
                path_params={
                    "customer_id": customer_id,
                },
                query_params=serialize_query_params(
                    {
                        "start_date": start_date,
                        "end_date": end_date,
                        "metric_id": metric_id,
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
        return decode_response(response, UsageResponse)

    async def retrieve_unattributed(
        self,
        customer_id: str,
        *,
        start_date: date | None = None,
        end_date: date | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> UnattributedUsageResponse:
        """Get unattributed usage

        Retrieve a customer's usage that no subscription bills. When subscriptions of the customer
        pricing a metric set a usage filter, events matching none of the filters are billed by a
        subscription without one; when every such subscription has a filter, those events are kept
        and reported here instead of being billed.

        :param start_date: First day of the range. Defaults to the first day of the current month (UTC).
        :param end_date: Day after the range (exclusive). Defaults to the first day of the next month."""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/usage/customer/{customer_id}/unattributed",
                path_params={
                    "customer_id": customer_id,
                },
                query_params=serialize_query_params(
                    {
                        "start_date": start_date,
                        "end_date": end_date,
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
        return decode_response(response, UnattributedUsageResponse)


class AsyncUsageCustomerWithRawResponse:
    """The methods of :class:`AsyncUsageCustomer`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncUsageCustomer) -> None:
        self.retrieve = async_to_raw_response_wrapper(resource.retrieve)
        self.retrieve_unattributed = async_to_raw_response_wrapper(
            resource.retrieve_unattributed
        )


class UsageCustomer(ApiBaseSync):
    """Usage customer API."""

    @property
    def with_raw_response(self) -> UsageCustomerWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return UsageCustomerWithRawResponse(self)

    def retrieve(
        self,
        customer_id: str,
        *,
        start_date: date,
        end_date: date,
        metric_id: BillableMetricId | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> UsageResponse:
        """Get customer usage

        Retrieve aggregated usage data for a customer over a specified period."""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/usage/customer/{customer_id}",
                path_params={
                    "customer_id": customer_id,
                },
                query_params=serialize_query_params(
                    {
                        "start_date": start_date,
                        "end_date": end_date,
                        "metric_id": metric_id,
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
        return decode_response(response, UsageResponse)

    def retrieve_unattributed(
        self,
        customer_id: str,
        *,
        start_date: date | None = None,
        end_date: date | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> UnattributedUsageResponse:
        """Get unattributed usage

        Retrieve a customer's usage that no subscription bills. When subscriptions of the customer
        pricing a metric set a usage filter, events matching none of the filters are billed by a
        subscription without one; when every such subscription has a filter, those events are kept
        and reported here instead of being billed.

        :param start_date: First day of the range. Defaults to the first day of the current month (UTC).
        :param end_date: Day after the range (exclusive). Defaults to the first day of the next month."""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/usage/customer/{customer_id}/unattributed",
                path_params={
                    "customer_id": customer_id,
                },
                query_params=serialize_query_params(
                    {
                        "start_date": start_date,
                        "end_date": end_date,
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
        return decode_response(response, UnattributedUsageResponse)


class UsageCustomerWithRawResponse:
    """The methods of :class:`UsageCustomer`, returning an :class:`APIResponse`."""

    def __init__(self, resource: UsageCustomer) -> None:
        self.retrieve = to_raw_response_wrapper(resource.retrieve)
        self.retrieve_unattributed = to_raw_response_wrapper(
            resource.retrieve_unattributed
        )
