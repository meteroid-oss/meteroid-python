# this file is @generated
# ruff: noqa: I001  (where the package sorts depends on whether it is generated yet)
import unittest

from meteroid.models import CreateEntitlementsRequest

from perseid_mock import call, decode, mock


class AddOnsEntitlementsTest(unittest.TestCase):
    def test_list(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"data":[{"feature":{"code":"sample","id":"feature_id_53","name":"sample"},"value":{"type":"BOOLEAN","enabled":false}}]}',
        )
        call(client.add_ons.entitlements.list, "addon_id")
        self.assertEqual(requests, ["GET /api/v1/addons/addon_id/entitlements"])

    def test_create(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"data":[{"created_at":"2023-12-31T23:59:59.999-05:30","feature_id":"feature_id_39","id":"entitlement_id_2","updated_at":"2024-03-15T10:30:45.123+02:00","value":{"type":"BOOLEAN","enabled":false}}]}',
        )
        call(
            client.add_ons.entitlements.create,
            "addon_id",
            body=decode(
                CreateEntitlementsRequest,
                '{"entitlements":[{"feature_id":"feature_id_9","value":{"type":"BOOLEAN","enabled":false}}]}',
            ),
        )
        self.assertEqual(requests, ["POST /api/v1/addons/addon_id/entitlements"])
