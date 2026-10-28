# this file is @generated
"""The pages of the list operations, each a subclass of the response model of its request."""

from __future__ import annotations

from ..models import (
    AddOn,
    AddOnListResponse,
    BatchJobFailuresResponse,
    BatchJobItemFailureResponse,
    BatchJobListResponse,
    BatchJobResponse,
    Budget,
    BudgetListResponse,
    Coupon,
    CouponListResponse,
    CreditGrant,
    CreditGrantListResponse,
    CreditNote,
    CreditNoteListResponse,
    Customer,
    CustomerListResponse,
    CustomPropertyDefinition,
    CustomPropertyDefinitionListResponse,
    Feature,
    FeatureListResponse,
    Invoice,
    InvoiceListResponse,
    LedgerEntry,
    LedgerListResponse,
    MetricListResponse,
    MetricSummary,
    Plan,
    PlanListResponse,
    PlanVersionListResponse,
    PlanVersionSummary,
    Product,
    ProductFamily,
    ProductFamilyListResponse,
    ProductListResponse,
    Subscription,
    SubscriptionListResponse,
    WebhookDelivery,
    WebhookDeliveryListResponse,
)
from ._pagination import AsyncPage, SyncPage

__all__ = [
    "AsyncAddOnsListPage",
    "AddOnsListPage",
    "AsyncBatchJobsListPage",
    "BatchJobsListPage",
    "AsyncBatchJobsListFailuresPage",
    "BatchJobsListFailuresPage",
    "AsyncBudgetsListPage",
    "BudgetsListPage",
    "AsyncCouponsListPage",
    "CouponsListPage",
    "AsyncCreditNotesListPage",
    "CreditNotesListPage",
    "AsyncCreditsListCustomerCreditLedgerPage",
    "CreditsListCustomerCreditLedgerPage",
    "AsyncCreditsGrantsListPage",
    "CreditsGrantsListPage",
    "AsyncCustomPropertiesListCustomPropertyDefinitionsPage",
    "CustomPropertiesListCustomPropertyDefinitionsPage",
    "AsyncCustomersListPage",
    "CustomersListPage",
    "AsyncFeaturesListPage",
    "FeaturesListPage",
    "AsyncInvoicesListPage",
    "InvoicesListPage",
    "AsyncMetricsListPage",
    "MetricsListPage",
    "AsyncPlansListPage",
    "PlansListPage",
    "AsyncPlansVersionsListPage",
    "PlansVersionsListPage",
    "AsyncProductFamiliesListPage",
    "ProductFamiliesListPage",
    "AsyncProductsListPage",
    "ProductsListPage",
    "AsyncSubscriptionsListPage",
    "SubscriptionsListPage",
    "AsyncWebhookEndpointsEndpointsListDeliveriesPage",
    "WebhookEndpointsEndpointsListDeliveriesPage",
]


class AddOnsListPage(SyncPage[AddOn, AddOnListResponse], AddOnListResponse):
    """A page of :class:`AddOn`, and the :class:`AddOnListResponse` response of its request."""


class AsyncAddOnsListPage(AsyncPage[AddOn, AddOnListResponse], AddOnListResponse):
    """A page of :class:`AddOn`, and the :class:`AddOnListResponse` response of its request."""


class BatchJobsListPage(
    SyncPage[BatchJobResponse, BatchJobListResponse], BatchJobListResponse
):
    """A page of :class:`BatchJobResponse`, and the :class:`BatchJobListResponse` response of its request."""


class AsyncBatchJobsListPage(
    AsyncPage[BatchJobResponse, BatchJobListResponse], BatchJobListResponse
):
    """A page of :class:`BatchJobResponse`, and the :class:`BatchJobListResponse` response of its request."""


class BatchJobsListFailuresPage(
    SyncPage[BatchJobItemFailureResponse, BatchJobFailuresResponse],
    BatchJobFailuresResponse,
):
    """A page of :class:`BatchJobItemFailureResponse`, and the :class:`BatchJobFailuresResponse` response of its request."""


