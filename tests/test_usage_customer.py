# this file is @generated
# ruff: noqa: I001  (where the package sorts depends on whether it is generated yet)
import unittest

from perseid_mock import call, mock


class UsageCustomerTest(unittest.TestCase):
    def test_retrieve_unattributed(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"period_end":"1999-12-31","period_start":"2024-02-29","usage":[{"from":"2024-03-15T10:30:45.123+02:00","metric_code":"sample","metric_id":"billable_metric_id_44","metric_name":"sample","total_value":"12345.6789","until":"2023-12-31T23:59:59.999-05:30"}]}',
        )
        call(client.usage.customer.retrieve_unattributed, "customer_id")
        self.assertEqual(
            requests, ["GET /api/v1/usage/customer/customer_id/unattributed"]
        )
