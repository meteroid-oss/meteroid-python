# this file is @generated
"""Credits API."""

from __future__ import annotations

import functools
import typing as t
from datetime import datetime

from .. import models as _models
from ..models import (
    CreateTopUpRequest,
    Currency,
    CurrencyLiteral,
    LedgerEntry,
    LedgerListResponse,
    TopUpCollection,
    TopUpCollectionLiteral,
    TopUpResponse,
)
from ..serialization import UNSET, Unset, to_json_value
from ._pages import (
    AsyncCreditsListCustomerCreditLedgerPage,
    CreditsListCustomerCreditLedgerPage,
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
from .credits_grants import (
    AsyncCreditsGrants,
    AsyncCreditsGrantsWithRawResponse,
    CreditsGrants,
    CreditsGrantsWithRawResponse,
)
from .credits_wallets import (
    AsyncCreditsWallets,
    AsyncCreditsWalletsWithRawResponse,
    CreditsWallets,
    CreditsWalletsWithRawResponse,
)


class AsyncCredits(ApiBaseAsync):
    """Credits API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncCreditsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncCreditsWithRawResponse(self)

    @functools.cached_property
    def grants(self) -> AsyncCreditsGrants:
        """The grants API."""
        return AsyncCreditsGrants(self._cfg, self._httpx_client)

    @functools.cached_property
    def wallets(self) -> AsyncCreditsWallets:
        """The wallets API."""
        return AsyncCreditsWallets(self._cfg, self._httpx_client)

    def list_customer_credit_ledger(
        self,
        id_or_alias: str,
        *,
        currency: Currency | None = None,
        credit_unit: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> AsyncPaginator[LedgerEntry, AsyncCreditsListCustomerCreditLedgerPage]:
        """List credit ledger entries

        Every movement of a customer's credit in one currency or credit unit, newest first, with the
        credit on account after it: credit granted, applied to invoices, given back, expired or
        rolled over.

        :param currency: Defaults to the customer's currency.
        :param credit_unit: The ledger of this credit unit (its code) instead of a currency; excludes `currency`.
        :param page: Page number (0-indexed)
        :param per_page: Number of items per page"""

        async def fetch(page_param: int | None) -> LedgerListResponse:
            response = await self._request(
                ApiRequest(
                    method="get",
                    path="/api/v1/customers/{id_or_alias}/credit-ledger",
                    path_params={
                        "id_or_alias": id_or_alias,
                    },
                    query_params=serialize_query_params(
                        {
                            "currency": currency,
                            "credit_unit": credit_unit,
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
            return decode_response(response, LedgerListResponse)

        paging = PagePaging[LedgerListResponse, LedgerEntry](
            items=lambda body: body.data,
            total_pages=lambda body: step(
                body.pagination_meta, lambda v: v.total_pages
            ),
            first_page=0,
        )
        return AsyncPaginator(
            lambda: AsyncCreditsListCustomerCreditLedgerPage._first(fetch, page, paging)
        )

    async def create_customer_top_up(
        self,
        id_or_alias: str,
        *,
        amount: int,
        idempotency_key: str,
        collection: TopUpCollection | TopUpCollectionLiteral | None = None,
        credit_unit: str | None | Unset = UNSET,
        currency: Currency | CurrencyLiteral | None | Unset = UNSET,
        expires_at: datetime | None | Unset = UNSET,
        payment_method_id: str | None | Unset = UNSET,
        unit_price: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> TopUpResponse:
        """Create a top-up

        Sells credit: CHARGE bills a saved payment method now, SEND_INVOICE grants it once paid. The
        credit is PAID and applies to ALL charges. Currency credit is sold one for one, untaxed, as
        its usage is taxed when invoiced. With `credit_unit`, sells credits of that unit at its
        selling price in the customer's currency, taxed at purchase under the unit's product; refused
        when the unit has no price in that currency or no product. Without a saved payment method,
        CHARGE returns a hosted `checkout_url` where the customer pays.

        :param amount: Credit to buy, positive, applying to ALL charges. In minor units of `currency`, charged one for one without tax: the usage it pays is taxed on the invoice that bills it. With `credit_unit`, in minor units of that unit (e.g. 500000 is 5,000.00 credits of a unit with precision 2), charged at the unit's price per credit in the customer's currency, plus tax under the unit's product.
        :param collection: CHARGE (default) charges a saved payment method now; SEND_INVOICE issues an invoice and grants the credit once it is paid.
        :param credit_unit: Buy credits of this credit unit (its code) instead of money; excludes `currency`. They are charged in the customer's currency at the customer's agreed price for the unit (the wallet's `unit_price`), else its list price, plus tax, under the unit's product.
        :param expires_at: Absolute expiry of the purchased credit; unset never expires.
        :param payment_method_id: CHARGE only; defaults to the customer's default payment method.
        :param unit_price: With `credit_unit`: the negotiated price of one credit for this purchase, in major units of the customer's currency, as a decimal string (e.g. "0.0008"). Defaults to the wallet's `unit_price` when set, else the list price; the unit must still have a list price in that currency."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/customers/{id_or_alias}/top-ups",
                path_params={
                    "id_or_alias": id_or_alias,
                },
                header_params={
                    "Idempotency-Key": header_value(idempotency_key),
                },
                json_body=to_json_value(
                    CreateTopUpRequest(
                        amount=amount,
                        collection=t.cast("TopUpCollection | None", collection),
                        credit_unit=credit_unit,
                        currency=t.cast("Currency | None | Unset", currency),
                        expires_at=expires_at,
                        payment_method_id=payment_method_id,
                        unit_price=unit_price,
                    ),
                    CreateTopUpRequest,
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
        return decode_response(response, TopUpResponse)


class AsyncCreditsWithRawResponse:
    """The methods of :class:`AsyncCredits`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncCredits) -> None:
        self._resource = resource
        self.list_customer_credit_ledger = async_to_raw_response_wrapper(
            resource.list_customer_credit_ledger
        )
        self.create_customer_top_up = async_to_raw_response_wrapper(
            resource.create_customer_top_up
        )

    @property
    def grants(self) -> AsyncCreditsGrantsWithRawResponse:
        """The grants API."""
        return AsyncCreditsGrantsWithRawResponse(self._resource.grants)

    @property
    def wallets(self) -> AsyncCreditsWalletsWithRawResponse:
        """The wallets API."""
        return AsyncCreditsWalletsWithRawResponse(self._resource.wallets)


class Credits(ApiBaseSync):
    """Credits API."""

    @property
    def with_raw_response(self) -> CreditsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return CreditsWithRawResponse(self)

    @functools.cached_property
    def grants(self) -> CreditsGrants:
        """The grants API."""
        return CreditsGrants(self._cfg, self._httpx_client)

    @functools.cached_property
    def wallets(self) -> CreditsWallets:
        """The wallets API."""
        return CreditsWallets(self._cfg, self._httpx_client)

    def list_customer_credit_ledger(
        self,
        id_or_alias: str,
        *,
        currency: Currency | None = None,
        credit_unit: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreditsListCustomerCreditLedgerPage:
        """List credit ledger entries

        Every movement of a customer's credit in one currency or credit unit, newest first, with the
        credit on account after it: credit granted, applied to invoices, given back, expired or
        rolled over.

        :param currency: Defaults to the customer's currency.
        :param credit_unit: The ledger of this credit unit (its code) instead of a currency; excludes `currency`.
        :param page: Page number (0-indexed)
        :param per_page: Number of items per page"""

        def fetch(page_param: int | None) -> LedgerListResponse:
            response = self._request(
                ApiRequest(
                    method="get",
                    path="/api/v1/customers/{id_or_alias}/credit-ledger",
                    path_params={
                        "id_or_alias": id_or_alias,
                    },
                    query_params=serialize_query_params(
                        {
                            "currency": currency,
                            "credit_unit": credit_unit,
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
            return decode_response(response, LedgerListResponse)

        paging = PagePaging[LedgerListResponse, LedgerEntry](
            items=lambda body: body.data,
            total_pages=lambda body: step(
                body.pagination_meta, lambda v: v.total_pages
            ),
            first_page=0,
        )
        return CreditsListCustomerCreditLedgerPage._first(fetch, page, paging)

    def create_customer_top_up(
        self,
        id_or_alias: str,
        *,
        amount: int,
        idempotency_key: str,
        collection: TopUpCollection | TopUpCollectionLiteral | None = None,
        credit_unit: str | None | Unset = UNSET,
        currency: Currency | CurrencyLiteral | None | Unset = UNSET,
        expires_at: datetime | None | Unset = UNSET,
        payment_method_id: str | None | Unset = UNSET,
        unit_price: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> TopUpResponse:
        """Create a top-up

        Sells credit: CHARGE bills a saved payment method now, SEND_INVOICE grants it once paid. The
        credit is PAID and applies to ALL charges. Currency credit is sold one for one, untaxed, as
        its usage is taxed when invoiced. With `credit_unit`, sells credits of that unit at its
        selling price in the customer's currency, taxed at purchase under the unit's product; refused
        when the unit has no price in that currency or no product. Without a saved payment method,
        CHARGE returns a hosted `checkout_url` where the customer pays.

        :param amount: Credit to buy, positive, applying to ALL charges. In minor units of `currency`, charged one for one without tax: the usage it pays is taxed on the invoice that bills it. With `credit_unit`, in minor units of that unit (e.g. 500000 is 5,000.00 credits of a unit with precision 2), charged at the unit's price per credit in the customer's currency, plus tax under the unit's product.
        :param collection: CHARGE (default) charges a saved payment method now; SEND_INVOICE issues an invoice and grants the credit once it is paid.
        :param credit_unit: Buy credits of this credit unit (its code) instead of money; excludes `currency`. They are charged in the customer's currency at the customer's agreed price for the unit (the wallet's `unit_price`), else its list price, plus tax, under the unit's product.
        :param expires_at: Absolute expiry of the purchased credit; unset never expires.
        :param payment_method_id: CHARGE only; defaults to the customer's default payment method.
        :param unit_price: With `credit_unit`: the negotiated price of one credit for this purchase, in major units of the customer's currency, as a decimal string (e.g. "0.0008"). Defaults to the wallet's `unit_price` when set, else the list price; the unit must still have a list price in that currency."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/customers/{id_or_alias}/top-ups",
                path_params={
                    "id_or_alias": id_or_alias,
                },
                header_params={
                    "Idempotency-Key": header_value(idempotency_key),
                },
                json_body=to_json_value(
                    CreateTopUpRequest(
                        amount=amount,
                        collection=t.cast("TopUpCollection | None", collection),
                        credit_unit=credit_unit,
                        currency=t.cast("Currency | None | Unset", currency),
                        expires_at=expires_at,
                        payment_method_id=payment_method_id,
                        unit_price=unit_price,
                    ),
                    CreateTopUpRequest,
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
        return decode_response(response, TopUpResponse)


class CreditsWithRawResponse:
    """The methods of :class:`Credits`, returning an :class:`APIResponse`."""

    def __init__(self, resource: Credits) -> None:
        self._resource = resource
        self.list_customer_credit_ledger = to_raw_response_wrapper(
            resource.list_customer_credit_ledger
        )
        self.create_customer_top_up = to_raw_response_wrapper(
            resource.create_customer_top_up
        )

    @property
    def grants(self) -> CreditsGrantsWithRawResponse:
        """The grants API."""
        return CreditsGrantsWithRawResponse(self._resource.grants)

    @property
    def wallets(self) -> CreditsWalletsWithRawResponse:
        """The wallets API."""
        return CreditsWalletsWithRawResponse(self._resource.wallets)
