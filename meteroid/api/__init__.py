# this file is @generated
"""Meteroid API resources."""

from __future__ import annotations

import importlib
import typing as t

from .._exceptions import (
    APIConnectionError,
    APIError,
    APIResponseValidationError,
    APITimeoutError,
)
from ..serialization import MeteroidError
from ._errors import (
    APIStatusError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    ErrorBody,
    InternalServerError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    UnprocessableEntityError,
)
from ._pagination import AsyncPage, AsyncPaginator, SyncPage
from ._response import APIResponse
from ._streaming import (
    AsyncEventStream,
    AsyncStream,
    EventStream,
    SseEvent,
    Stream,
    Upload,
)
from .client import AsyncMeteroid, Meteroid

if t.TYPE_CHECKING:
    from ._pages import (
        AddOnsListPage,
        AsyncAddOnsListPage,
        AsyncBatchJobsListFailuresPage,
        AsyncBatchJobsListPage,
        AsyncCouponsListPage,
        AsyncCreditNotesListPage,
        AsyncCustomersListPage,
        AsyncCustomPropertiesListCustomPropertyDefinitionsPage,
        AsyncFeaturesListPage,
        AsyncInvoicesListPage,
        AsyncMetricsListPage,
        AsyncPlansListPage,
        AsyncPlansListVersionsPage,
        AsyncProductFamiliesListPage,
        AsyncProductsListPage,
        AsyncSubscriptionsListPage,
        BatchJobsListFailuresPage,
        BatchJobsListPage,
        CouponsListPage,
        CreditNotesListPage,
        CustomersListPage,
        CustomPropertiesListCustomPropertyDefinitionsPage,
        FeaturesListPage,
        InvoicesListPage,
        MetricsListPage,
        PlansListPage,
        PlansListVersionsPage,
        ProductFamiliesListPage,
        ProductsListPage,
        SubscriptionsListPage,
    )
    from .add_ons import AddOns, AsyncAddOns
    from .batch_jobs import AsyncBatchJobs, BatchJobs
    from .checkout_sessions import AsyncCheckoutSessions, CheckoutSessions
    from .connect import AsyncConnect, Connect
    from .coupons import AsyncCoupons, Coupons
    from .credit_notes import AsyncCreditNotes, CreditNotes
    from .custom_properties import AsyncCustomProperties, CustomProperties
    from .customers import AsyncCustomers, Customers
    from .entitlements import AsyncEntitlements, Entitlements
    from .events import AsyncEvents, Events
    from .features import AsyncFeatures, Features
    from .invoices import AsyncInvoices, Invoices
    from .metrics import AsyncMetrics, Metrics
    from .oauth import AsyncOauth, Oauth
    from .oauth_apps import AsyncOauthApps, OauthApps
    from .plans import AsyncPlans, Plans
    from .product_families import AsyncProductFamilies, ProductFamilies
    from .products import AsyncProducts, Products
    from .subscriptions import AsyncSubscriptions, Subscriptions
    from .usage import AsyncUsage, Usage

