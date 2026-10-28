# this file is @generated
"""Checks API."""

from __future__ import annotations

import typing as t
from decimal import Decimal

from .. import models as _models
from ..models import (
    EntitlementCheck,
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


class AsyncChecks(ApiBaseAsync):
    """Checks API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncChecksWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncChecksWithRawResponse(self)

    async def check_entitlement(
        self,
        id_or_alias: str,
        feature_id_or_code: str,
        *,
        requested: Decimal | None = None,
        subscription_id: str | None = None,
        group: dict[str, str] | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> EntitlementCheck:
        """Check customer entitlement

        Whether the customer may consume `requested` more of a feature right now, given their
        entitlement, the hard budgets that count the feature's usage, and their prepaid credit.
        Boolean features answer from their enabled state; config features grant access and return
        their `value`. An `ALLOW` limit never refuses: `in_overage` tells when the requested units go
        beyond it. Sliding windows send no threshold webhooks. Pass the group as
        `group[<property>]=<value>`: it is required when the entitlement is grouped. Pass
        `subscription_id` when the usage belongs to one subscription, so that a hard budget on another
        subscription does not refuse it.

        The answer reflects usage up to `as_of`: typically less than a minute old, and less than 10
        seconds old once `near_limit` is true. A hard limit can therefore be exceeded by the usage of
        those few seconds. While `near_limit` is true, check before every request with its actual
        `requested` and do not cache the answer; `retry_after_ms` says when to check again. Use the
        check to gate access, not to bill.

        Beta: the request and response shapes of this endpoint may change before general availability.

        :param requested: Units the customer is about to consume. Defaults to 1.
        :param subscription_id: The subscription (`sub_…`) the usage belongs to: only its own budgets and the customer-wide ones apply. Without it, a budget on one subscription refuses only once every subscription charging the feature's metric is refused by its own budget.
        :param group: The group to check, as `group[<property>]=<value>`: required when the entitlement is grouped"""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/customers/{id_or_alias}/entitlements/{feature_id_or_code}/check",
                path_params={
                    "id_or_alias": id_or_alias,
                    "feature_id_or_code": feature_id_or_code,
                },
                query_params=serialize_query_params(
                    {
                        "requested": requested,
                        "subscription_id": subscription_id,
                        "group": group,
                    },
                    structured=("group",),
                    deep_object=("group",),
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
        return decode_response(response, EntitlementCheck)


class AsyncChecksWithRawResponse:
    """The methods of :class:`AsyncChecks`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncChecks) -> None:
        self.check_entitlement = async_to_raw_response_wrapper(
            resource.check_entitlement
        )


class Checks(ApiBaseSync):
    """Checks API."""

    @property
    def with_raw_response(self) -> ChecksWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return ChecksWithRawResponse(self)

    def check_entitlement(
        self,
        id_or_alias: str,
        feature_id_or_code: str,
        *,
        requested: Decimal | None = None,
        subscription_id: str | None = None,
        group: dict[str, str] | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> EntitlementCheck:
        """Check customer entitlement

        Whether the customer may consume `requested` more of a feature right now, given their
        entitlement, the hard budgets that count the feature's usage, and their prepaid credit.
        Boolean features answer from their enabled state; config features grant access and return
        their `value`. An `ALLOW` limit never refuses: `in_overage` tells when the requested units go
        beyond it. Sliding windows send no threshold webhooks. Pass the group as
        `group[<property>]=<value>`: it is required when the entitlement is grouped. Pass
        `subscription_id` when the usage belongs to one subscription, so that a hard budget on another
        subscription does not refuse it.

        The answer reflects usage up to `as_of`: typically less than a minute old, and less than 10
        seconds old once `near_limit` is true. A hard limit can therefore be exceeded by the usage of
        those few seconds. While `near_limit` is true, check before every request with its actual
        `requested` and do not cache the answer; `retry_after_ms` says when to check again. Use the
        check to gate access, not to bill.

        Beta: the request and response shapes of this endpoint may change before general availability.

        :param requested: Units the customer is about to consume. Defaults to 1.
        :param subscription_id: The subscription (`sub_…`) the usage belongs to: only its own budgets and the customer-wide ones apply. Without it, a budget on one subscription refuses only once every subscription charging the feature's metric is refused by its own budget.
        :param group: The group to check, as `group[<property>]=<value>`: required when the entitlement is grouped"""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/customers/{id_or_alias}/entitlements/{feature_id_or_code}/check",
                path_params={
                    "id_or_alias": id_or_alias,
                    "feature_id_or_code": feature_id_or_code,
                },
                query_params=serialize_query_params(
                    {
                        "requested": requested,
                        "subscription_id": subscription_id,
                        "group": group,
                    },
                    structured=("group",),
                    deep_object=("group",),
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
        return decode_response(response, EntitlementCheck)


class ChecksWithRawResponse:
    """The methods of :class:`Checks`, returning an :class:`APIResponse`."""

    def __init__(self, resource: Checks) -> None:
        self.check_entitlement = to_raw_response_wrapper(resource.check_entitlement)
