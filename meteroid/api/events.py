# this file is @generated
"""Events API."""

from __future__ import annotations

import typing as t
from datetime import datetime

from .. import models as _models
from ..models import (
    AmendEventRequest,
    Event,
    EventChangeResponse,
    IngestEventsRequest,
    IngestEventsResponse,
    VoidEventRequest,
)
from ..serialization import UNSET, Unset, to_json_value
from ._response import async_to_raw_response_wrapper, to_raw_response_wrapper
from .common import (
    ApiBaseAsync,
    ApiBaseSync,
    ApiRequest,
    Timeout,
    decode_response,
)


class AsyncEvents(ApiBaseAsync):
    """Events API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncEventsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncEventsWithRawResponse(self)

    async def ingest(
        self,
        *,
        events: list[Event],
        allow_backfilling: bool | None | Unset = UNSET,
        allow_partial_failures: bool | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> IngestEventsResponse:
        """Ingest events

        Ingest usage events for metering and billing purposes.

        Events are deduplicated by `(event_id, customer_id)` — re-sending the same pair will not be
        double-counted. The first copy received is kept and later copies are ignored, whatever they change.

        By default, any invalid event rejects the entire batch. Set `allow_partial_failures` to `true` to ingest valid events and receive per-event failure details in the response body.

        :param allow_backfilling: Allow events with timestamps more than 1 day in the past, up to 13 months. Defaults to `false`.
        :param allow_partial_failures: Accept the batch even if some events fail validation. Defaults to `false`. When `true`, valid events are ingested and failures are reported in the response body. When `false` (default), any invalid event rejects the entire batch.
        :param events: 1–100 events per request."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/events/ingest",
                json_body=to_json_value(
                    IngestEventsRequest(
                        allow_backfilling=allow_backfilling,
                        allow_partial_failures=allow_partial_failures,
                        events=events,
                    ),
                    IngestEventsRequest,
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
        return decode_response(response, IngestEventsResponse)

    async def amend(
        self,
        event_id: str,
        *,
        properties: dict[str, str],
        timestamp: datetime,
        allow_backfilling: bool | None | Unset = UNSET,
        customer_alias: str | None | Unset = UNSET,
        customer_id: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> EventChangeResponse:
        """Amend an event

        Replaces the timestamp and the properties of an ingested event. The code and the customer
        cannot change: void the event and send a new one instead. The change is applied asynchronously,
        in order with the event's other copies.

        Only events ingested in the last 35 days can be amended, and neither their current nor their
        new timestamp can be in an invoiced period. Tenants that keep the last copy of an event correct
        it by sending it again instead.

        An event is found once metering has stored it: a just-ingested event can still return `404`.
        Wait until an amend is visible before sending the next change to the same event; concurrent
        changes resolve by `ingested_at`, the latest wins.

        :param allow_backfilling: Allow a timestamp more than 1 day in the past. Defaults to `false`.
        :param customer_alias: External customer alias of the event. Set this or `customer_id`.
        :param customer_id: Meteroid customer ID of the event. Set this or `customer_alias`.
        :param properties: The corrected properties. They replace the stored ones.
        :param timestamp: RFC 3339 timestamp of the corrected event. Must be between 24 hours ago and 1 hour from now. Set `allow_backfilling` to remove the past limit."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/events/{event_id}/amend",
                path_params={
                    "event_id": event_id,
                },
                json_body=to_json_value(
                    AmendEventRequest(
                        allow_backfilling=allow_backfilling,
                        customer_alias=customer_alias,
                        customer_id=customer_id,
                        properties=properties,
                        timestamp=timestamp,
                    ),
                    AmendEventRequest,
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
        return decode_response(response, EventChangeResponse)

    async def void(
        self,
        event_id: str,
        *,
        customer_alias: str | None | Unset = UNSET,
        customer_id: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> EventChangeResponse:
        """Void an event

        Cancels an ingested event: it no longer counts in usage. The change is applied asynchronously,
        in order with the event's other copies.

        Only events ingested in the last 35 days, outside an invoiced period, can be voided. Tenants
        that keep the last copy of an event correct it by sending it again instead.

        An event is found once metering has stored it: a just-ingested event can still return `404`,
        and so does a retried void once the first one is applied. Wait until a change is visible
        before sending the next one to the same event; concurrent changes resolve by `ingested_at`.

        :param customer_alias: External customer alias of the event. Set this or `customer_id`.
        :param customer_id: Meteroid customer ID of the event. Set this or `customer_alias`."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/events/{event_id}/void",
                path_params={
                    "event_id": event_id,
                },
                json_body=to_json_value(
                    VoidEventRequest(
                        customer_alias=customer_alias,
                        customer_id=customer_id,
                    ),
                    VoidEventRequest,
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
        return decode_response(response, EventChangeResponse)


class AsyncEventsWithRawResponse:
    """The methods of :class:`AsyncEvents`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncEvents) -> None:
        self.ingest = async_to_raw_response_wrapper(resource.ingest)
        self.amend = async_to_raw_response_wrapper(resource.amend)
        self.void = async_to_raw_response_wrapper(resource.void)


class Events(ApiBaseSync):
    """Events API."""

    @property
    def with_raw_response(self) -> EventsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return EventsWithRawResponse(self)

    def ingest(
        self,
        *,
        events: list[Event],
        allow_backfilling: bool | None | Unset = UNSET,
        allow_partial_failures: bool | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> IngestEventsResponse:
        """Ingest events

        Ingest usage events for metering and billing purposes.

        Events are deduplicated by `(event_id, customer_id)` — re-sending the same pair will not be
        double-counted. The first copy received is kept and later copies are ignored, whatever they change.

        By default, any invalid event rejects the entire batch. Set `allow_partial_failures` to `true` to ingest valid events and receive per-event failure details in the response body.

        :param allow_backfilling: Allow events with timestamps more than 1 day in the past, up to 13 months. Defaults to `false`.
        :param allow_partial_failures: Accept the batch even if some events fail validation. Defaults to `false`. When `true`, valid events are ingested and failures are reported in the response body. When `false` (default), any invalid event rejects the entire batch.
        :param events: 1–100 events per request."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/events/ingest",
                json_body=to_json_value(
                    IngestEventsRequest(
                        allow_backfilling=allow_backfilling,
                        allow_partial_failures=allow_partial_failures,
                        events=events,
                    ),
                    IngestEventsRequest,
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
        return decode_response(response, IngestEventsResponse)

    def amend(
        self,
        event_id: str,
        *,
        properties: dict[str, str],
        timestamp: datetime,
        allow_backfilling: bool | None | Unset = UNSET,
        customer_alias: str | None | Unset = UNSET,
        customer_id: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> EventChangeResponse:
        """Amend an event

        Replaces the timestamp and the properties of an ingested event. The code and the customer
        cannot change: void the event and send a new one instead. The change is applied asynchronously,
        in order with the event's other copies.

        Only events ingested in the last 35 days can be amended, and neither their current nor their
        new timestamp can be in an invoiced period. Tenants that keep the last copy of an event correct
        it by sending it again instead.

        An event is found once metering has stored it: a just-ingested event can still return `404`.
        Wait until an amend is visible before sending the next change to the same event; concurrent
        changes resolve by `ingested_at`, the latest wins.

        :param allow_backfilling: Allow a timestamp more than 1 day in the past. Defaults to `false`.
        :param customer_alias: External customer alias of the event. Set this or `customer_id`.
        :param customer_id: Meteroid customer ID of the event. Set this or `customer_alias`.
        :param properties: The corrected properties. They replace the stored ones.
        :param timestamp: RFC 3339 timestamp of the corrected event. Must be between 24 hours ago and 1 hour from now. Set `allow_backfilling` to remove the past limit."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/events/{event_id}/amend",
                path_params={
                    "event_id": event_id,
                },
                json_body=to_json_value(
                    AmendEventRequest(
                        allow_backfilling=allow_backfilling,
                        customer_alias=customer_alias,
                        customer_id=customer_id,
                        properties=properties,
                        timestamp=timestamp,
                    ),
                    AmendEventRequest,
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
        return decode_response(response, EventChangeResponse)

    def void(
        self,
        event_id: str,
        *,
        customer_alias: str | None | Unset = UNSET,
        customer_id: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> EventChangeResponse:
        """Void an event

        Cancels an ingested event: it no longer counts in usage. The change is applied asynchronously,
        in order with the event's other copies.

        Only events ingested in the last 35 days, outside an invoiced period, can be voided. Tenants
        that keep the last copy of an event correct it by sending it again instead.

        An event is found once metering has stored it: a just-ingested event can still return `404`,
        and so does a retried void once the first one is applied. Wait until a change is visible
        before sending the next one to the same event; concurrent changes resolve by `ingested_at`.

        :param customer_alias: External customer alias of the event. Set this or `customer_id`.
        :param customer_id: Meteroid customer ID of the event. Set this or `customer_alias`."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/events/{event_id}/void",
                path_params={
                    "event_id": event_id,
                },
                json_body=to_json_value(
                    VoidEventRequest(
                        customer_alias=customer_alias,
                        customer_id=customer_id,
                    ),
                    VoidEventRequest,
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
        return decode_response(response, EventChangeResponse)


class EventsWithRawResponse:
    """The methods of :class:`Events`, returning an :class:`APIResponse`."""

    def __init__(self, resource: Events) -> None:
        self.ingest = to_raw_response_wrapper(resource.ingest)
        self.amend = to_raw_response_wrapper(resource.amend)
        self.void = to_raw_response_wrapper(resource.void)
