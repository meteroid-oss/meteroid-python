# this file is @generated
# ruff: noqa: I001  (where the package sorts depends on whether it is generated yet)
import unittest

from meteroid.models import CreditUnitCreateRequest, CreditUnitUpdateRequest

from perseid_mock import call, decode, mock


class CreditUnitsTest(unittest.TestCase):
    def test_list(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"data":[{"archived":false,"code":"sample","id":"sample","name":"sample","plural_name":"sample","precision":123456789,"prices":[{"created_at":"2023-12-31T23:59:59.999-05:30","currency":"sample","id":"sample","unit_price":"sample"}]}]}',
        )
        call(client.credit_units.list)
        self.assertEqual(requests, ["GET /api/v1/credit-units"])

    def test_create(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"archived":false,"code":"sample","id":"sample","name":"sample","plural_name":"sample","precision":2147483647,"prices":[{"created_at":"2024-03-15T10:30:45.123+02:00","currency":"sample","id":"sample","unit_price":"sample"}]}',
        )
        call(
            client.credit_units.create,
            body=decode(
                CreditUnitCreateRequest,
                '{"code":"sample","name":"sample","plural_name":"sample","precision":123456789}',
            ),
        )
        self.assertEqual(requests, ["POST /api/v1/credit-units"])

    def test_retrieve(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"archived":false,"code":"sample","id":"sample","name":"sample","plural_name":"sample","precision":2147483647,"prices":[{"created_at":"2024-03-15T10:30:45.123+02:00","currency":"sample","id":"sample","unit_price":"sample"}]}',
        )
        call(client.credit_units.retrieve, "id")
        self.assertEqual(requests, ["GET /api/v1/credit-units/id"])

    def test_update(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"archived":false,"code":"sample","id":"sample","name":"sample","plural_name":"sample","precision":2147483647,"prices":[{"created_at":"2024-03-15T10:30:45.123+02:00","currency":"sample","id":"sample","unit_price":"sample"}]}',
        )
        call(
            client.credit_units.update, "id", body=decode(CreditUnitUpdateRequest, "{}")
        )
        self.assertEqual(requests, ["PATCH /api/v1/credit-units/id"])