class AsyncBatchJobsListFailuresPage(
    AsyncPage[BatchJobItemFailureResponse, BatchJobFailuresResponse],
    BatchJobFailuresResponse,
):
    """A page of :class:`BatchJobItemFailureResponse`, and the :class:`BatchJobFailuresResponse` response of its request."""


class BudgetsListPage(SyncPage[Budget, BudgetListResponse], BudgetListResponse):
    """A page of :class:`Budget`, and the :class:`BudgetListResponse` response of its request."""


class AsyncBudgetsListPage(AsyncPage[Budget, BudgetListResponse], BudgetListResponse):
    """A page of :class:`Budget`, and the :class:`BudgetListResponse` response of its request."""


class CouponsListPage(SyncPage[Coupon, CouponListResponse], CouponListResponse):
    """A page of :class:`Coupon`, and the :class:`CouponListResponse` response of its request."""


class AsyncCouponsListPage(AsyncPage[Coupon, CouponListResponse], CouponListResponse):
    """A page of :class:`Coupon`, and the :class:`CouponListResponse` response of its request."""


class CreditNotesListPage(
    SyncPage[CreditNote, CreditNoteListResponse], CreditNoteListResponse
):
    """A page of :class:`CreditNote`, and the :class:`CreditNoteListResponse` response of its request."""


class AsyncCreditNotesListPage(
    AsyncPage[CreditNote, CreditNoteListResponse], CreditNoteListResponse
):
    """A page of :class:`CreditNote`, and the :class:`CreditNoteListResponse` response of its request."""


class CreditsListCustomerCreditLedgerPage(
    SyncPage[LedgerEntry, LedgerListResponse], LedgerListResponse
):
    """A page of :class:`LedgerEntry`, and the :class:`LedgerListResponse` response of its request."""


class AsyncCreditsListCustomerCreditLedgerPage(
    AsyncPage[LedgerEntry, LedgerListResponse], LedgerListResponse
):
    """A page of :class:`LedgerEntry`, and the :class:`LedgerListResponse` response of its request."""


class CreditsGrantsListPage(
    SyncPage[CreditGrant, CreditGrantListResponse], CreditGrantListResponse
):
    """A page of :class:`CreditGrant`, and the :class:`CreditGrantListResponse` response of its request."""


class AsyncCreditsGrantsListPage(
    AsyncPage[CreditGrant, CreditGrantListResponse], CreditGrantListResponse
):
    """A page of :class:`CreditGrant`, and the :class:`CreditGrantListResponse` response of its request."""


class CustomPropertiesListCustomPropertyDefinitionsPage(
    SyncPage[CustomPropertyDefinition, CustomPropertyDefinitionListResponse],
    CustomPropertyDefinitionListResponse,
):
    """A page of :class:`CustomPropertyDefinition`, and the :class:`CustomPropertyDefinitionListResponse` response of its request."""


class AsyncCustomPropertiesListCustomPropertyDefinitionsPage(
    AsyncPage[CustomPropertyDefinition, CustomPropertyDefinitionListResponse],
    CustomPropertyDefinitionListResponse,
):
    """A page of :class:`CustomPropertyDefinition`, and the :class:`CustomPropertyDefinitionListResponse` response of its request."""


class CustomersListPage(SyncPage[Customer, CustomerListResponse], CustomerListResponse):
    """A page of :class:`Customer`, and the :class:`CustomerListResponse` response of its request."""


class AsyncCustomersListPage(
    AsyncPage[Customer, CustomerListResponse], CustomerListResponse
):
    """A page of :class:`Customer`, and the :class:`CustomerListResponse` response of its request."""


class FeaturesListPage(SyncPage[Feature, FeatureListResponse], FeatureListResponse):
    """A page of :class:`Feature`, and the :class:`FeatureListResponse` response of its request."""


