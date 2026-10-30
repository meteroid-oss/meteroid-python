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
        AsyncBudgetsListPage,
        AsyncCouponsListPage,
        AsyncCreditNotesListPage,
        AsyncCreditsGrantsListPage,
        AsyncCreditsListCustomerCreditLedgerPage,
        AsyncCustomersListPage,
        AsyncCustomPropertiesListCustomPropertyDefinitionsPage,
        AsyncFeaturesListPage,
        AsyncInvoicesListPage,
        AsyncMetricsListPage,
        AsyncPlansListPage,
        AsyncPlansVersionsListPage,
        AsyncProductFamiliesListPage,
        AsyncProductsListPage,
        AsyncSubscriptionsListPage,
        AsyncWebhookEndpointsEndpointsListDeliveriesPage,
        BatchJobsListFailuresPage,
        BatchJobsListPage,
        BudgetsListPage,
        CouponsListPage,
        CreditNotesListPage,
        CreditsGrantsListPage,
        CreditsListCustomerCreditLedgerPage,
        CustomersListPage,
        CustomPropertiesListCustomPropertyDefinitionsPage,
        FeaturesListPage,
        InvoicesListPage,
        MetricsListPage,
        PlansListPage,
        PlansVersionsListPage,
        ProductFamiliesListPage,
        ProductsListPage,
        SubscriptionsListPage,
        WebhookEndpointsEndpointsListDeliveriesPage,
    )
    from .add_ons import AddOns, AsyncAddOns
    from .add_ons_entitlements import AddOnsEntitlements, AsyncAddOnsEntitlements
    from .batch_jobs import AsyncBatchJobs, BatchJobs
    from .budgets import AsyncBudgets, Budgets
    from .checkout_sessions import AsyncCheckoutSessions, CheckoutSessions
    from .checks import AsyncChecks, Checks
    from .connect import AsyncConnect, Connect
    from .coupons import AsyncCoupons, Coupons
    from .credit_notes import AsyncCreditNotes, CreditNotes
    from .credit_units import AsyncCreditUnits, CreditUnits
    from .credit_units_prices import AsyncCreditUnitsPrices, CreditUnitsPrices
    from .credits import AsyncCredits, Credits
    from .credits_grants import AsyncCreditsGrants, CreditsGrants
    from .credits_wallets import AsyncCreditsWallets, CreditsWallets
    from .custom_properties import AsyncCustomProperties, CustomProperties
    from .customers import AsyncCustomers, Customers
    from .entitlements import AsyncEntitlements, Entitlements
    from .events import AsyncEvents, Events
    from .features import AsyncFeatures, Features
    from .invoices import AsyncInvoices, Invoices
    from .licenses import AsyncLicenses, Licenses
    from .metrics import AsyncMetrics, Metrics
    from .oauth import AsyncOauth, Oauth
    from .oauth_apps import AsyncOauthApps, OauthApps
    from .plans import AsyncPlans, Plans
    from .plans_versions import AsyncPlansVersions, PlansVersions
    from .product_families import AsyncProductFamilies, ProductFamilies
    from .products import AsyncProducts, Products
    from .products_entitlements import AsyncProductsEntitlements, ProductsEntitlements
    from .subscriptions import AsyncSubscriptions, Subscriptions
    from .usage import AsyncUsage, Usage
    from .usage_costs import AsyncUsageCosts, UsageCosts
    from .usage_costs_customer import AsyncUsageCostsCustomer, UsageCostsCustomer
    from .usage_costs_subscription import (
        AsyncUsageCostsSubscription,
        UsageCostsSubscription,
    )
    from .usage_customer import AsyncUsageCustomer, UsageCustomer
    from .webhook_endpoints import AsyncWebhookEndpoints, WebhookEndpoints
    from .webhook_endpoints_endpoints import (
        AsyncWebhookEndpointsEndpoints,
        WebhookEndpointsEndpoints,
    )

