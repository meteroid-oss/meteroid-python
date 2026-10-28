# this file is @generated
# ruff: noqa: I001  (where the package sorts depends on whether it is generated yet)
import unittest

from perseid_mock import call, mock


class ChecksTest(unittest.TestCase):
    def test_check_entitlement(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"as_of":"2023-12-31T23:59:59.999-05:30","exact":true,"feature":{"code":"sample","id":"feature_id_19"},"has_access":true,"in_overage":false,"lag_ms":9007199254740993,"limits":[{"behavior":"HARD","has_access":false,"limit":"-0.000123","remaining":"12345.6789","usage_limit_id":"usage_limit_id_23","used":"12345.6789"}],"near_limit":false,"reason":"INSUFFICIENT_BALANCE"}',
        )
        call(client.checks.check_entitlement, "id_or_alias", "feature_id_or_code")
        self.assertEqual(
            requests,
            ["GET /api/v1/customers/id_or_alias/entitlements/feature_id_or_code/check"],
        )
