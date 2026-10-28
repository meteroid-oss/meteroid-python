# this file is @generated
"""Credit units API."""

from __future__ import annotations

import functools
import typing as t

from .. import models as _models
from ..models import (
    CreditUnit,
    CreditUnitCreateRequest,
    CreditUnitListResponse,
    CreditUnitUpdateRequest,
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
from .credit_units_prices import (
    AsyncCreditUnitsPrices,
    AsyncCreditUnitsPricesWithRawResponse,
    CreditUnitsPrices,
    CreditUnitsPricesWithRawResponse,
)


class AsyncCreditUnits(ApiBaseAsync):
    """Credit units API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncCreditUnitsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncCreditUnitsWithRawResponse(self)

    @functools.cached_property
    def prices(self) -> AsyncCreditUnitsPrices:
        """The prices API."""
        return AsyncCreditUnitsPrices(self._cfg, self._httpx_client)

    async def list(
        self,
        *,
        include_archived: bool | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreditUnitListResponse:
        """List credit units

        The tenant's credit units (e.g. "Halyard credits"): denominations usage can be priced and
        credit granted in, instead of money, each with its selling prices.

        :param include_archived: Include archived units. Defaults to false."""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/credit-units",
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
        return decode_response(response, CreditUnitListResponse)

    async def create(
        self,
        *,
        code: str,
        name: str,
        plural_name: str,
        precision: int,
        symbol: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreditUnit:
        """Create a credit unit

        `code` and `precision` are immutable once created. Price usage in the unit with a plan fee's
        `credit_unit`, grant it with a credit pack or a credit grant, and sell it with a top-up once
        it has a `product_id` and a selling price.

        :param code: Immutable once created: 4 to 16 characters, A-Z/0-9/_, starting with a letter. Never an ISO currency code (those are always 3 letters).
        :param name: Singular display name, 1 to 64 characters, e.g. "Credit".
        :param plural_name: Plural display name, 1 to 64 characters, e.g. "Credits".
        :param precision: Immutable once created: 0 to 6.
        :param symbol: Short display symbol, at most 8 characters."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/credit-units",
                json_body=to_json_value(
                    CreditUnitCreateRequest(
                        code=code,
                        name=name,
                        plural_name=plural_name,
                        precision=precision,
                        symbol=symbol,
                    ),
                    CreditUnitCreateRequest,
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
        return decode_response(response, CreditUnit)

    async def retrieve(
        self,
        id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreditUnit:
        """Get a credit unit

        The unit with its active selling prices."""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/credit-units/{id}",
                path_params={
                    "id": id,
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
        return decode_response(response, CreditUnit)

    async def update(
        self,
        id: str,
        *,
        archived: bool | None | Unset = UNSET,
        name: str | None | Unset = UNSET,
        plural_name: str | None | Unset = UNSET,
        product_id: str | None | Unset = UNSET,
        symbol: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreditUnit:
        """Update a credit unit

        Partial update: an absent field is left unchanged. `code` and `precision` are immutable and
        cannot be changed here. Setting `archived: true` blocks the unit from new prices, packs and
        grants; existing ones keep working.

        :param archived: Blocks the unit from new prices, packs and grants; existing ones keep working.
        :param name: Singular display name, 1 to 64 characters.
        :param plural_name: Plural display name, 1 to 64 characters.
        :param product_id: The product sales of the unit are booked under; `null` clears it, which stops the unit from being sold.
        :param symbol: Validated by the store (trimmed, at most 8 characters) rather than here: `validator` has no built-in support for a double `Option`."""
        response = await self._request(
            ApiRequest(
                method="patch",
                path="/api/v1/credit-units/{id}",
                path_params={
                    "id": id,
                },
                json_body=to_json_value(
                    CreditUnitUpdateRequest(
                        archived=archived,
                        name=name,
                        plural_name=plural_name,
                        product_id=product_id,
                        symbol=symbol,
                    ),
                    CreditUnitUpdateRequest,
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
        return decode_response(response, CreditUnit)


class AsyncCreditUnitsWithRawResponse:
    """The methods of :class:`AsyncCreditUnits`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncCreditUnits) -> None:
        self._resource = resource
        self.list = async_to_raw_response_wrapper(resource.list)
        self.create = async_to_raw_response_wrapper(resource.create)
        self.retrieve = async_to_raw_response_wrapper(resource.retrieve)
        self.update = async_to_raw_response_wrapper(resource.update)

    @property
    def prices(self) -> AsyncCreditUnitsPricesWithRawResponse:
        """The prices API."""
        return AsyncCreditUnitsPricesWithRawResponse(self._resource.prices)


class CreditUnits(ApiBaseSync):
    """Credit units API."""

    @property
    def with_raw_response(self) -> CreditUnitsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return CreditUnitsWithRawResponse(self)

    @functools.cached_property
    def prices(self) -> CreditUnitsPrices:
        """The prices API."""
        return CreditUnitsPrices(self._cfg, self._httpx_client)

    def list(
        self,
        *,
        include_archived: bool | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreditUnitListResponse:
        """List credit units

        The tenant's credit units (e.g. "Halyard credits"): denominations usage can be priced and
        credit granted in, instead of money, each with its selling prices.

        :param include_archived: Include archived units. Defaults to false."""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/credit-units",
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
        return decode_response(response, CreditUnitListResponse)

    def create(
        self,
        *,
        code: str,
        name: str,
        plural_name: str,
        precision: int,
        symbol: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreditUnit:
        """Create a credit unit

        `code` and `precision` are immutable once created. Price usage in the unit with a plan fee's
        `credit_unit`, grant it with a credit pack or a credit grant, and sell it with a top-up once
        it has a `product_id` and a selling price.

        :param code: Immutable once created: 4 to 16 characters, A-Z/0-9/_, starting with a letter. Never an ISO currency code (those are always 3 letters).
        :param name: Singular display name, 1 to 64 characters, e.g. "Credit".
        :param plural_name: Plural display name, 1 to 64 characters, e.g. "Credits".
        :param precision: Immutable once created: 0 to 6.
        :param symbol: Short display symbol, at most 8 characters."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/credit-units",
                json_body=to_json_value(
                    CreditUnitCreateRequest(
                        code=code,
                        name=name,
                        plural_name=plural_name,
                        precision=precision,
                        symbol=symbol,
                    ),
                    CreditUnitCreateRequest,
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
        return decode_response(response, CreditUnit)

    def retrieve(
        self,
        id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreditUnit:
        """Get a credit unit

        The unit with its active selling prices."""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/credit-units/{id}",
                path_params={
                    "id": id,
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
        return decode_response(response, CreditUnit)

    def update(
        self,
        id: str,
        *,
        archived: bool | None | Unset = UNSET,
        name: str | None | Unset = UNSET,
        plural_name: str | None | Unset = UNSET,
        product_id: str | None | Unset = UNSET,
        symbol: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreditUnit:
        """Update a credit unit

        Partial update: an absent field is left unchanged. `code` and `precision` are immutable and
        cannot be changed here. Setting `archived: true` blocks the unit from new prices, packs and
        grants; existing ones keep working.

        :param archived: Blocks the unit from new prices, packs and grants; existing ones keep working.
        :param name: Singular display name, 1 to 64 characters.
        :param plural_name: Plural display name, 1 to 64 characters.
        :param product_id: The product sales of the unit are booked under; `null` clears it, which stops the unit from being sold.
        :param symbol: Validated by the store (trimmed, at most 8 characters) rather than here: `validator` has no built-in support for a double `Option`."""
        response = self._request(
            ApiRequest(
                method="patch",
                path="/api/v1/credit-units/{id}",
                path_params={
                    "id": id,
                },
                json_body=to_json_value(
                    CreditUnitUpdateRequest(
                        archived=archived,
                        name=name,
                        plural_name=plural_name,
                        product_id=product_id,
                        symbol=symbol,
                    ),
                    CreditUnitUpdateRequest,
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
        return decode_response(response, CreditUnit)


class CreditUnitsWithRawResponse:
    """The methods of :class:`CreditUnits`, returning an :class:`APIResponse`."""

    def __init__(self, resource: CreditUnits) -> None:
        self._resource = resource
        self.list = to_raw_response_wrapper(resource.list)
        self.create = to_raw_response_wrapper(resource.create)
        self.retrieve = to_raw_response_wrapper(resource.retrieve)
        self.update = to_raw_response_wrapper(resource.update)

    @property
    def prices(self) -> CreditUnitsPricesWithRawResponse:
        """The prices API."""
        return CreditUnitsPricesWithRawResponse(self._resource.prices)