# Each resource's module is imported the first time it is used.
_MODULES: dict[str, str] = {
    "AsyncAddOns": "add_ons",
    "AddOns": "add_ons",
    "AsyncAddOnsEntitlements": "add_ons_entitlements",
    "AddOnsEntitlements": "add_ons_entitlements",
    "AsyncBatchJobs": "batch_jobs",
    "BatchJobs": "batch_jobs",
    "AsyncBudgets": "budgets",
    "Budgets": "budgets",
    "AsyncCheckoutSessions": "checkout_sessions",
    "CheckoutSessions": "checkout_sessions",
    "AsyncChecks": "checks",
    "Checks": "checks",
    "AsyncConnect": "connect",
    "Connect": "connect",
    "AsyncCoupons": "coupons",
    "Coupons": "coupons",
    "AsyncCreditNotes": "credit_notes",
    "CreditNotes": "credit_notes",
    "AsyncCreditUnits": "credit_units",
    "CreditUnits": "credit_units",
    "AsyncCreditUnitsPrices": "credit_units_prices",
    "CreditUnitsPrices": "credit_units_prices",
    "AsyncCredits": "credits",
    "Credits": "credits",
    "AsyncCreditsGrants": "credits_grants",
    "CreditsGrants": "credits_grants",
    "AsyncCreditsWallets": "credits_wallets",
    "CreditsWallets": "credits_wallets",
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
    "AsyncLicenses": "licenses",
    "Licenses": "licenses",
    "AsyncMetrics": "metrics",
    "Metrics": "metrics",
    "AsyncOauth": "oauth",
    "Oauth": "oauth",
    "AsyncOauthApps": "oauth_apps",
    "OauthApps": "oauth_apps",
    "AsyncPlans": "plans",
    "Plans": "plans",
    "AsyncPlansVersions": "plans_versions",
    "PlansVersions": "plans_versions",
    "AsyncProductFamilies": "product_families",
    "ProductFamilies": "product_families",
    "AsyncProducts": "products",
    "Products": "products",
    "AsyncProductsEntitlements": "products_entitlements",
    "ProductsEntitlements": "products_entitlements",
    "AsyncSubscriptions": "subscriptions",
    "Subscriptions": "subscriptions",
    "AsyncUsage": "usage",
    "Usage": "usage",
    "AsyncUsageCustomer": "usage_customer",
    "UsageCustomer": "usage_customer",
    "AsyncUsageCosts": "usage_costs",
    "UsageCosts": "usage_costs",
    "AsyncUsageCostsCustomer": "usage_costs_customer",
    "UsageCostsCustomer": "usage_costs_customer",
    "AsyncUsageCostsSubscription": "usage_costs_subscription",
    "UsageCostsSubscription": "usage_costs_subscription",
    "AsyncWebhookEndpoints": "webhook_endpoints",
    "WebhookEndpoints": "webhook_endpoints",
    "AsyncWebhookEndpointsEndpoints": "webhook_endpoints_endpoints",
    "WebhookEndpointsEndpoints": "webhook_endpoints_endpoints",
    "AsyncAddOnsListPage": "_pages",
    "AddOnsListPage": "_pages",
    "AsyncBatchJobsListPage": "_pages",
    "BatchJobsListPage": "_pages",
    "AsyncBatchJobsListFailuresPage": "_pages",
    "BatchJobsListFailuresPage": "_pages",
    "AsyncBudgetsListPage": "_pages",
    "BudgetsListPage": "_pages",
    "AsyncCouponsListPage": "_pages",
    "CouponsListPage": "_pages",
    "AsyncCreditNotesListPage": "_pages",
    "CreditNotesListPage": "_pages",
    "AsyncCreditsListCustomerCreditLedgerPage": "_pages",
    "CreditsListCustomerCreditLedgerPage": "_pages",
    "AsyncCreditsGrantsListPage": "_pages",
    "CreditsGrantsListPage": "_pages",
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
    "AsyncPlansVersionsListPage": "_pages",
    "PlansVersionsListPage": "_pages",
    "AsyncProductFamiliesListPage": "_pages",
    "ProductFamiliesListPage": "_pages",
    "AsyncProductsListPage": "_pages",
    "ProductsListPage": "_pages",
    "AsyncSubscriptionsListPage": "_pages",
    "SubscriptionsListPage": "_pages",
    "AsyncWebhookEndpointsEndpointsListDeliveriesPage": "_pages",
    "WebhookEndpointsEndpointsListDeliveriesPage": "_pages",
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
    "AsyncAddOnsEntitlements",
    "AddOnsEntitlements",
    "AsyncBatchJobs",
    "BatchJobs",
    "AsyncBudgets",
    "Budgets",
    "AsyncCheckoutSessions",
    "CheckoutSessions",
    "AsyncChecks",
    "Checks",
    "AsyncConnect",
    "Connect",
    "AsyncCoupons",
    "Coupons",
    "AsyncCreditNotes",
    "CreditNotes",
    "AsyncCreditUnits",
    "CreditUnits",
    "AsyncCreditUnitsPrices",
    "CreditUnitsPrices",
    "AsyncCredits",
    "Credits",
    "AsyncCreditsGrants",
    "CreditsGrants",
    "AsyncCreditsWallets",
    "CreditsWallets",
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
    "AsyncLicenses",
    "Licenses",
    "AsyncMetrics",
    "Metrics",
    "AsyncOauth",
    "Oauth",
    "AsyncOauthApps",
    "OauthApps",
    "AsyncPlans",
    "Plans",
    "AsyncPlansVersions",
    "PlansVersions",
    "AsyncProductFamilies",
    "ProductFamilies",
    "AsyncProducts",
    "Products",
    "AsyncProductsEntitlements",
    "ProductsEntitlements",
    "AsyncSubscriptions",
    "Subscriptions",
    "AsyncUsage",
    "Usage",
    "AsyncUsageCustomer",
    "UsageCustomer",
    "AsyncUsageCosts",
    "UsageCosts",
    "AsyncUsageCostsCustomer",
    "UsageCostsCustomer",
    "AsyncUsageCostsSubscription",
    "UsageCostsSubscription",
    "AsyncWebhookEndpoints",
    "WebhookEndpoints",
    "AsyncWebhookEndpointsEndpoints",
    "WebhookEndpointsEndpoints",
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