# Each resource's module is imported the first time it is used.
_MODULES: dict[str, str] = {
    "AsyncAddOns": "add_ons",
    "AddOns": "add_ons",
    "AsyncBatchJobs": "batch_jobs",
    "BatchJobs": "batch_jobs",
    "AsyncCheckoutSessions": "checkout_sessions",
    "CheckoutSessions": "checkout_sessions",
    "AsyncConnect": "connect",
    "Connect": "connect",
    "AsyncCoupons": "coupons",
    "Coupons": "coupons",
    "AsyncCreditNotes": "credit_notes",
    "CreditNotes": "credit_notes",
    "AsyncCustomProperties": "custom_properties",
    "CustomProperties": "custom_properties",
    "AsyncCustomers": "customers",
    "Customers": "customers",
    "AsyncEntitlements": "entitlements",
    "Entitlements": "entitlements",
    "AsyncEvents": "events",
    "Events": "events",
    "AsyncFeatures": "features",
    "Features": "features",
    "AsyncInvoices": "invoices",
    "Invoices": "invoices",
    "AsyncMetrics": "metrics",
    "Metrics": "metrics",
    "AsyncOauth": "oauth",
    "Oauth": "oauth",
    "AsyncOauthApps": "oauth_apps",
    "OauthApps": "oauth_apps",
    "AsyncPlans": "plans",
    "Plans": "plans",
    "AsyncProductFamilies": "product_families",
    "ProductFamilies": "product_families",
    "AsyncProducts": "products",
    "Products": "products",
    "AsyncSubscriptions": "subscriptions",
    "Subscriptions": "subscriptions",
    "AsyncUsage": "usage",
    "Usage": "usage",
    "AsyncAddOnsListPage": "_pages",
    "AddOnsListPage": "_pages",
    "AsyncBatchJobsListPage": "_pages",
    "BatchJobsListPage": "_pages",
    "AsyncBatchJobsListFailuresPage": "_pages",
    "BatchJobsListFailuresPage": "_pages",
    "AsyncCouponsListPage": "_pages",
    "CouponsListPage": "_pages",
    "AsyncCreditNotesListPage": "_pages",
    "CreditNotesListPage": "_pages",
    "AsyncCustomPropertiesListCustomPropertyDefinitionsPage": "_pages",
    "CustomPropertiesListCustomPropertyDefinitionsPage": "_pages",
    "AsyncCustomersListPage": "_pages",
    "CustomersListPage": "_pages",
    "AsyncFeaturesListPage": "_pages",
    "FeaturesListPage": "_pages",
    "AsyncInvoicesListPage": "_pages",
    "InvoicesListPage": "_pages",
    "AsyncMetricsListPage": "_pages",
    "MetricsListPage": "_pages",
    "AsyncPlansListPage": "_pages",
    "PlansListPage": "_pages",
    "AsyncPlansListVersionsPage": "_pages",
    "PlansListVersionsPage": "_pages",
    "AsyncProductFamiliesListPage": "_pages",
    "ProductFamiliesListPage": "_pages",
    "AsyncProductsListPage": "_pages",
    "ProductsListPage": "_pages",
    "AsyncSubscriptionsListPage": "_pages",
    "SubscriptionsListPage": "_pages",
}


def __getattr__(name: str) -> t.Any:
    module = _MODULES.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    value = getattr(importlib.import_module(f".{module}", __name__), name)
    globals()[name] = value
    return value


def __dir__() -> list[str]:
    return sorted({*globals(), *_MODULES})


__all__ = [
    "APIConnectionError",
    "APIError",
    "APIResponse",
    "APIResponseValidationError",
    "APITimeoutError",
    "AsyncMeteroid",
    "AsyncEventStream",
    "AsyncPage",
    "AsyncPaginator",
    "AsyncStream",
    "EventStream",
    "Meteroid",
    "MeteroidError",
    "SseEvent",
    "Stream",
    "SyncPage",
    "Upload",
    "APIStatusError",
    "AuthenticationError",
    "BadRequestError",
    "ConflictError",
    "ErrorBody",
    "InternalServerError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitError",
    "UnprocessableEntityError",
    "AsyncAddOns",
    "AddOns",
    "AsyncBatchJobs",
    "BatchJobs",
    "AsyncCheckoutSessions",
    "CheckoutSessions",
    "AsyncConnect",
    "Connect",
    "AsyncCoupons",
    "Coupons",
    "AsyncCreditNotes",
    "CreditNotes",
    "AsyncCustomProperties",
    "CustomProperties",
    "AsyncCustomers",
    "Customers",
    "AsyncEntitlements",
    "Entitlements",
    "AsyncEvents",
    "Events",
    "AsyncFeatures",
    "Features",
    "AsyncInvoices",
    "Invoices",
    "AsyncMetrics",
    "Metrics",
    "AsyncOauth",
    "Oauth",
    "AsyncOauthApps",
    "OauthApps",
    "AsyncPlans",
    "Plans",
    "AsyncProductFamilies",
    "ProductFamilies",
    "AsyncProducts",
    "Products",
    "AsyncSubscriptions",
    "Subscriptions",
    "AsyncUsage",
    "Usage",
    "AsyncAddOnsListPage",
    "AddOnsListPage",
    "AsyncBatchJobsListPage",
    "BatchJobsListPage",
    "AsyncBatchJobsListFailuresPage",
    "BatchJobsListFailuresPage",
    "AsyncCouponsListPage",
    "CouponsListPage",
    "AsyncCreditNotesListPage",
    "CreditNotesListPage",
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
    "AsyncPlansListVersionsPage",
    "PlansListVersionsPage",
    "AsyncProductFamiliesListPage",
    "ProductFamiliesListPage",
    "AsyncProductsListPage",
    "ProductsListPage",
    "AsyncSubscriptionsListPage",
    "SubscriptionsListPage",
]
