# this file is @generated
"""Usage costs API."""

from __future__ import annotations

import functools

from .common import (
    ApiBaseAsync,
    ApiBaseSync,
)
from .usage_costs_customer import (
    AsyncUsageCostsCustomer,
    AsyncUsageCostsCustomerWithRawResponse,
    UsageCostsCustomer,
    UsageCostsCustomerWithRawResponse,
)
from .usage_costs_subscription import (
    AsyncUsageCostsSubscription,
    AsyncUsageCostsSubscriptionWithRawResponse,
    UsageCostsSubscription,
    UsageCostsSubscriptionWithRawResponse,
)


class AsyncUsageCosts(ApiBaseAsync):
    """Usage costs API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncUsageCostsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncUsageCostsWithRawResponse(self)

    @functools.cached_property
    def customer(self) -> AsyncUsageCostsCustomer:
        """The customer API."""
        return AsyncUsageCostsCustomer(self._cfg, self._httpx_client)

    @functools.cached_property
    def subscription(self) -> AsyncUsageCostsSubscription:
        """The subscription API."""
        return AsyncUsageCostsSubscription(self._cfg, self._httpx_client)


class AsyncUsageCostsWithRawResponse:
    """The methods of :class:`AsyncUsageCosts`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncUsageCosts) -> None:
        self._resource = resource

    @property
    def customer(self) -> AsyncUsageCostsCustomerWithRawResponse:
        """The customer API."""
        return AsyncUsageCostsCustomerWithRawResponse(self._resource.customer)

    @property
    def subscription(self) -> AsyncUsageCostsSubscriptionWithRawResponse:
        """The subscription API."""
        return AsyncUsageCostsSubscriptionWithRawResponse(self._resource.subscription)


class UsageCosts(ApiBaseSync):
    """Usage costs API."""

    @property
    def with_raw_response(self) -> UsageCostsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return UsageCostsWithRawResponse(self)

    @functools.cached_property
    def customer(self) -> UsageCostsCustomer:
        """The customer API."""
        return UsageCostsCustomer(self._cfg, self._httpx_client)

    @functools.cached_property
    def subscription(self) -> UsageCostsSubscription:
        """The subscription API."""
        return UsageCostsSubscription(self._cfg, self._httpx_client)


class UsageCostsWithRawResponse:
    """The methods of :class:`UsageCosts`, returning an :class:`APIResponse`."""

    def __init__(self, resource: UsageCosts) -> None:
        self._resource = resource

    @property
    def customer(self) -> UsageCostsCustomerWithRawResponse:
        """The customer API."""
        return UsageCostsCustomerWithRawResponse(self._resource.customer)

    @property
    def subscription(self) -> UsageCostsSubscriptionWithRawResponse:
        """The subscription API."""
        return UsageCostsSubscriptionWithRawResponse(self._resource.subscription)
