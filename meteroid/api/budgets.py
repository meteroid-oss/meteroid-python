# this file is @generated
"""Budgets API."""

from __future__ import annotations

import builtins
import typing as t

from .. import models as _models
from ..models import (
    Budget,
    BudgetBehavior,
    BudgetBehaviorLiteral,
    BudgetListResponse,
    CreateBudgetRequest,
    Currency,
    CurrencyLiteral,
    PatchBudgetRequest,
)
from ..serialization import UNSET, Unset, to_json_value
from ._pages import (
    AsyncBudgetsListPage,
    BudgetsListPage,
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
    header_value,
    serialize_query_params,
)


class AsyncBudgets(ApiBaseAsync):
    """Budgets API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncBudgetsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncBudgetsWithRawResponse(self)

    def list(
        self,
        id_or_alias: str,
        *,
        include_archived: bool | None = None,
        page: int | None = None,
        per_page: int | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> AsyncPaginator[Budget, AsyncBudgetsListPage]:
        """List budgets

        A customer's budgets, oldest first, with their estimated spend in the current billing period.
        Archived ones are left out unless requested.

        Beta: the request and response shapes of this endpoint may change before general availability.

        :param include_archived: Defaults to false.
        :param page: Page number (0-indexed)
        :param per_page: Number of items per page"""

        async def fetch(page_param: int | None) -> BudgetListResponse:
            response = await self._request(
                ApiRequest(
                    method="get",
                    path="/api/v1/customers/{id_or_alias}/budgets",
                    path_params={
                        "id_or_alias": id_or_alias,
                    },
                    query_params=serialize_query_params(
                        {
                            "include_archived": include_archived,
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
            return decode_response(response, BudgetListResponse)

        paging = PagePaging[BudgetListResponse, Budget](
            items=lambda body: body.data,
            total_pages=lambda body: step(
                body.pagination_meta, lambda v: v.total_pages
            ),
            first_page=0,
        )
        return AsyncPaginator(lambda: AsyncBudgetsListPage._first(fetch, page, paging))

    async def create(
        self,
        id_or_alias: str,
        *,
        amount: int,
        idempotency_key: str,
        behavior: BudgetBehavior | BudgetBehaviorLiteral | None | Unset = UNSET,
        credit_unit: str | None | Unset = UNSET,
        currency: Currency | CurrencyLiteral | None | Unset = UNSET,
        subscription_id: str | None | Unset = UNSET,
        thresholds: builtins.list[int] | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Budget:
        """Create a budget

        Sets a spending limit for one currency the customer is billed in, with alerts at percentages
        of it, on the customer's whole spend or on one subscription's. A customer has one active
        budget per currency, and per subscription.

        Beta: the request and response shapes of this endpoint may change before general availability.

        :param amount: In minor units of the currency or credit unit.
        :param credit_unit: A credit unit (its code): the budget counts the usage priced in that unit, in its minor units.
        :param subscription_id: An active subscription of the customer (`sub_…`): the budget then counts only that subscription's spend, in its currency. Absent counts the whole customer's.
        :param thresholds: Percentages of the amount (1 to 100, at most 10). Defaults to 50, 80 and 100."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/customers/{id_or_alias}/budgets",
                path_params={
                    "id_or_alias": id_or_alias,
                },
                header_params={
                    "Idempotency-Key": header_value(idempotency_key),
                },
                json_body=to_json_value(
                    CreateBudgetRequest(
                        amount=amount,
                        behavior=t.cast("BudgetBehavior | None | Unset", behavior),
                        credit_unit=credit_unit,
                        currency=t.cast("Currency | None | Unset", currency),
                        subscription_id=subscription_id,
                        thresholds=thresholds,
                    ),
                    CreateBudgetRequest,
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
        return decode_response(response, Budget)

    async def update(
        self,
        id_or_alias: str,
        budget_id: str,
        *,
        expected_version: int,
        idempotency_key: str,
        amount: int | None | Unset = UNSET,
        behavior: BudgetBehavior | BudgetBehaviorLiteral | None | Unset = UNSET,
        thresholds: builtins.list[int] | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Budget:
        """Update a budget

        Changes the amount, thresholds or behavior. Send the `version` you read as `expected_version`; a newer
        stored version, for instance after the customer edited it, is refused with 409.

        Beta: the request and response shapes of this endpoint may change before general availability.

        :param expected_version: The `version` you read; a newer stored version is refused with 409."""
        response = await self._request(
            ApiRequest(
                method="patch",
                path="/api/v1/customers/{id_or_alias}/budgets/{budget_id}",
                path_params={
                    "id_or_alias": id_or_alias,
                    "budget_id": budget_id,
                },
                header_params={
                    "Idempotency-Key": header_value(idempotency_key),
                },
                json_body=to_json_value(
                    PatchBudgetRequest(
                        amount=amount,
                        behavior=t.cast("BudgetBehavior | None | Unset", behavior),
                        expected_version=expected_version,
                        thresholds=thresholds,
                    ),
                    PatchBudgetRequest,
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
        return decode_response(response, Budget)

    async def archive(
        self,
        id_or_alias: str,
        budget_id: str,
        *,
        idempotency_key: str,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Budget:
        """Archive a budget

        Stops the budget from sending alerts and, for a HARD budget, from refusing access. Archiving an
        archived budget returns it unchanged.

        Beta: the request and response shapes of this endpoint may change before general availability."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/customers/{id_or_alias}/budgets/{budget_id}/archive",
                path_params={
                    "id_or_alias": id_or_alias,
                    "budget_id": budget_id,
                },
                header_params={
                    "Idempotency-Key": header_value(idempotency_key),
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
        return decode_response(response, Budget)


class AsyncBudgetsWithRawResponse:
    """The methods of :class:`AsyncBudgets`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncBudgets) -> None:
        self.list = async_to_raw_response_wrapper(resource.list)
        self.create = async_to_raw_response_wrapper(resource.create)
        self.update = async_to_raw_response_wrapper(resource.update)
        self.archive = async_to_raw_response_wrapper(resource.archive)


class Budgets(ApiBaseSync):
    """Budgets API."""

    @property
    def with_raw_response(self) -> BudgetsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return BudgetsWithRawResponse(self)

    def list(
        self,
        id_or_alias: str,
        *,
        include_archived: bool | None = None,
        page: int | None = None,
        per_page: int | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> BudgetsListPage:
        """List budgets

        A customer's budgets, oldest first, with their estimated spend in the current billing period.
        Archived ones are left out unless requested.

        Beta: the request and response shapes of this endpoint may change before general availability.

        :param include_archived: Defaults to false.
        :param page: Page number (0-indexed)
        :param per_page: Number of items per page"""

        def fetch(page_param: int | None) -> BudgetListResponse:
            response = self._request(
                ApiRequest(
                    method="get",
                    path="/api/v1/customers/{id_or_alias}/budgets",
                    path_params={
                        "id_or_alias": id_or_alias,
                    },
                    query_params=serialize_query_params(
                        {
                            "include_archived": include_archived,
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
            return decode_response(response, BudgetListResponse)

        paging = PagePaging[BudgetListResponse, Budget](
            items=lambda body: body.data,
            total_pages=lambda body: step(
                body.pagination_meta, lambda v: v.total_pages
            ),
            first_page=0,
        )
        return BudgetsListPage._first(fetch, page, paging)

    def create(
        self,
        id_or_alias: str,
        *,
        amount: int,
        idempotency_key: str,
        behavior: BudgetBehavior | BudgetBehaviorLiteral | None | Unset = UNSET,
        credit_unit: str | None | Unset = UNSET,
        currency: Currency | CurrencyLiteral | None | Unset = UNSET,
        subscription_id: str | None | Unset = UNSET,
        thresholds: builtins.list[int] | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Budget:
        """Create a budget

        Sets a spending limit for one currency the customer is billed in, with alerts at percentages
        of it, on the customer's whole spend or on one subscription's. A customer has one active
        budget per currency, and per subscription.

        Beta: the request and response shapes of this endpoint may change before general availability.

        :param amount: In minor units of the currency or credit unit.
        :param credit_unit: A credit unit (its code): the budget counts the usage priced in that unit, in its minor units.
        :param subscription_id: An active subscription of the customer (`sub_…`): the budget then counts only that subscription's spend, in its currency. Absent counts the whole customer's.
        :param thresholds: Percentages of the amount (1 to 100, at most 10). Defaults to 50, 80 and 100."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/customers/{id_or_alias}/budgets",
                path_params={
                    "id_or_alias": id_or_alias,
                },
                header_params={
                    "Idempotency-Key": header_value(idempotency_key),
                },
                json_body=to_json_value(
                    CreateBudgetRequest(
                        amount=amount,
                        behavior=t.cast("BudgetBehavior | None | Unset", behavior),
                        credit_unit=credit_unit,
                        currency=t.cast("Currency | None | Unset", currency),
                        subscription_id=subscription_id,
                        thresholds=thresholds,
                    ),
                    CreateBudgetRequest,
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
        return decode_response(response, Budget)

    def update(
        self,
        id_or_alias: str,
        budget_id: str,
        *,
        expected_version: int,
        idempotency_key: str,
        amount: int | None | Unset = UNSET,
        behavior: BudgetBehavior | BudgetBehaviorLiteral | None | Unset = UNSET,
        thresholds: builtins.list[int] | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Budget:
        """Update a budget

        Changes the amount, thresholds or behavior. Send the `version` you read as `expected_version`; a newer
        stored version, for instance after the customer edited it, is refused with 409.

        Beta: the request and response shapes of this endpoint may change before general availability.

        :param expected_version: The `version` you read; a newer stored version is refused with 409."""
        response = self._request(
            ApiRequest(
                method="patch",
                path="/api/v1/customers/{id_or_alias}/budgets/{budget_id}",
                path_params={
                    "id_or_alias": id_or_alias,
                    "budget_id": budget_id,
                },
                header_params={
                    "Idempotency-Key": header_value(idempotency_key),
                },
                json_body=to_json_value(
                    PatchBudgetRequest(
                        amount=amount,
                        behavior=t.cast("BudgetBehavior | None | Unset", behavior),
                        expected_version=expected_version,
                        thresholds=thresholds,
                    ),
                    PatchBudgetRequest,
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
        return decode_response(response, Budget)

    def archive(
        self,
        id_or_alias: str,
        budget_id: str,
        *,
        idempotency_key: str,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Budget:
        """Archive a budget

        Stops the budget from sending alerts and, for a HARD budget, from refusing access. Archiving an
        archived budget returns it unchanged.

        Beta: the request and response shapes of this endpoint may change before general availability."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/customers/{id_or_alias}/budgets/{budget_id}/archive",
                path_params={
                    "id_or_alias": id_or_alias,
                    "budget_id": budget_id,
                },
                header_params={
                    "Idempotency-Key": header_value(idempotency_key),
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
        return decode_response(response, Budget)


class BudgetsWithRawResponse:
    """The methods of :class:`Budgets`, returning an :class:`APIResponse`."""

    def __init__(self, resource: Budgets) -> None:
        self.list = to_raw_response_wrapper(resource.list)
        self.create = to_raw_response_wrapper(resource.create)
        self.update = to_raw_response_wrapper(resource.update)
        self.archive = to_raw_response_wrapper(resource.archive)
