# this file is @generated
"""Credits grants API."""

from __future__ import annotations

import builtins
import typing as t
from datetime import datetime

from .. import models as _models
from ..models import (
    CreateCreditGrantRequest,
    CreditAppliesTo,
    CreditAppliesToLiteral,
    CreditCostRequest,
    CreditGrant,
    CreditGrantListResponse,
    CreditGrantStatus,
    CreditGrantType,
    CreditGrantTypeLiteral,
    Currency,
    CurrencyLiteral,
    ProductId,
)
from ..serialization import UNSET, Unset, to_json_value
from ._pages import (
    AsyncCreditsGrantsListPage,
    CreditsGrantsListPage,
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


class AsyncCreditsGrants(ApiBaseAsync):
    """Credits grants API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncCreditsGrantsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncCreditsGrantsWithRawResponse(self)

    def list(
        self,
        id_or_alias: str,
        *,
        currency: Currency | None = None,
        credit_unit: str | None = None,
        status: CreditGrantStatus | None = None,
        subscription_id: str | None = None,
        usable_by_subscription_id: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> AsyncPaginator[CreditGrant, AsyncCreditsGrantsListPage]:
        """List credit grants

        A customer's credit grants, newest first, in every currency and credit unit unless filtered.

        :param currency: Only grants in this currency.
        :param credit_unit: Only grants in this credit unit (its code); excludes `currency`.
        :param subscription_id: Only the grants that belong to this subscription (`sub_…`); excludes `usable_by_subscription_id`.
        :param usable_by_subscription_id: Only the credit this subscription (`sub_…`) can use: its own grants and the customer's grants that belong to no subscription. Excludes `subscription_id`.
        :param page: Page number (0-indexed)
        :param per_page: Number of items per page"""

        async def fetch(page_param: int | None) -> CreditGrantListResponse:
            response = await self._request(
                ApiRequest(
                    method="get",
                    path="/api/v1/customers/{id_or_alias}/credit-grants",
                    path_params={
                        "id_or_alias": id_or_alias,
                    },
                    query_params=serialize_query_params(
                        {
                            "currency": currency,
                            "credit_unit": credit_unit,
                            "status": status,
                            "subscription_id": subscription_id,
                            "usable_by_subscription_id": usable_by_subscription_id,
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
            return decode_response(response, CreditGrantListResponse)

        paging = PagePaging[CreditGrantListResponse, CreditGrant](
            items=lambda body: body.data,
            total_pages=lambda body: step(
                body.pagination_meta, lambda v: v.total_pages
            ),
            first_page=0,
        )
        return AsyncPaginator(
            lambda: AsyncCreditsGrantsListPage._first(fetch, page, paging)
        )

    async def create(
        self,
        id_or_alias: str,
        *,
        amount: int,
        type: CreditGrantType | CreditGrantTypeLiteral,
        idempotency_key: str,
        applicable_product_ids: builtins.list[ProductId] | None | Unset = UNSET,
        applies_to: CreditAppliesTo | CreditAppliesToLiteral | None = None,
        cost: CreditCostRequest | None | Unset = UNSET,
        credit_unit: str | None | Unset = UNSET,
        currency: Currency | CurrencyLiteral | None | Unset = UNSET,
        expires_at: datetime | None | Unset = UNSET,
        priority: int | None | Unset = UNSET,
        reason: str | None | Unset = UNSET,
        reference: str | None | Unset = UNSET,
        subscription_id: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreditGrant:
        """Create a credit grant

        Grants credit without charging or invoicing: PROMOTIONAL credit for free, or PAID credit the
        customer paid for outside Meteroid ("Paid outside Meteroid"). A PAID currency grant whose
        `cost` is below its `amount` is split into a PAID grant for the cost and a PROMOTIONAL bonus
        grant for the rest, returned as `bonus_grant_id`; a `cost` above the `amount` is refused.
        For a customer of a French invoicing entity, PAID credit that cost more than zero needs a
        `reference` to the invoice or receipt of its payment. Sell credit through Meteroid with a
        top-up.

        :param amount: Credit granted, in minor units of `currency`, or of `credit_unit` when set (e.g. 500000 is 5,000.00 credits of a unit with precision 2). Positive.
        :param applicable_product_ids: Restricts the credit to charges of these products; absent applies to every product. Combined with `applies_to`. Not available for credit units.
        :param applies_to: ALL pays any charge on an invoice; USAGE only usage charges.
        :param credit_unit: Grants in this credit unit (its code) instead of a currency; excludes `currency`. Credit in a credit unit pays the usage priced in that unit, so `applies_to` must stay ALL.
        :param expires_at: When unspent credit lapses; absent never expires.
        :param priority: Lower values are drawn first among grants of the same type that pay the same charges; defaults to 100.
        :param reason: Shown on the credit ledger.
        :param reference: Your own reference, e.g. a contract or support ticket. Required for PAID credit that cost more than zero when the customer's invoicing entity is in France: the number of the invoice or receipt for the payment, as French law requires a supporting document for every accounting entry. Refused with 400 when missing.
        :param subscription_id: The customer's subscription (`sub_…`) the credit belongs to: it pays only that subscription's charges and lapses when the subscription ends. It must not have ended, and its currency must be the grant's. Absent pays any of the customer's subscriptions.
        :param type: PROMOTIONAL gives credit for free (a goodwill or marketing grant). PAID records credit the customer paid for outside of Meteroid: nothing is charged or invoiced, and the grant is shown as "Paid outside Meteroid". Usage paid with PAID currency credit is taxed on the invoice that bills it, so do not charge tax on the external sale of currency credit, or the customer is taxed twice. Credit in a credit unit is the exception: its usage is billed in credits, untaxed, so tax its sale as you would any other. Use a top-up to sell credit through Meteroid."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/customers/{id_or_alias}/credit-grants",
                path_params={
                    "id_or_alias": id_or_alias,
                },
                header_params={
                    "Idempotency-Key": header_value(idempotency_key),
                },
                json_body=to_json_value(
                    CreateCreditGrantRequest(
                        amount=amount,
                        applicable_product_ids=applicable_product_ids,
                        applies_to=t.cast("CreditAppliesTo | None", applies_to),
                        cost=cost,
                        credit_unit=credit_unit,
                        currency=t.cast("Currency | None | Unset", currency),
                        expires_at=expires_at,
                        priority=priority,
                        reason=reason,
                        reference=reference,
                        subscription_id=subscription_id,
                        type=t.cast("CreditGrantType", type),
                    ),
                    CreateCreditGrantRequest,
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
        return decode_response(response, CreditGrant)


class AsyncCreditsGrantsWithRawResponse:
    """The methods of :class:`AsyncCreditsGrants`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncCreditsGrants) -> None:
        self.list = async_to_raw_response_wrapper(resource.list)
        self.create = async_to_raw_response_wrapper(resource.create)


class CreditsGrants(ApiBaseSync):
    """Credits grants API."""

    @property
    def with_raw_response(self) -> CreditsGrantsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return CreditsGrantsWithRawResponse(self)

    def list(
        self,
        id_or_alias: str,
        *,
        currency: Currency | None = None,
        credit_unit: str | None = None,
        status: CreditGrantStatus | None = None,
        subscription_id: str | None = None,
        usable_by_subscription_id: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreditsGrantsListPage:
        """List credit grants

        A customer's credit grants, newest first, in every currency and credit unit unless filtered.

        :param currency: Only grants in this currency.
        :param credit_unit: Only grants in this credit unit (its code); excludes `currency`.
        :param subscription_id: Only the grants that belong to this subscription (`sub_…`); excludes `usable_by_subscription_id`.
        :param usable_by_subscription_id: Only the credit this subscription (`sub_…`) can use: its own grants and the customer's grants that belong to no subscription. Excludes `subscription_id`.
        :param page: Page number (0-indexed)
        :param per_page: Number of items per page"""

        def fetch(page_param: int | None) -> CreditGrantListResponse:
            response = self._request(
                ApiRequest(
                    method="get",
                    path="/api/v1/customers/{id_or_alias}/credit-grants",
                    path_params={
                        "id_or_alias": id_or_alias,
                    },
                    query_params=serialize_query_params(
                        {
                            "currency": currency,
                            "credit_unit": credit_unit,
                            "status": status,
                            "subscription_id": subscription_id,
                            "usable_by_subscription_id": usable_by_subscription_id,
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
            return decode_response(response, CreditGrantListResponse)

        paging = PagePaging[CreditGrantListResponse, CreditGrant](
            items=lambda body: body.data,
            total_pages=lambda body: step(
                body.pagination_meta, lambda v: v.total_pages
            ),
            first_page=0,
        )
        return CreditsGrantsListPage._first(fetch, page, paging)

    def create(
        self,
        id_or_alias: str,
        *,
        amount: int,
        type: CreditGrantType | CreditGrantTypeLiteral,
        idempotency_key: str,
        applicable_product_ids: builtins.list[ProductId] | None | Unset = UNSET,
        applies_to: CreditAppliesTo | CreditAppliesToLiteral | None = None,
        cost: CreditCostRequest | None | Unset = UNSET,
        credit_unit: str | None | Unset = UNSET,
        currency: Currency | CurrencyLiteral | None | Unset = UNSET,
        expires_at: datetime | None | Unset = UNSET,
        priority: int | None | Unset = UNSET,
        reason: str | None | Unset = UNSET,
        reference: str | None | Unset = UNSET,
        subscription_id: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreditGrant:
        """Create a credit grant

        Grants credit without charging or invoicing: PROMOTIONAL credit for free, or PAID credit the
        customer paid for outside Meteroid ("Paid outside Meteroid"). A PAID currency grant whose
        `cost` is below its `amount` is split into a PAID grant for the cost and a PROMOTIONAL bonus
        grant for the rest, returned as `bonus_grant_id`; a `cost` above the `amount` is refused.
        For a customer of a French invoicing entity, PAID credit that cost more than zero needs a
        `reference` to the invoice or receipt of its payment. Sell credit through Meteroid with a
        top-up.

        :param amount: Credit granted, in minor units of `currency`, or of `credit_unit` when set (e.g. 500000 is 5,000.00 credits of a unit with precision 2). Positive.
        :param applicable_product_ids: Restricts the credit to charges of these products; absent applies to every product. Combined with `applies_to`. Not available for credit units.
        :param applies_to: ALL pays any charge on an invoice; USAGE only usage charges.
        :param credit_unit: Grants in this credit unit (its code) instead of a currency; excludes `currency`. Credit in a credit unit pays the usage priced in that unit, so `applies_to` must stay ALL.
        :param expires_at: When unspent credit lapses; absent never expires.
        :param priority: Lower values are drawn first among grants of the same type that pay the same charges; defaults to 100.
        :param reason: Shown on the credit ledger.
        :param reference: Your own reference, e.g. a contract or support ticket. Required for PAID credit that cost more than zero when the customer's invoicing entity is in France: the number of the invoice or receipt for the payment, as French law requires a supporting document for every accounting entry. Refused with 400 when missing.
        :param subscription_id: The customer's subscription (`sub_…`) the credit belongs to: it pays only that subscription's charges and lapses when the subscription ends. It must not have ended, and its currency must be the grant's. Absent pays any of the customer's subscriptions.
        :param type: PROMOTIONAL gives credit for free (a goodwill or marketing grant). PAID records credit the customer paid for outside of Meteroid: nothing is charged or invoiced, and the grant is shown as "Paid outside Meteroid". Usage paid with PAID currency credit is taxed on the invoice that bills it, so do not charge tax on the external sale of currency credit, or the customer is taxed twice. Credit in a credit unit is the exception: its usage is billed in credits, untaxed, so tax its sale as you would any other. Use a top-up to sell credit through Meteroid."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/customers/{id_or_alias}/credit-grants",
                path_params={
                    "id_or_alias": id_or_alias,
                },
                header_params={
                    "Idempotency-Key": header_value(idempotency_key),
                },
                json_body=to_json_value(
                    CreateCreditGrantRequest(
                        amount=amount,
                        applicable_product_ids=applicable_product_ids,
                        applies_to=t.cast("CreditAppliesTo | None", applies_to),
                        cost=cost,
                        credit_unit=credit_unit,
                        currency=t.cast("Currency | None | Unset", currency),
                        expires_at=expires_at,
                        priority=priority,
                        reason=reason,
                        reference=reference,
                        subscription_id=subscription_id,
                        type=t.cast("CreditGrantType", type),
                    ),
                    CreateCreditGrantRequest,
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
        return decode_response(response, CreditGrant)


class CreditsGrantsWithRawResponse:
    """The methods of :class:`CreditsGrants`, returning an :class:`APIResponse`."""

    def __init__(self, resource: CreditsGrants) -> None:
        self.list = to_raw_response_wrapper(resource.list)
        self.create = to_raw_response_wrapper(resource.create)
