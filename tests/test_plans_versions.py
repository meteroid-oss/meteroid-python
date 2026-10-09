# this file is @generated
# ruff: noqa: I001  (where the package sorts depends on whether it is generated yet)
import unittest

from meteroid.models import MinimumCommitment

from perseid_mock import call, decode, mock


class PlansVersionsTest(unittest.TestCase):
    def test_update_minimum(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"amount":"sample","scope":{"type":"all_components"}}',
        )
        call(
            client.plans.versions.update_minimum,
            "plan_version_id",
            body=decode(
                MinimumCommitment,
                '{"amount":"sample","scope":{"type":"all_components"}}',
            ),
        )
        self.assertEqual(
            requests, ["PUT /api/v1/plans/versions/plan_version_id/minimum"]
        )

    def test_delete_minimum(self) -> None:
        client, requests = mock(204, None, "")
        call(client.plans.versions.delete_minimum, "plan_version_id")
        self.assertEqual(
            requests, ["DELETE /api/v1/plans/versions/plan_version_id/minimum"]
        )

    def test_list(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"data":[{"created_at":"2023-12-31T23:59:59.999-05:30","currency":"CVE","id":"plan_version_id_2","is_draft":true,"version":-2147483648}],"pagination_meta":{"page":-123456789,"per_page":-123456789,"total_items":-9007199254740993,"total_pages":123456789}}',
        )
        call(client.plans.versions.list, "plan_id")
        self.assertEqual(requests, ["GET /api/v1/plans/plan_id/versions"])
