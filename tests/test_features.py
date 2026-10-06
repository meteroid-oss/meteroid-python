# this file is @generated
# ruff: noqa: I001  (where the package sorts depends on whether it is generated yet)
import unittest

from meteroid.models import CreateFeatureRequest, UpdateFeatureRequest

from perseid_mock import call, decode, mock


class FeaturesTest(unittest.TestCase):
    def test_list(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"data":[{"code":"sample","created_at":"2023-12-31T23:59:59.999-05:30","feature_type":{"type":"BOOLEAN"},"id":"feature_id_0","name":"sample","status":"DISABLED"}],"pagination_meta":{"page":-123456789,"per_page":-123456789,"total_items":-9007199254740993,"total_pages":123456789}}',
        )
        call(client.features.list)
        self.assertEqual(requests, ["GET /api/v1/features"])

    def test_create(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"code":"sample","created_at":"2024-03-15T10:30:45.123+02:00","feature_type":{"type":"BOOLEAN"},"id":"feature_id_90","name":"sample","status":"ARCHIVED"}',
        )
        call(
            client.features.create,
            body=decode(
                CreateFeatureRequest,
                '{"code":"sample","feature_type":{"type":"BOOLEAN"},"name":"sample"}',
            ),
        )
        self.assertEqual(requests, ["POST /api/v1/features"])

    def test_retrieve(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"code":"sample","created_at":"2024-03-15T10:30:45.123+02:00","feature_type":{"type":"BOOLEAN"},"id":"feature_id_90","name":"sample","status":"ARCHIVED"}',
        )
        call(client.features.retrieve, "id_or_code")
        self.assertEqual(requests, ["GET /api/v1/features/id_or_code"])

    def test_update(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"code":"sample","created_at":"2024-03-15T10:30:45.123+02:00","feature_type":{"type":"BOOLEAN"},"id":"feature_id_90","name":"sample","status":"ARCHIVED"}',
        )
        call(
            client.features.update,
            "id_or_code",
            body=decode(UpdateFeatureRequest, "{}"),
        )
        self.assertEqual(requests, ["PATCH /api/v1/features/id_or_code"])

    def test_archive(self) -> None:
        client, requests = mock(204, None, "")
        call(client.features.archive, "id_or_code")
        self.assertEqual(requests, ["POST /api/v1/features/id_or_code/archive"])

    def test_unarchive(self) -> None:
        client, requests = mock(204, None, "")
        call(client.features.unarchive, "id_or_code")
        self.assertEqual(requests, ["POST /api/v1/features/id_or_code/unarchive"])