class AsyncFeaturesListPage(
    AsyncPage[Feature, FeatureListResponse], FeatureListResponse
):
    """A page of :class:`Feature`, and the :class:`FeatureListResponse` response of its request."""


class InvoicesListPage(SyncPage[Invoice, InvoiceListResponse], InvoiceListResponse):
    """A page of :class:`Invoice`, and the :class:`InvoiceListResponse` response of its request."""


class AsyncInvoicesListPage(
    AsyncPage[Invoice, InvoiceListResponse], InvoiceListResponse
):
    """A page of :class:`Invoice`, and the :class:`InvoiceListResponse` response of its request."""


class MetricsListPage(SyncPage[MetricSummary, MetricListResponse], MetricListResponse):
    """A page of :class:`MetricSummary`, and the :class:`MetricListResponse` response of its request."""


class AsyncMetricsListPage(
    AsyncPage[MetricSummary, MetricListResponse], MetricListResponse
):
    """A page of :class:`MetricSummary`, and the :class:`MetricListResponse` response of its request."""


class PlansListPage(SyncPage[Plan, PlanListResponse], PlanListResponse):
    """A page of :class:`Plan`, and the :class:`PlanListResponse` response of its request."""


class AsyncPlansListPage(AsyncPage[Plan, PlanListResponse], PlanListResponse):
    """A page of :class:`Plan`, and the :class:`PlanListResponse` response of its request."""


class PlansVersionsListPage(
    SyncPage[PlanVersionSummary, PlanVersionListResponse], PlanVersionListResponse
):
    """A page of :class:`PlanVersionSummary`, and the :class:`PlanVersionListResponse` response of its request."""


class AsyncPlansVersionsListPage(
    AsyncPage[PlanVersionSummary, PlanVersionListResponse], PlanVersionListResponse
):
    """A page of :class:`PlanVersionSummary`, and the :class:`PlanVersionListResponse` response of its request."""


class ProductFamiliesListPage(
    SyncPage[ProductFamily, ProductFamilyListResponse], ProductFamilyListResponse
):
    """A page of :class:`ProductFamily`, and the :class:`ProductFamilyListResponse` response of its request."""


class AsyncProductFamiliesListPage(
    AsyncPage[ProductFamily, ProductFamilyListResponse], ProductFamilyListResponse
):
    """A page of :class:`ProductFamily`, and the :class:`ProductFamilyListResponse` response of its request."""


class ProductsListPage(SyncPage[Product, ProductListResponse], ProductListResponse):
    """A page of :class:`Product`, and the :class:`ProductListResponse` response of its request."""


class AsyncProductsListPage(
    AsyncPage[Product, ProductListResponse], ProductListResponse
):
    """A page of :class:`Product`, and the :class:`ProductListResponse` response of its request."""


class SubscriptionsListPage(
    SyncPage[Subscription, SubscriptionListResponse], SubscriptionListResponse
):
    """A page of :class:`Subscription`, and the :class:`SubscriptionListResponse` response of its request."""


class AsyncSubscriptionsListPage(
    AsyncPage[Subscription, SubscriptionListResponse], SubscriptionListResponse
):
    """A page of :class:`Subscription`, and the :class:`SubscriptionListResponse` response of its request."""


class WebhookEndpointsEndpointsListDeliveriesPage(
    SyncPage[WebhookDelivery, WebhookDeliveryListResponse], WebhookDeliveryListResponse
):
    """A page of :class:`WebhookDelivery`, and the :class:`WebhookDeliveryListResponse` response of its request."""


class AsyncWebhookEndpointsEndpointsListDeliveriesPage(
    AsyncPage[WebhookDelivery, WebhookDeliveryListResponse], WebhookDeliveryListResponse
):
    """A page of :class:`WebhookDelivery`, and the :class:`WebhookDeliveryListResponse` response of its request."""
