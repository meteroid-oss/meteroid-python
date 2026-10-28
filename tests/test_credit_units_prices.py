# this file is @generated
# ruff: noqa: I001  (where the package sorts depends on whether it is generated yet)
import unittest

from meteroid.models import CreditUnitPriceSetRequest

from perseid_mock import call, decode, mock


class CreditUnitsPricesTest(unittest.TestCase):
    def test_list(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"data":[{"created_at":"2023-12-31T23:59:59.999-05:30","currency":"sample","id":"sample","unit_price":"sample"}]}',
        )
        call(client.credit_units.prices.list, "id")
        self.assertEqual(requests, ["GET /api/v1/credit-units/id/prices"])

    def test_update(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"created_at":"2024-03-15T10:30:45.123+02:00","currency":"sample","id":"sample","unit_price":"sample"}',
        )
        call(
            client.credit_units.prices.update,
            "id",
            "currency",
            body=decode(CreditUnitPriceSetRequest, '{"unit_price":"sample"}'),
        )
        self.assertEqual(requests, ["PUT /api/v1/credit-units/id/prices/currency"])

    def test_archive(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"created_at":"2024-03-15T10:30:45.123+02:00","currency":"sample","id":"sample","unit_price":"sample"}',
        )
        call(client.credit_units.prices.archive, "id", "currency")
        self.assertEqual(requests, ["DELETE /api/v1/credit-units/id/prices/currency"])
