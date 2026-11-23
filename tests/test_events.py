# this file is @generated
# ruff: noqa: I001  (where the package sorts depends on whether it is generated yet)
import unittest

from meteroid.models import IngestEventsRequest, AmendEventRequest, VoidEventRequest

from perseid_mock import call, decode, mock


class EventsTest(unittest.TestCase):
    def test_ingest(self) -> None:
        client, requests = mock(200, "application/json", "{}")
        call(
            client.events.ingest,
            body=decode(
                IngestEventsRequest,
                '{"events":[{"code":"sample","customer_id":"sample","event_id":"sample"}]}',
            ),
        )
        self.assertEqual(requests, ["POST /api/v1/events/ingest"])

    def test_amend(self) -> None:
        client, requests = mock(
            200, "application/json", '{"ingested_at":"2023-12-31T23:59:59.999-05:30"}'
        )
        call(
            client.events.amend,
            "event_id",
            body=decode(
                AmendEventRequest,
                '{"properties":{"alpha":"sample"},"timestamp":"2023-12-31T23:59:59.999-05:30"}',
            ),
        )
        self.assertEqual(requests, ["POST /api/v1/events/event_id/amend"])

    def test_void(self) -> None:
        client, requests = mock(
            200, "application/json", '{"ingested_at":"2023-12-31T23:59:59.999-05:30"}'
        )
        call(client.events.void, "event_id", body=decode(VoidEventRequest, "{}"))
        self.assertEqual(requests, ["POST /api/v1/events/event_id/void"])
