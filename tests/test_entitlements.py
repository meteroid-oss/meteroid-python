# this file is @generated
# ruff: noqa: I001  (where the package sorts depends on whether it is generated yet)
import unittest

from meteroid.models import UpdateEntitlementRequest

from perseid_mock import call, decode, mock


class EntitlementsTest(unittest.TestCase):
    def test_retrieve(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"created_at":"2023-12-31T23:59:59.999-05:30","feature_id":"feature_id_0","id":"entitlement_id_79","updated_at":"2024-03-15T10:30:45.123+02:00","value":{"type":"BOOLEAN","enabled":true}}',
        )
        call(client.entitlements.retrieve, "entitlement_id")
        self.assertEqual(requests, ["GET /api/v1/entitlements/entitlement_id"])

    def test_delete(self) -> None:
        client, requests = mock(204, None, "")
        call(client.entitlements.delete, "entitlement_id")
        self.assertEqual(requests, ["DELETE /api/v1/entitlements/entitlement_id"])

    def test_update(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"created_at":"2023-12-31T23:59:59.999-05:30","feature_id":"feature_id_0","id":"entitlement_id_79","updated_at":"2024-03-15T10:30:45.123+02:00","value":{"type":"BOOLEAN","enabled":true}}',
        )
        call(
            client.entitlements.update,
            "entitlement_id",
            body=decode(UpdateEntitlementRequest, "{}"),
        )
        self.assertEqual(requests, ["PATCH /api/v1/entitlements/entitlement_id"])
