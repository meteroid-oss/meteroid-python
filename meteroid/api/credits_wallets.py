# this file is @generated
"""Credits wallets API."""

from __future__ import annotations

import builtins
import typing as t

from .. import models as _models
from ..models import (
    AutoTopUpWriteRequest,
    Currency,
    PatchWalletRequest,
    ProductId,
    SubscriptionId,
    UsageAtZero,
    UsageAtZeroLiteral,
    Wallet,
    WalletCheck,
    WalletListResponse,
)
from ..serialization import UNSET, Unset, to_json_value
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


class AsyncCreditsWallets(ApiBaseAsync):
    """Credits wallets API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncCreditsWalletsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncCreditsWalletsWithRawResponse(self)

    async def list(
        self,
        id_or_alias: str,
        *,
        subscription_id: SubscriptionId | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> WalletListResponse:
        """List wallets

        A customer's credit per currency and credit unit: the credit on account, the usage not
        invoiced yet and the balance left after it, with the wallet's alerts and automatic top-up. The
        customer's own currency comes first, even when empty. With `subscription_id`, each wallet
        counts only the credit that subscription can use.

        :param subscription_id: Only the credit this subscription (`sub_…`) can use: the credit that belongs to it and the customer's credit that belongs to no subscription. Every wallet is still listed."""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/customers/{id_or_alias}/wallets",
                path_params={
                    "id_or_alias": id_or_alias,
                },
                query_params=serialize_query_params(
                    {
                        "subscription_id": subscription_id,
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
        return decode_response(response, WalletListResponse)

    async def check(
        self,
        id_or_alias: str,
        *,
        currency: Currency | None = None,
        credit_unit: str | None = None,
        product_id: ProductId | None = None,
        subscription_id: SubscriptionId | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> WalletCheck:
        """Check wallet access

        Whether the customer's prepaid credit in a currency or credit unit still covers them, net of
        usage not invoiced yet. Denies only when the wallet blocks usage once its credit is used up;
        otherwise access stays allowed and `exhausted` signals the empty balance on its own. With
        `subscription_id`, only the credit that subscription can use counts: pass it when the
        customer has several subscriptions, since one subscription's credit cannot pay another's
        usage. The balance follows usage within a few seconds near zero or a threshold, within a
        minute otherwise, and the answer is cached for one second: use it to gate consumption, not
        to bill.

        :param currency: Defaults to the customer's currency.
        :param credit_unit: Checks the wallet of this credit unit (its code) instead of a currency.
        :param product_id: Checks only the credit that can pay for this product: credit not restricted to products, and credit restricted to it. Absent checks all credit.
        :param subscription_id: Checks only the credit this subscription (`sub_…`) can spend, net of its own usage no credit pays: the credit that belongs to it and the customer's credit that belongs to no subscription, once every subscription's unbilled usage is paid. `has_access` is then the decision the access gate makes for that subscription's usage. Absent checks the customer's credit as a whole."""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/customers/{id_or_alias}/wallets/check",
                path_params={
                    "id_or_alias": id_or_alias,
                },
                query_params=serialize_query_params(
                    {
                        "currency": currency,
                        "credit_unit": credit_unit,
                        "product_id": product_id,
                        "subscription_id": subscription_id,
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
        return decode_response(response, WalletCheck)

    async def update(
        self,
        id_or_alias: str,
        currency: str,
        *,
        idempotency_key: str,
        auto_top_up: AutoTopUpWriteRequest | None | Unset = UNSET,
        low_balance_thresholds: builtins.list[int] | None | Unset = UNSET,
        unit_price: str | None | Unset = UNSET,
        usage_at_zero: UsageAtZero | UsageAtZeroLiteral | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Wallet:
        """Configure a wallet

        Settings of a customer's wallet in one currency or credit unit: whether usage is refused
        once its credit is used up, the balances that fire `wallet.balance_low`, and its automatic
        top-up. Opens the wallet if it does not exist yet. Partial update: omit a field to leave it
        unchanged.

        :param low_balance_thresholds: Ascending, distinct, at most 5, non-negative. Omit to leave unchanged; an empty list clears every threshold.
        :param unit_price: Credit unit wallets: the price this customer agreed for one credit, in major units of the customer's currency, as a decimal string (positive, at most 12 decimal places). Purchases and automatic top-ups default to it instead of the list price. Omit to leave it unchanged; `null` returns the customer to the list price. A change applies to purchases quoted after it. An automatic top-up keeps running at the new price when it is at or below the price its terms were authorized at, and stops until they are confirmed again when it is above."""
        response = await self._request(
            ApiRequest(
                method="patch",
                path="/api/v1/customers/{id_or_alias}/wallets/{currency}",
                path_params={
                    "id_or_alias": id_or_alias,
                    "currency": currency,
                },
                header_params={
                    "Idempotency-Key": header_value(idempotency_key),
                },
                json_body=to_json_value(
                    PatchWalletRequest(
                        auto_top_up=auto_top_up,
                        low_balance_thresholds=low_balance_thresholds,
                        unit_price=unit_price,
                        usage_at_zero=t.cast(
                            "UsageAtZero | None | Unset", usage_at_zero
                        ),
                    ),
                    PatchWalletRequest,
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
        return decode_response(response, Wallet)


class AsyncCreditsWalletsWithRawResponse:
    """The methods of :class:`AsyncCreditsWallets`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncCreditsWallets) -> None:
        self.list = async_to_raw_response_wrapper(resource.list)
        self.check = async_to_raw_response_wrapper(resource.check)
        self.update = async_to_raw_response_wrapper(resource.update)


class CreditsWallets(ApiBaseSync):
    """Credits wallets API."""

    @property
    def with_raw_response(self) -> CreditsWalletsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return CreditsWalletsWithRawResponse(self)

    def list(
        self,
        id_or_alias: str,
        *,
        subscription_id: SubscriptionId | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> WalletListResponse:
        """List wallets

        A customer's credit per currency and credit unit: the credit on account, the usage not
        invoiced yet and the balance left after it, with the wallet's alerts and automatic top-up. The
        customer's own currency comes first, even when empty. With `subscription_id`, each wallet
        counts only the credit that subscription can use.

        :param subscription_id: Only the credit this subscription (`sub_…`) can use: the credit that belongs to it and the customer's credit that belongs to no subscription. Every wallet is still listed."""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/customers/{id_or_alias}/wallets",
                path_params={
                    "id_or_alias": id_or_alias,
                },
                query_params=serialize_query_params(
                    {
                        "subscription_id": subscription_id,
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
        return decode_response(response, WalletListResponse)

    def check(
        self,
        id_or_alias: str,
        *,
        currency: Currency | None = None,
        credit_unit: str | None = None,
        product_id: ProductId | None = None,
        subscription_id: SubscriptionId | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> WalletCheck:
        """Check wallet access

        Whether the customer's prepaid credit in a currency or credit unit still covers them, net of
        usage not invoiced yet. Denies only when the wallet blocks usage once its credit is used up;
        otherwise access stays allowed and `exhausted` signals the empty balance on its own. With
        `subscription_id`, only the credit that subscription can use counts: pass it when the
        customer has several subscriptions, since one subscription's credit cannot pay another's
        usage. The balance follows usage within a few seconds near zero or a threshold, within a
        minute otherwise, and the answer is cached for one second: use it to gate consumption, not
        to bill.

        :param currency: Defaults to the customer's currency.
        :param credit_unit: Checks the wallet of this credit unit (its code) instead of a currency.
        :param product_id: Checks only the credit that can pay for this product: credit not restricted to products, and credit restricted to it. Absent checks all credit.
        :param subscription_id: Checks only the credit this subscription (`sub_…`) can spend, net of its own usage no credit pays: the credit that belongs to it and the customer's credit that belongs to no subscription, once every subscription's unbilled usage is paid. `has_access` is then the decision the access gate makes for that subscription's usage. Absent checks the customer's credit as a whole."""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/customers/{id_or_alias}/wallets/check",
                path_params={
                    "id_or_alias": id_or_alias,
                },
                query_params=serialize_query_params(
                    {
                        "currency": currency,
                        "credit_unit": credit_unit,
                        "product_id": product_id,
                        "subscription_id": subscription_id,
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
        return decode_response(response, WalletCheck)

    def update(
        self,
        id_or_alias: str,
        currency: str,
        *,
        idempotency_key: str,
        auto_top_up: AutoTopUpWriteRequest | None | Unset = UNSET,
        low_balance_thresholds: builtins.list[int] | None | Unset = UNSET,
        unit_price: str | None | Unset = UNSET,
        usage_at_zero: UsageAtZero | UsageAtZeroLiteral | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Wallet:
        """Configure a wallet

        Settings of a customer's wallet in one currency or credit unit: whether usage is refused
        once its credit is used up, the balances that fire `wallet.balance_low`, and its automatic
        top-up. Opens the wallet if it does not exist yet. Partial update: omit a field to leave it
        unchanged.

        :param low_balance_thresholds: Ascending, distinct, at most 5, non-negative. Omit to leave unchanged; an empty list clears every threshold.
        :param unit_price: Credit unit wallets: the price this customer agreed for one credit, in major units of the customer's currency, as a decimal string (positive, at most 12 decimal places). Purchases and automatic top-ups default to it instead of the list price. Omit to leave it unchanged; `null` returns the customer to the list price. A change applies to purchases quoted after it. An automatic top-up keeps running at the new price when it is at or below the price its terms were authorized at, and stops until they are confirmed again when it is above."""
        response = self._request(
            ApiRequest(
                method="patch",
                path="/api/v1/customers/{id_or_alias}/wallets/{currency}",
                path_params={
                    "id_or_alias": id_or_alias,
                    "currency": currency,
                },
                header_params={
                    "Idempotency-Key": header_value(idempotency_key),
                },
                json_body=to_json_value(
                    PatchWalletRequest(
                        auto_top_up=auto_top_up,
                        low_balance_thresholds=low_balance_thresholds,
                        unit_price=unit_price,
                        usage_at_zero=t.cast(
                            "UsageAtZero | None | Unset", usage_at_zero
                        ),
                    ),
                    PatchWalletRequest,
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
        return decode_response(response, Wallet)


class CreditsWalletsWithRawResponse:
    """The methods of :class:`CreditsWallets`, returning an :class:`APIResponse`."""

    def __init__(self, resource: CreditsWallets) -> None:
        self.list = to_raw_response_wrapper(resource.list)
        self.check = to_raw_response_wrapper(resource.check)
        self.update = to_raw_response_wrapper(resource.update)
