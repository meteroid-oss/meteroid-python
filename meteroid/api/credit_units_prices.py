# this file is @generated
"""Credit units prices API."""

from __future__ import annotations

import typing as t

from .. import models as _models
from ..models import (
    CreditUnitPrice,
    CreditUnitPriceListResponse,
    CreditUnitPriceSetRequest,
)
from ..serialization import UNSET, Unset, to_json_value
from ._response import async_to_raw_response_wrapper, to_raw_response_wrapper
from .common import (
    ApiBaseAsync,
    ApiBaseSync,
    ApiRequest,
    Timeout,
    decode_response,
    serialize_query_params,
)


class AsyncCreditUnitsPrices(ApiBaseAsync):
    """Credit units prices API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncCreditUnitsPricesWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncCreditUnitsPricesWithRawResponse(self)

    async def list(
        self,
        id: str,
        *,
        include_archived: bool | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreditUnitPriceListResponse:
        """List a credit unit's selling prices

        The active price per currency, and archived ones when asked, newest first.

        :param include_archived: Include archived prices. Defaults to false."""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/credit-units/{id}/prices",
                path_params={
                    "id": id,
                },
                query_params=serialize_query_params(
                    {
                        "include_archived": include_archived,
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
        return decode_response(response, CreditUnitPriceListResponse)

    async def update(
        self,
        id: str,
        currency: str,
        *,
        unit_price: str,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreditUnitPrice:
        """Set a credit unit's selling price

        The price of one credit in a currency, used to sell the unit through top-ups and automatic
        top-ups (taxed at purchase under the unit's `product_id`). Replaces the active price in that
        currency, which is archived: a top-up already priced keeps its terms.

        :param unit_price: Major units of the currency per credit, as a decimal string: positive, at most 12 decimal places."""
        response = await self._request(
            ApiRequest(
                method="put",
                path="/api/v1/credit-units/{id}/prices/{currency}",
                path_params={
                    "id": id,
                    "currency": currency,
                },
                json_body=to_json_value(
                    CreditUnitPriceSetRequest(
                        unit_price=unit_price,
                    ),
                    CreditUnitPriceSetRequest,
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
        return decode_response(response, CreditUnitPrice)

    async def archive(
        self,
        id: str,
        currency: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreditUnitPrice:
        """Remove a credit unit's selling price

        Archives the active price in a currency: the unit can no longer be sold in it (top-ups and
        automatic top-ups included) until a new price is set."""
        response = await self._request(
            ApiRequest(
                method="delete",
                path="/api/v1/credit-units/{id}/prices/{currency}",
                path_params={
                    "id": id,
                    "currency": currency,
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
        return decode_response(response, CreditUnitPrice)


class AsyncCreditUnitsPricesWithRawResponse:
    """The methods of :class:`AsyncCreditUnitsPrices`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncCreditUnitsPrices) -> None:
        self.list = async_to_raw_response_wrapper(resource.list)
        self.update = async_to_raw_response_wrapper(resource.update)
        self.archive = async_to_raw_response_wrapper(resource.archive)


class CreditUnitsPrices(ApiBaseSync):
    """Credit units prices API."""

    @property
    def with_raw_response(self) -> CreditUnitsPricesWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return CreditUnitsPricesWithRawResponse(self)

    def list(
        self,
        id: str,
        *,
        include_archived: bool | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreditUnitPriceListResponse:
        """List a credit unit's selling prices

        The active price per currency, and archived ones when asked, newest first.

        :param include_archived: Include archived prices. Defaults to false."""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/credit-units/{id}/prices",
                path_params={
                    "id": id,
                },
                query_params=serialize_query_params(
                    {
                        "include_archived": include_archived,
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
        return decode_response(response, CreditUnitPriceListResponse)

    def update(
        self,
        id: str,
        currency: str,
        *,
        unit_price: str,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreditUnitPrice:
        """Set a credit unit's selling price

        The price of one credit in a currency, used to sell the unit through top-ups and automatic
        top-ups (taxed at purchase under the unit's `product_id`). Replaces the active price in that
        currency, which is archived: a top-up already priced keeps its terms.

        :param unit_price: Major units of the currency per credit, as a decimal string: positive, at most 12 decimal places."""
        response = self._request(
            ApiRequest(
                method="put",
                path="/api/v1/credit-units/{id}/prices/{currency}",
                path_params={
                    "id": id,
                    "currency": currency,
                },
                json_body=to_json_value(
                    CreditUnitPriceSetRequest(
                        unit_price=unit_price,
                    ),
                    CreditUnitPriceSetRequest,
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
        return decode_response(response, CreditUnitPrice)

    def archive(
        self,
        id: str,
        currency: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreditUnitPrice:
        """Remove a credit unit's selling price

        Archives the active price in a currency: the unit can no longer be sold in it (top-ups and
        automatic top-ups included) until a new price is set."""
        response = self._request(
            ApiRequest(
                method="delete",
                path="/api/v1/credit-units/{id}/prices/{currency}",
                path_params={
                    "id": id,
                    "currency": currency,
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
        return decode_response(response, CreditUnitPrice)


class CreditUnitsPricesWithRawResponse:
    """The methods of :class:`CreditUnitsPrices`, returning an :class:`APIResponse`."""

    def __init__(self, resource: CreditUnitsPrices) -> None:
        self.list = to_raw_response_wrapper(resource.list)
        self.update = to_raw_response_wrapper(resource.update)
        self.archive = to_raw_response_wrapper(resource.archive)
