# this file is @generated
# ruff: noqa: I001  (where the package sorts depends on whether it is generated yet)
import unittest

from perseid_mock import call, mock


class WebhookEndpointsTest(unittest.TestCase):
    def test_resend_webhook_delivery(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"attempt_count":-2147483648,"created_at":"2023-12-31T23:59:59.999-05:30","endpoint_id":"webhook_endpoint_id_44","event_type":"sample","id":"webhook_delivery_id_90","manual":false,"message_id":"event_id_90","status":"IN_FLIGHT"}',
        )
        call(client.webhook_endpoints.resend_webhook_delivery, "delivery_id")
        self.assertEqual(
            requests, ["POST /api/v1/webhooks/deliveries/delivery_id/resend"]
        )
