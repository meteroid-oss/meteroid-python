# this file is @generated
"""Invoices payments API."""

from __future__ import annotations

import typing as t
from datetime import datetime

from .. import models as _models
from ..models import (
    RecordInvoicePaymentRequest,
    ReversalKind,
    ReversalKindLiteral,
    ReverseInvoicePaymentRequest,
    Transaction,
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
)


class AsyncInvoicesPayments(ApiBaseAsync):
    """Invoices payments API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncInvoicesPaymentsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncInvoicesPaymentsWithRawResponse(self)

    async def create(
        self,
        invoice_id: str,
        *,
        amount: int,
        idempotency_key: str,
        paid_at: datetime | None | Unset = UNSET,
        reference: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Transaction:
        """Record an invoice payment

        Record a partial or full payment received outside Meteroid against a finalized invoice.
        Paying the remaining balance marks the invoice paid.

        :param amount: The positive amount received, in minor units of the invoice currency (e.g. cents).
        :param paid_at: When the payment was received, at most a day ahead. Defaults to the current time.
        :param reference: Reference for the external payment, such as a bank transfer ID."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/invoices/{invoice_id}/payments",
                path_params={
                    "invoice_id": invoice_id,
                },
                header_params={
                    "Idempotency-Key": header_value(idempotency_key),
                },
                json_body=to_json_value(
                    RecordInvoicePaymentRequest(
                        amount=amount,
                        paid_at=paid_at,
                        reference=reference,
                    ),
                    RecordInvoicePaymentRequest,
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
        return decode_response(response, Transaction)

    async def reverse(
        self,
        invoice_id: str,
        transaction_id: str,
        *,
        kind: ReversalKind | ReversalKindLiteral,
        idempotency_key: str,
        reason: str | None | Unset = UNSET,
        reversed_at: datetime | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Transaction:
        """Reverse an invoice payment

        Record the full reversal of a settled manual payment.

        :param kind: `CHARGEBACK`, `DEBTOR_RECALL` and `DISPUTE` leave the invoice paid and mark the payment disputed. Any other kind makes the amount due again.
        :param reason: Additional details about the reversal.
        :param reversed_at: When the reversal occurred, at most a day ahead. Defaults to the current time."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/invoices/{invoice_id}/payments/{transaction_id}/reverse",
                path_params={
                    "invoice_id": invoice_id,
                    "transaction_id": transaction_id,
                },
                header_params={
                    "Idempotency-Key": header_value(idempotency_key),
                },
                json_body=to_json_value(
                    ReverseInvoicePaymentRequest(
                        kind=t.cast("ReversalKind", kind),
                        reason=reason,
                        reversed_at=reversed_at,
                    ),
                    ReverseInvoicePaymentRequest,
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
        return decode_response(response, Transaction)


class AsyncInvoicesPaymentsWithRawResponse:
    """The methods of :class:`AsyncInvoicesPayments`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncInvoicesPayments) -> None:
        self.create = async_to_raw_response_wrapper(resource.create)
        self.reverse = async_to_raw_response_wrapper(resource.reverse)


class InvoicesPayments(ApiBaseSync):
    """Invoices payments API."""

    @property
    def with_raw_response(self) -> InvoicesPaymentsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return InvoicesPaymentsWithRawResponse(self)

    def create(
        self,
        invoice_id: str,
        *,
        amount: int,
        idempotency_key: str,
        paid_at: datetime | None | Unset = UNSET,
        reference: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Transaction:
        """Record an invoice payment

        Record a partial or full payment received outside Meteroid against a finalized invoice.
        Paying the remaining balance marks the invoice paid.

        :param amount: The positive amount received, in minor units of the invoice currency (e.g. cents).
        :param paid_at: When the payment was received, at most a day ahead. Defaults to the current time.
        :param reference: Reference for the external payment, such as a bank transfer ID."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/invoices/{invoice_id}/payments",
                path_params={
                    "invoice_id": invoice_id,
                },
                header_params={
                    "Idempotency-Key": header_value(idempotency_key),
                },
                json_body=to_json_value(
                    RecordInvoicePaymentRequest(
                        amount=amount,
                        paid_at=paid_at,
                        reference=reference,
                    ),
                    RecordInvoicePaymentRequest,
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
        return decode_response(response, Transaction)

    def reverse(
        self,
        invoice_id: str,
        transaction_id: str,
        *,
        kind: ReversalKind | ReversalKindLiteral,
        idempotency_key: str,
        reason: str | None | Unset = UNSET,
        reversed_at: datetime | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Transaction:
        """Reverse an invoice payment

        Record the full reversal of a settled manual payment.

        :param kind: `CHARGEBACK`, `DEBTOR_RECALL` and `DISPUTE` leave the invoice paid and mark the payment disputed. Any other kind makes the amount due again.
        :param reason: Additional details about the reversal.
        :param reversed_at: When the reversal occurred, at most a day ahead. Defaults to the current time."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/invoices/{invoice_id}/payments/{transaction_id}/reverse",
                path_params={
                    "invoice_id": invoice_id,
                    "transaction_id": transaction_id,
                },
                header_params={
                    "Idempotency-Key": header_value(idempotency_key),
                },
                json_body=to_json_value(
                    ReverseInvoicePaymentRequest(
                        kind=t.cast("ReversalKind", kind),
                        reason=reason,
                        reversed_at=reversed_at,
                    ),
                    ReverseInvoicePaymentRequest,
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
        return decode_response(response, Transaction)


class InvoicesPaymentsWithRawResponse:
    """The methods of :class:`InvoicesPayments`, returning an :class:`APIResponse`."""

    def __init__(self, resource: InvoicesPayments) -> None:
        self.create = to_raw_response_wrapper(resource.create)
        self.reverse = to_raw_response_wrapper(resource.reverse)
