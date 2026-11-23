# this file is @generated
# ruff: noqa: I001  (where the package sorts depends on whether it is generated yet)
import unittest

from meteroid.models import InvoiceCustomPropertiesRequest

from perseid_mock import call, decode, mock


class InvoicesTest(unittest.TestCase):
    def test_list(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"data":[{"amount_due":-9007199254740993,"applied_credits":-9007199254740993,"coupons":[{"coupon_id":"sample","name":"sample","total":-9007199254740993}],"created_at":"2024-03-15T10:30:45.123+02:00","currency":"BHD","custom_properties":{"key":"value","count":3,"ratio":0.5,"flags":[true,false],"nested":{"ok":true}},"customer_details":{"id":"customer_id_9","name":"sample","snapshot_at":"2024-03-15T10:30:45.123+02:00"},"customer_id":"customer_id_39","id":"invoice_id_21","invoice_date":"2024-02-29","invoice_number":"sample","invoice_type":"USAGE_THRESHOLD","line_items":[{"amount_total":-9007199254740993,"end_date":"2024-02-29","name":"sample","start_date":"2024-02-29","sub_line_items":[{"id":"sample","name":"sample","quantity":"12345.6789","total":9007199254740993,"unit_price":"-0.000123"}],"tax_rate":"-0.000123"}],"net_terms":-2147483648,"payment_status":"PAID","settled_by_credit_notes":true,"status":"VOID","subtotal":-9007199254740993,"subtotal_recurring":-9007199254740993,"tax_amount":9007199254740993,"tax_breakdown":[{"name":"sample","tax_amount":9007199254740993,"tax_rate":"12345.6789","taxable_amount":-9007199254740993}],"tax_inclusive":false,"total":9007199254740993,"transactions":[{"amount":9007199254740993,"amount_refunded":9007199254740993,"amount_reversed":9007199254740993,"currency":"sample","id":"payment_transaction_id_93","payment_type":"PAYMENT","status":"CANCELLED"}]}],"pagination_meta":{"page":-123456789,"per_page":-123456789,"total_items":-9007199254740993,"total_pages":123456789}}',
        )
        call(client.invoices.list)
        self.assertEqual(requests, ["GET /api/v1/invoices"])

    def test_retrieve(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"amount_due":-9007199254740993,"applied_credits":9007199254740993,"coupons":[{"coupon_id":"sample","name":"sample","total":9007199254740993}],"created_at":"2023-12-31T23:59:59.999-05:30","currency":"NAD","custom_properties":{"key":"value","count":3,"ratio":0.5,"flags":[true,false],"nested":{"ok":true}},"customer_details":{"id":"customer_id_85","name":"sample","snapshot_at":"2024-03-15T10:30:45.123+02:00"},"customer_id":"customer_id_1","id":"invoice_id_17","invoice_date":"1999-12-31","invoice_number":"sample","invoice_type":"ADJUSTMENT","line_items":[{"amount_total":-9007199254740993,"end_date":"2024-02-29","name":"sample","start_date":"2024-02-29","sub_line_items":[{"id":"sample","name":"sample","quantity":"-0.000123","total":-9007199254740993,"unit_price":"12345.6789"}],"tax_rate":"-0.000123"}],"net_terms":-123456789,"payment_status":"CARRIED","settled_by_credit_notes":true,"status":"FINALIZED","subtotal":9007199254740993,"subtotal_recurring":-9007199254740993,"tax_amount":-9007199254740993,"tax_breakdown":[{"name":"sample","tax_amount":-9007199254740993,"tax_rate":"12345.6789","taxable_amount":-9007199254740993}],"tax_inclusive":false,"total":-9007199254740993,"transactions":[{"amount":9007199254740993,"amount_refunded":-9007199254740993,"amount_reversed":9007199254740993,"currency":"sample","id":"payment_transaction_id_91","payment_type":"PAYMENT","status":"FAILED"}]}',
        )
        call(client.invoices.retrieve, "invoice_id")
        self.assertEqual(requests, ["GET /api/v1/invoices/invoice_id"])

    def test_update_custom_properties(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"amount_due":-9007199254740993,"applied_credits":9007199254740993,"coupons":[{"coupon_id":"sample","name":"sample","total":9007199254740993}],"created_at":"2023-12-31T23:59:59.999-05:30","currency":"NAD","custom_properties":{"key":"value","count":3,"ratio":0.5,"flags":[true,false],"nested":{"ok":true}},"customer_details":{"id":"customer_id_85","name":"sample","snapshot_at":"2024-03-15T10:30:45.123+02:00"},"customer_id":"customer_id_1","id":"invoice_id_17","invoice_date":"1999-12-31","invoice_number":"sample","invoice_type":"ADJUSTMENT","line_items":[{"amount_total":-9007199254740993,"end_date":"2024-02-29","name":"sample","start_date":"2024-02-29","sub_line_items":[{"id":"sample","name":"sample","quantity":"-0.000123","total":-9007199254740993,"unit_price":"12345.6789"}],"tax_rate":"-0.000123"}],"net_terms":-123456789,"payment_status":"CARRIED","settled_by_credit_notes":true,"status":"FINALIZED","subtotal":9007199254740993,"subtotal_recurring":-9007199254740993,"tax_amount":-9007199254740993,"tax_breakdown":[{"name":"sample","tax_amount":-9007199254740993,"tax_rate":"12345.6789","taxable_amount":-9007199254740993}],"tax_inclusive":false,"total":-9007199254740993,"transactions":[{"amount":9007199254740993,"amount_refunded":-9007199254740993,"amount_reversed":9007199254740993,"currency":"sample","id":"payment_transaction_id_91","payment_type":"PAYMENT","status":"FAILED"}]}',
        )
        call(
            client.invoices.update_custom_properties,
            "invoice_id",
            body=decode(
                InvoiceCustomPropertiesRequest,
                '{"custom_properties":{"key":"value","count":3,"ratio":0.5,"flags":[true,false],"nested":{"ok":true}}}',
            ),
        )
        self.assertEqual(
            requests, ["PATCH /api/v1/invoices/invoice_id/custom-properties"]
        )

    def test_download(self) -> None:
        client, requests = mock(200, "application/octet-stream", "sample")
        call(client.invoices.download, "invoice_id")
        self.assertEqual(requests, ["GET /api/v1/invoices/invoice_id/download"])

    def test_refresh(self) -> None:
        client, requests = mock(
            200,
            "application/json",
            '{"amount_due":-9007199254740993,"applied_credits":9007199254740993,"coupons":[{"coupon_id":"sample","name":"sample","total":9007199254740993}],"created_at":"2023-12-31T23:59:59.999-05:30","currency":"NAD","custom_properties":{"key":"value","count":3,"ratio":0.5,"flags":[true,false],"nested":{"ok":true}},"customer_details":{"id":"customer_id_85","name":"sample","snapshot_at":"2024-03-15T10:30:45.123+02:00"},"customer_id":"customer_id_1","id":"invoice_id_17","invoice_date":"1999-12-31","invoice_number":"sample","invoice_type":"ADJUSTMENT","line_items":[{"amount_total":-9007199254740993,"end_date":"2024-02-29","name":"sample","start_date":"2024-02-29","sub_line_items":[{"id":"sample","name":"sample","quantity":"-0.000123","total":-9007199254740993,"unit_price":"12345.6789"}],"tax_rate":"-0.000123"}],"net_terms":-123456789,"payment_status":"CARRIED","settled_by_credit_notes":true,"status":"FINALIZED","subtotal":9007199254740993,"subtotal_recurring":-9007199254740993,"tax_amount":-9007199254740993,"tax_breakdown":[{"name":"sample","tax_amount":-9007199254740993,"tax_rate":"12345.6789","taxable_amount":-9007199254740993}],"tax_inclusive":false,"total":-9007199254740993,"transactions":[{"amount":9007199254740993,"amount_refunded":-9007199254740993,"amount_reversed":9007199254740993,"currency":"sample","id":"payment_transaction_id_91","payment_type":"PAYMENT","status":"FAILED"}]}',
        )
        call(client.invoices.refresh, "invoice_id")
        self.assertEqual(requests, ["POST /api/v1/invoices/invoice_id/refresh"])

    def test_download_xml(self) -> None:
        client, requests = mock(200, "application/octet-stream", "sample")
        call(client.invoices.download_xml, "invoice_id")
        self.assertEqual(requests, ["GET /api/v1/invoices/invoice_id/xml"])
