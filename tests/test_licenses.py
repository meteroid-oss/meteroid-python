# this file is @generated
# ruff: noqa: I001  (where the package sorts depends on whether it is generated yet)
import unittest

from meteroid.models import (
    IssueLicenseRequest,
    IssueOfflineLicenseRequest,
    RevokeLicenseRequest,
)

from perseid_mock import call, decode, mock


class LicensesTest(unittest.TestCase):
    def test_list(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"data":[{"auto_issued":false,"created_at":"2023-12-31T23:59:59.999-05:30","customer_id":"customer_id_2","customer_name":"sample","has_activation_code":false,"id":"license_id_0","offline":false,"revoked_immediately":false,"status":"REVOKED","validity_days":-123456789}]}',
        )
        call(client.licenses.list)
        self.assertEqual(requests, ["GET /api/v1/licenses"])

    def test_create(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"license":{"auto_issued":false,"created_at":"2023-12-31T23:59:59.999-05:30","customer_id":"customer_id_37","customer_name":"sample","has_activation_code":true,"id":"license_id_40","offline":true,"revoked_immediately":true,"status":"PENDING","validity_days":123456789}}',
        )
        call(
            client.licenses.create,
            body=decode(IssueLicenseRequest, '{"customer_id":"sample"}'),
        )
        self.assertEqual(requests, ["POST /api/v1/licenses"])

    def test_retrieve(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"auto_issued":false,"created_at":"2024-03-15T10:30:45.123+02:00","customer_id":"customer_id_79","customer_name":"sample","has_activation_code":false,"id":"license_id_90","offline":false,"revoked_immediately":true,"status":"PENDING","validity_days":-123456789}',
        )
        call(client.licenses.retrieve, "license_id")
        self.assertEqual(requests, ["GET /api/v1/licenses/license_id"])

    def test_retrieve_activation_code(self) -> None:
        client, requests = mock(200, "application/json", '{"activation_code":"sample"}')
        call(client.licenses.retrieve_activation_code, "license_id")
        self.assertEqual(requests, ["GET /api/v1/licenses/license_id/activation-code"])

    def test_offline(self) -> None:
        client, requests = mock(200, "application/json", '{"license":"sample"}')
        call(
            client.licenses.offline,
            "license_id",
            body=decode(IssueOfflineLicenseRequest, '{"valid_days":123456789}'),
        )
        self.assertEqual(requests, ["POST /api/v1/licenses/license_id/offline"])

    def test_revoke(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"auto_issued":false,"created_at":"2024-03-15T10:30:45.123+02:00","customer_id":"customer_id_79","customer_name":"sample","has_activation_code":false,"id":"license_id_90","offline":false,"revoked_immediately":true,"status":"PENDING","validity_days":-123456789}',
        )
        call(
            client.licenses.revoke,
            "license_id",
            body=decode(RevokeLicenseRequest, "{}"),
        )
        self.assertEqual(requests, ["POST /api/v1/licenses/license_id/revoke"])

    def test_list_licensing_signing_keys(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"endpoints":{"activate_url":"sample","events_url":"sample","jwks_url":"sample","refresh_url":"sample"},"keys":[{"created_at":"2023-12-31T23:59:59.999-05:30","kid":"sample","public_key_pem":"sample","status":"ACTIVE"}]}',
        )
        call(client.licenses.list_licensing_signing_keys)
        self.assertEqual(requests, ["GET /api/v1/licensing/signing-keys"])
