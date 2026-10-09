# this file is @generated
# ruff: noqa: I001  (where the package sorts depends on whether it is generated yet)
import unittest

from meteroid.models import CreateWebhookEndpointRequest, UpdateWebhookEndpointRequest

from perseid_mock import call, decode, mock


class WebhookEndpointsEndpointsTest(unittest.TestCase):
    def test_list(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"data":[{"consecutive_failures":-123456789,"created_at":"2023-12-31T23:59:59.999-05:30","disabled":true,"event_types":["sample"],"headers":[{"name":"sample","sensitive":false,"set":true}],"id":"webhook_endpoint_id_25","max_in_flight":-2147483648,"needs_setup":false,"url":"sample"}]}',
        )
        call(client.webhook_endpoints.endpoints.list)
        self.assertEqual(requests, ["GET /api/v1/webhooks/endpoints"])

    def test_create(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"consecutive_failures":-123456789,"created_at":"2023-12-31T23:59:59.999-05:30","disabled":true,"event_types":["sample"],"headers":[{"name":"sample","sensitive":false,"set":true}],"id":"webhook_endpoint_id_25","max_in_flight":-2147483648,"needs_setup":false,"url":"sample","secret":"sample"}',
        )
        call(
            client.webhook_endpoints.endpoints.create,
            body=decode(CreateWebhookEndpointRequest, '{"url":"sample"}'),
        )
        self.assertEqual(requests, ["POST /api/v1/webhooks/endpoints"])

    def test_retrieve(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"consecutive_failures":-2147483648,"created_at":"2024-03-15T10:30:45.123+02:00","disabled":true,"event_types":["sample"],"headers":[{"name":"sample","sensitive":true,"set":true}],"id":"webhook_endpoint_id_40","max_in_flight":-123456789,"needs_setup":true,"url":"sample"}',
        )
        call(client.webhook_endpoints.endpoints.retrieve, "endpoint_id")
        self.assertEqual(requests, ["GET /api/v1/webhooks/endpoints/endpoint_id"])

    def test_delete(self) -> None:
        client, requests = mock(204, None, "")
        call(client.webhook_endpoints.endpoints.delete, "endpoint_id")
        self.assertEqual(requests, ["DELETE /api/v1/webhooks/endpoints/endpoint_id"])

    def test_update(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"consecutive_failures":-2147483648,"created_at":"2024-03-15T10:30:45.123+02:00","disabled":true,"event_types":["sample"],"headers":[{"name":"sample","sensitive":true,"set":true}],"id":"webhook_endpoint_id_40","max_in_flight":-123456789,"needs_setup":true,"url":"sample"}',
        )
        call(
            client.webhook_endpoints.endpoints.update,
            "endpoint_id",
            body=decode(UpdateWebhookEndpointRequest, "{}"),
        )
        self.assertEqual(requests, ["PATCH /api/v1/webhooks/endpoints/endpoint_id"])

    def test_list_deliveries(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"data":[{"attempt_count":-123456789,"created_at":"2024-03-15T10:30:45.123+02:00","endpoint_id":"webhook_endpoint_id_90","event_type":"sample","id":"webhook_delivery_id_0","manual":false,"message_id":"event_id_67","status":"SUCCEEDED"}],"pagination_meta":{"page":-123456789,"per_page":-123456789,"total_items":-9007199254740993,"total_pages":123456789}}',
        )
        call(client.webhook_endpoints.endpoints.list_deliveries, "endpoint_id")
        self.assertEqual(
            requests, ["GET /api/v1/webhooks/endpoints/endpoint_id/deliveries"]
        )

    def test_rotate_secret(self) -> None:
        client, requests = mock(200, "application/json", '{"secret":"sample"}')
        call(client.webhook_endpoints.endpoints.rotate_secret, "endpoint_id")
        self.assertEqual(
            requests, ["POST /api/v1/webhooks/endpoints/endpoint_id/rotate-secret"]
        )

    def test_retrieve_secret(self) -> None:
        client, requests = mock(200, "application/json", '{"secret":"sample"}')
        call(client.webhook_endpoints.endpoints.retrieve_secret, "endpoint_id")
        self.assertEqual(
            requests, ["GET /api/v1/webhooks/endpoints/endpoint_id/secret"]
        )
