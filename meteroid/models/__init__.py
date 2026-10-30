# this file is @generated
"""Models for the Meteroid API.

Each model's module is imported the first time the model is used.
"""

from __future__ import annotations

import importlib
import typing as t

from ..serialization import UNSET, UnknownVariant, Unset

if t.TYPE_CHECKING:
    from .actor import Actor
    from .actor_type import ActorType, ActorTypeLiteral
    from .add_on import AddOn
    from .add_on_event import AddOnEvent
    from .add_on_event_data import AddOnEventData
    from .add_on_id import AddOnId
    from .add_on_list_response import AddOnListResponse
    from .address import Address
    from .all_components_scope import AllComponentsScope
    from .applied_coupon import AppliedCoupon
    from .applied_coupon_detailed import AppliedCouponDetailed
    from .applied_coupon_id import AppliedCouponId
    from .auto_top_up import AutoTopUp
    from .auto_top_up_cap_reached_event import AutoTopUpCapReachedEvent
    from .auto_top_up_cap_reached_event_data import AutoTopUpCapReachedEventData
    from .auto_top_up_consent_changed_event import AutoTopUpConsentChangedEvent
    from .auto_top_up_consent_changed_event_data import AutoTopUpConsentChangedEventData
    from .auto_top_up_event import AutoTopUpEvent
    from .auto_top_up_event_data import AutoTopUpEventData
    from .auto_top_up_method import AutoTopUpMethod, AutoTopUpMethodLiteral
    from .auto_top_up_status import AutoTopUpStatus, AutoTopUpStatusLiteral
    from .auto_top_up_write_request import AutoTopUpWriteRequest
    from .available_parameters import AvailableParameters
    from .bank_account_id import BankAccountId
    from .bank_transfer_payment_method_config import BankTransferPaymentMethodConfig
    from .batch_job_chunk_id import BatchJobChunkId
    from .batch_job_detail_response import BatchJobDetailResponse
    from .batch_job_failures_response import BatchJobFailuresResponse
    from .batch_job_id import BatchJobId
    from .batch_job_item_failure_response import BatchJobItemFailureResponse
    from .batch_job_list_response import BatchJobListResponse
    from .batch_job_response import BatchJobResponse
    from .batch_job_status import BatchJobStatus, BatchJobStatusLiteral
    from .batch_job_type import BatchJobType, BatchJobTypeLiteral
    from .billable_metric_id import BillableMetricId
    from .billing_config import BillingConfig
    from .billing_cycle_reset_period import BillingCycleResetPeriod
    from .billing_metric_aggregate_enum import (
        BillingMetricAggregateEnum,
        BillingMetricAggregateEnumLiteral,
    )
    from .billing_period_enum import BillingPeriodEnum, BillingPeriodEnumLiteral
    from .billing_type import BillingType, BillingTypeLiteral
    from .billing_type_enum import BillingTypeEnum, BillingTypeEnumLiteral
    from .boolean_config_value import BooleanConfigValue
    from .boolean_effective_entitlement_value import BooleanEffectiveEntitlementValue
    from .boolean_entitlement_value import BooleanEntitlementValue
    from .boolean_feature_type import BooleanFeatureType
    from .boolean_resolved_entitlement_value import BooleanResolvedEntitlementValue
    from .budget import Budget
    from .budget_author import BudgetAuthor, BudgetAuthorLiteral
    from .budget_behavior import BudgetBehavior, BudgetBehaviorLiteral
    from .budget_list_response import BudgetListResponse
    from .budget_period import BudgetPeriod
    from .calendar_reset_period import CalendarResetPeriod
    from .calendar_unit import CalendarUnit, CalendarUnitLiteral
    from .cancel_checkout_session_response import CancelCheckoutSessionResponse
    from .cancel_subscription_request import CancelSubscriptionRequest
    from .cancel_subscription_response import CancelSubscriptionResponse
    from .capacity_fee import CapacityFee
    from .capacity_fee_structure import CapacityFeeStructure
    from .capacity_plan_fee import CapacityPlanFee
    from .capacity_pricing import CapacityPricing
    from .capacity_threshold import CapacityThreshold
    from .checkout_session import CheckoutSession
    from .checkout_session_id import CheckoutSessionId
    from .checkout_session_status import (
        CheckoutSessionStatus,
        CheckoutSessionStatusLiteral,
    )
    from .checkout_type import CheckoutType, CheckoutTypeLiteral
    from .component_override import ComponentOverride
    from .component_parameterization import ComponentParameterization
    from .component_parameters import ComponentParameters
    from .components_scope import ComponentsScope
    from .config_effective_entitlement_value import ConfigEffectiveEntitlementValue
    from .config_entitlement_value import ConfigEntitlementValue
    from .config_feature_type import ConfigFeatureType
    from .config_resolved_entitlement_value import ConfigResolvedEntitlementValue
    from .config_value import ConfigValue
    from .config_value_type import ConfigValueType, ConfigValueTypeLiteral
    from .connected_account import ConnectedAccount
    from .connected_account_id import ConnectedAccountId
    from .connected_accounts_response import ConnectedAccountsResponse
    from .connection_status import ConnectionStatus, ConnectionStatusLiteral
    from .connection_type import ConnectionType, ConnectionTypeLiteral
    from .country_code import CountryCode
    from .coupon import Coupon
    from .coupon_credit_scope import CouponCreditScope, CouponCreditScopeLiteral
    from .coupon_discount import CouponDiscount
    from .coupon_event import CouponEvent
    from .coupon_event_data import CouponEventData
    from .coupon_filter import CouponFilter, CouponFilterLiteral
    from .coupon_id import CouponId
    from .coupon_line_item import CouponLineItem
    from .coupon_list_response import CouponListResponse
    from .create_add_on_request import CreateAddOnRequest
    from .create_budget_request import CreateBudgetRequest
    from .create_checkout_session_request import CreateCheckoutSessionRequest
    from .create_checkout_session_response import CreateCheckoutSessionResponse
    from .create_connected_account_request import CreateConnectedAccountRequest
    from .create_connected_account_response import CreateConnectedAccountResponse
    from .create_coupon_request import CreateCouponRequest
    from .create_credit_grant_request import CreateCreditGrantRequest
    from .create_entitlements_request import CreateEntitlementsRequest
    from .create_feature_request import CreateFeatureRequest
    from .create_metric_request import CreateMetricRequest
    from .create_o_auth_app_request import CreateOAuthAppRequest
    from .create_onboarding_link_request import CreateOnboardingLinkRequest
    from .create_plan_request import CreatePlanRequest
    from .create_product_request import CreateProductRequest
    from .create_subscription_add_on import CreateSubscriptionAddOn
    from .create_subscription_components import CreateSubscriptionComponents
    from .create_top_up_request import CreateTopUpRequest
    from .create_webhook_endpoint_request import CreateWebhookEndpointRequest
    from .created_webhook_endpoint import CreatedWebhookEndpoint
    from .credit_applies_to import CreditAppliesTo, CreditAppliesToLiteral
    from .credit_cap import CreditCap
    from .credit_caps import CreditCaps
    from .credit_cost import CreditCost
    from .credit_cost_request import CreditCostRequest
    from .credit_discount import CreditDiscount
    from .credit_exhausted_rule import CreditExhaustedRule
    from .credit_exhausted_rule_invoice_variant import CreditExhaustedRuleInvoiceVariant
    from .credit_exhausted_rule_pause_variant import CreditExhaustedRulePauseVariant
    from .credit_expiry_unit import CreditExpiryUnit, CreditExpiryUnitLiteral
    from .credit_fee import CreditFee
    from .credit_fee_structure import CreditFeeStructure
    from .credit_grant import CreditGrant
    from .credit_grant_expired_event import CreditGrantExpiredEvent
    from .credit_grant_expired_event_data import CreditGrantExpiredEventData
    from .credit_grant_id import CreditGrantId
    from .credit_grant_kind import CreditGrantKind, CreditGrantKindLiteral
    from .credit_grant_lapse_reason import (
        CreditGrantLapseReason,
        CreditGrantLapseReasonLiteral,
    )
    from .credit_grant_list_response import CreditGrantListResponse
    from .credit_grant_source import CreditGrantSource, CreditGrantSourceLiteral
    from .credit_grant_status import CreditGrantStatus, CreditGrantStatusLiteral
    from .credit_grant_type import CreditGrantType, CreditGrantTypeLiteral
    from .credit_note import CreditNote
    from .credit_note_custom_properties_request import CreditNoteCustomPropertiesRequest
    from .credit_note_event import CreditNoteEvent
    from .credit_note_event_data import CreditNoteEventData
    from .credit_note_id import CreditNoteId
    from .credit_note_list_response import CreditNoteListResponse
    from .credit_note_status import CreditNoteStatus, CreditNoteStatusLiteral
    from .credit_pack_expiry import CreditPackExpiry
    from .credit_pack_rollover import CreditPackRollover
    from .credit_pack_unit import CreditPackUnit
    from .credit_plan_fee import CreditPlanFee
    from .credit_type import CreditType, CreditTypeLiteral
    from .credit_unit import CreditUnit
    from .credit_unit_create_request import CreditUnitCreateRequest
    from .credit_unit_list_response import CreditUnitListResponse
    from .credit_unit_price import CreditUnitPrice
    from .credit_unit_price_list_response import CreditUnitPriceListResponse
    from .credit_unit_price_set_request import CreditUnitPriceSetRequest
    from .credit_unit_update_request import CreditUnitUpdateRequest
    from .currency import Currency, CurrencyLiteral
    from .custom_property_definition import CustomPropertyDefinition
    from .custom_property_definition_create_request import (
        CustomPropertyDefinitionCreateRequest,
    )
    from .custom_property_definition_id import CustomPropertyDefinitionId
    from .custom_property_definition_list_response import (
        CustomPropertyDefinitionListResponse,
    )
    from .custom_property_definition_update_request import (
        CustomPropertyDefinitionUpdateRequest,
    )
    from .custom_property_entity_type import (
        CustomPropertyEntityType,
        CustomPropertyEntityTypeLiteral,
    )
    from .custom_property_type import CustomPropertyType, CustomPropertyTypeLiteral
    from .custom_tax_rate import CustomTaxRate
    from .customer import Customer
    from .customer_create_request import CustomerCreateRequest
    from .customer_details import CustomerDetails
    from .customer_event import CustomerEvent
    from .customer_event_data import CustomerEventData
    from .customer_id import CustomerId
    from .customer_list_response import CustomerListResponse
    from .customer_patch_request import CustomerPatchRequest
    from .customer_payment_method_id import CustomerPaymentMethodId
    from .customer_portal_scope import CustomerPortalScope, CustomerPortalScopeLiteral
    from .customer_portal_token_request import CustomerPortalTokenRequest
    from .customer_portal_token_response import CustomerPortalTokenResponse
    from .customer_type import CustomerType, CustomerTypeLiteral
    from .customer_update_request import CustomerUpdateRequest
    from .decline_kind import DeclineKind, DeclineKindLiteral
    from .double_segmentation_matrix import DoubleSegmentationMatrix
    from .e_invoicing_finding import EInvoicingFinding
    from .e_invoicing_status import EInvoicingStatus, EInvoicingStatusLiteral
    from .effective_entitlement import EffectiveEntitlement
    from .effective_entitlement_list_response import EffectiveEntitlementListResponse
    from .effective_entitlement_value import EffectiveEntitlementValue
    from .entitlement import Entitlement
    from .entitlement_check import EntitlementCheck
    from .entitlement_check_feature import EntitlementCheckFeature
    from .entitlement_check_limit import EntitlementCheckLimit
    from .entitlement_check_limit_behavior import (
        EntitlementCheckLimitBehavior,
        EntitlementCheckLimitBehaviorLiteral,
    )
    from .entitlement_check_period import EntitlementCheckPeriod
    from .entitlement_check_reason import (
        EntitlementCheckReason,
        EntitlementCheckReasonLiteral,
    )
    from .entitlement_id import EntitlementId
    from .entitlement_list_response import EntitlementListResponse
    from .entitlement_overage_behavior import (
        EntitlementOverageBehavior,
        EntitlementOverageBehaviorLiteral,
    )
    from .entitlement_product_ref import EntitlementProductRef
    from .entitlement_spec_request import EntitlementSpecRequest
    from .entitlement_value import EntitlementValue
    from .error_code import ErrorCode, ErrorCodeLiteral
    from .event import Event
    from .event_id import EventId
    from .event_type import EventType, EventTypeLiteral
    from .existing_price_ref import ExistingPriceRef
    from .existing_product_ref import ExistingProductRef
    from .external_payment_method_config import ExternalPaymentMethodConfig
    from .extra_component import ExtraComponent
    from .extra_recurring_billing_type_enum import (
        ExtraRecurringBillingTypeEnum,
        ExtraRecurringBillingTypeEnumLiteral,
    )
    from .extra_recurring_fee_structure import ExtraRecurringFeeStructure
    from .extra_recurring_plan_fee import ExtraRecurringPlanFee
    from .extra_recurring_pricing import ExtraRecurringPricing
    from .feature import Feature
    from .feature_id import FeatureId
    from .feature_list_response import FeatureListResponse
    from .feature_ref import FeatureRef
    from .feature_status import FeatureStatus, FeatureStatusLiteral
    from .feature_type import FeatureType
    from .fee import Fee
    from .fee_credit_unit import FeeCreditUnit
    from .fixed_discount import FixedDiscount
    from .fixed_window_reset_period import FixedWindowResetPeriod
    from .get_checkout_session_response import GetCheckoutSessionResponse
    from .grouped_usage import GroupedUsage
    from .ingest_events_request import IngestEventsRequest
    from .ingest_events_response import IngestEventsResponse
    from .ingest_failure import IngestFailure
    from .introspection_request import IntrospectionRequest
    from .invoice import Invoice
    from .invoice_custom_properties_request import InvoiceCustomPropertiesRequest
    from .invoice_documents_event import InvoiceDocumentsEvent
    from .invoice_documents_event_data import InvoiceDocumentsEventData
    from .invoice_event import InvoiceEvent
    from .invoice_event_data import InvoiceEventData
    from .invoice_id import InvoiceId
    from .invoice_line_credit_unit import InvoiceLineCreditUnit
    from .invoice_line_item import InvoiceLineItem
    from .invoice_list_response import InvoiceListResponse
    from .invoice_payment_status import (
        InvoicePaymentStatus,
        InvoicePaymentStatusLiteral,
    )
    from .invoice_status import InvoiceStatus, InvoiceStatusLiteral
    from .invoice_type import InvoiceType, InvoiceTypeLiteral
    from .invoicing_entity_id import InvoicingEntityId
    from .issue_license_request import IssueLicenseRequest
    from .issue_license_response import IssueLicenseResponse
    from .issue_offline_license_request import IssueOfflineLicenseRequest
    from .json_config_value import JsonConfigValue
    from .ledger_entry import LedgerEntry
    from .ledger_entry_id import LedgerEntryId
    from .ledger_entry_type import LedgerEntryType, LedgerEntryTypeLiteral
    from .ledger_list_response import LedgerListResponse
    from .license import License
    from .license_activation_code import LicenseActivationCode
    from .license_id import LicenseId
    from .license_list_response import LicenseListResponse
    from .license_signing_key import LicenseSigningKey
    from .license_signing_key_status import (
        LicenseSigningKeyStatus,
        LicenseSigningKeyStatusLiteral,
    )
    from .license_signing_keys_response import LicenseSigningKeysResponse
    from .license_status import LicenseStatus, LicenseStatusLiteral
    from .licensing_endpoints import LicensingEndpoints
    from .linked_segmentation_matrix import LinkedSegmentationMatrix
    from .list_checkout_sessions_response import ListCheckoutSessionsResponse
    from .list_customer_usage_costs_granularity import (
        ListCustomerUsageCostsGranularity,
        ListCustomerUsageCostsGranularityLiteral,
    )
    from .list_subscription_usage_costs_granularity import (
        ListSubscriptionUsageCostsGranularity,
        ListSubscriptionUsageCostsGranularityLiteral,
    )
    from .matrix_dimension import MatrixDimension
    from .matrix_plan_pricing import MatrixPlanPricing
    from .matrix_pricing import MatrixPricing
    from .matrix_row import MatrixRow
    from .metered_effective_entitlement_value import MeteredEffectiveEntitlementValue
    from .metered_entitlement_spec import MeteredEntitlementSpec
    from .metered_entitlement_usage import MeteredEntitlementUsage
    from .metered_entitlement_value import MeteredEntitlementValue
    from .metered_feature_type import MeteredFeatureType
    from .metered_resolved_entitlement_value import MeteredResolvedEntitlementValue
    from .metric import Metric
    from .metric_dimension import MetricDimension
    from .metric_event import MetricEvent
    from .metric_event_data import MetricEventData
    from .metric_filter import MetricFilter
    from .metric_filter_operator import (
        MetricFilterOperator,
        MetricFilterOperatorLiteral,
    )
    from .metric_list_response import MetricListResponse
    from .metric_segmentation_matrix import MetricSegmentationMatrix
    from .metric_summary import MetricSummary
    from .metric_usage import MetricUsage
    from .minimum_commitment import MinimumCommitment
    from .minimum_commitment_input import MinimumCommitmentInput
    from .minimum_commitment_input_scope import MinimumCommitmentInputScope
    from .minimum_commitment_scope import MinimumCommitmentScope
    from .never_reset_period import NeverResetPeriod
    from .new_product_ref import NewProductRef
    from .number_config_value import NumberConfigValue
    from .o_auth_app import OAuthApp
    from .o_auth_app_id import OAuthAppId
    from .o_auth_app_with_secret import OAuthAppWithSecret
    from .o_auth_apps_response import OAuthAppsResponse
    from .o_auth_error_code import OAuthErrorCode, OAuthErrorCodeLiteral
    from .o_auth_error_response import OAuthErrorResponse
    from .offline_license import OfflineLicense
    from .onboarding_link_response import OnboardingLinkResponse
    from .onboarding_mode import OnboardingMode, OnboardingModeLiteral
    from .one_time_fee import OneTimeFee
    from .one_time_fee_structure import OneTimeFeeStructure
    from .one_time_plan_fee import OneTimePlanFee
    from .one_time_pricing import OneTimePricing
    from .online_method_config import OnlineMethodConfig
    from .online_methods_config import OnlineMethodsConfig
    from .online_payment_method_config import OnlinePaymentMethodConfig
    from .organization_id import OrganizationId
    from .package_plan_pricing import PackagePlanPricing
    from .package_pricing import PackagePricing
    from .pagination_response import PaginationResponse
    from .patch_budget_request import PatchBudgetRequest
    from .patch_plan_request import PatchPlanRequest
    from .patch_wallet_request import PatchWalletRequest
    from .payment_event import PaymentEvent
    from .payment_method_info import PaymentMethodInfo
    from .payment_method_type_enum import (
        PaymentMethodTypeEnum,
        PaymentMethodTypeEnumLiteral,
    )
    from .payment_methods_config import PaymentMethodsConfig
    from .payment_status_enum import PaymentStatusEnum, PaymentStatusEnumLiteral
    from .payment_transaction_id import PaymentTransactionId
    from .payment_type_enum import PaymentTypeEnum, PaymentTypeEnumLiteral
    from .per_unit_plan_pricing import PerUnitPlanPricing
    from .per_unit_pricing import PerUnitPricing
    from .percentage_discount import PercentageDiscount
    from .plan import Plan
    from .plan_add_on_input import PlanAddOnInput
    from .plan_event import PlanEvent
    from .plan_event_data import PlanEventData
    from .plan_fee_credit_unit import PlanFeeCreditUnit
    from .plan_id import PlanId
    from .plan_list_response import PlanListResponse
    from .plan_status_enum import PlanStatusEnum, PlanStatusEnumLiteral
    from .plan_type_enum import PlanTypeEnum, PlanTypeEnumLiteral
    from .plan_usage_pricing_model import PlanUsagePricingModel
    from .plan_version_id import PlanVersionId
    from .plan_version_list_response import PlanVersionListResponse
    from .plan_version_summary import PlanVersionSummary
    from .price_component import PriceComponent
    from .price_component_id import PriceComponentId
    from .price_component_input import PriceComponentInput
    from .price_entry import PriceEntry
    from .price_id import PriceId
    from .price_input import PriceInput
    from .pricing import Pricing
    from .product import Product
    from .product_event import ProductEvent
    from .product_event_data import ProductEventData
    from .product_family import ProductFamily
    from .product_family_create_request import ProductFamilyCreateRequest
    from .product_family_id import ProductFamilyId
    from .product_family_list_response import ProductFamilyListResponse
    from .product_fee_structure import ProductFeeStructure
    from .product_fee_type_enum import ProductFeeTypeEnum, ProductFeeTypeEnumLiteral
    from .product_id import ProductId
    from .product_list_response import ProductListResponse
    from .product_ref import ProductRef
    from .products_scope import ProductsScope
    from .property_config import PropertyConfig
    from .quote_event import QuoteEvent
    from .quote_event_data import QuoteEventData
    from .quote_id import QuoteId
    from .rate_fee import RateFee
    from .rate_fee_structure import RateFeeStructure
    from .rate_plan_fee import RatePlanFee
    from .rate_pricing import RatePricing
    from .recurring_fee import RecurringFee
    from .refund_event_data import RefundEventData
    from .refund_mode import RefundMode, RefundModeLiteral
    from .replace_plan_request import ReplacePlanRequest
    from .reset_period import ResetPeriod
    from .resolved_entitlement import ResolvedEntitlement
    from .resolved_entitlement_list_response import ResolvedEntitlementListResponse
    from .resolved_entitlement_value import ResolvedEntitlementValue
    from .rest_error_response import RestErrorResponse
    from .reversal_kind import ReversalKind, ReversalKindLiteral
    from .revocation_request import RevocationRequest
    from .revoke_license_request import RevokeLicenseRequest
    from .rotated_secret import RotatedSecret
    from .select_option import SelectOption
    from .shipping_address import ShippingAddress
    from .sliding_window_reset_period import SlidingWindowResetPeriod
    from .slot_downgrade_policy_enum import (
        SlotDowngradePolicyEnum,
        SlotDowngradePolicyEnumLiteral,
    )
    from .slot_fee import SlotFee
    from .slot_fee_structure import SlotFeeStructure
    from .slot_plan_fee import SlotPlanFee
    from .slot_pricing import SlotPricing
    from .slot_upgrade_policy_enum import (
        SlotUpgradePolicyEnum,
        SlotUpgradePolicyEnumLiteral,
    )
    from .sub_line_item import SubLineItem
    from .subscription import Subscription
    from .subscription_activation_condition_enum import (
        SubscriptionActivationConditionEnum,
        SubscriptionActivationConditionEnumLiteral,
    )
    from .subscription_add_on import SubscriptionAddOn
    from .subscription_add_on_customization import SubscriptionAddOnCustomization
    from .subscription_add_on_id import SubscriptionAddOnId
    from .subscription_add_on_parameterization import SubscriptionAddOnParameterization
    from .subscription_add_on_price_override import SubscriptionAddOnPriceOverride
    from .subscription_component import SubscriptionComponent
    from .subscription_coupon import SubscriptionCoupon
    from .subscription_create_request import SubscriptionCreateRequest
    from .subscription_credit import SubscriptionCredit
    from .subscription_details import SubscriptionDetails
    from .subscription_event import SubscriptionEvent
    from .subscription_event_data import SubscriptionEventData
    from .subscription_fee import SubscriptionFee
    from .subscription_fee_billing_period_enum import (
        SubscriptionFeeBillingPeriodEnum,
        SubscriptionFeeBillingPeriodEnumLiteral,
    )
    from .subscription_id import SubscriptionId
    from .subscription_list_response import SubscriptionListResponse
    from .subscription_status_enum import (
        SubscriptionStatusEnum,
        SubscriptionStatusEnumLiteral,
    )
    from .subscription_update_request import SubscriptionUpdateRequest
    from .subscription_update_response import SubscriptionUpdateResponse
    from .subscription_update_type import (
        SubscriptionUpdateType,
        SubscriptionUpdateTypeLiteral,
    )
    from .tax_breakdown_item import TaxBreakdownItem
    from .tax_exemption_type import TaxExemptionType, TaxExemptionTypeLiteral
    from .tenant_id import TenantId
    from .term_rate import TermRate
    from .text_config_value import TextConfigValue
    from .tier_row import TierRow
    from .tiered_plan_pricing import TieredPlanPricing
    from .tiered_pricing import TieredPricing
    from .token_introspection_response import TokenIntrospectionResponse
    from .token_request import TokenRequest
    from .token_response import TokenResponse
    from .top_up_collection import TopUpCollection, TopUpCollectionLiteral
    from .top_up_response import TopUpResponse
    from .top_up_status import TopUpStatus, TopUpStatusLiteral
    from .transaction import Transaction
    from .trial_config import TrialConfig
    from .unattributed_metric_usage import UnattributedMetricUsage
    from .unattributed_usage_response import UnattributedUsageResponse
    from .unit_conversion import UnitConversion
    from .unit_conversion_rounding_enum import (
        UnitConversionRoundingEnum,
        UnitConversionRoundingEnumLiteral,
    )
    from .update_add_on_request import UpdateAddOnRequest
    from .update_coupon_request import UpdateCouponRequest
    from .update_entitlement_request import UpdateEntitlementRequest
    from .update_feature_request import UpdateFeatureRequest
    from .update_metric_request import UpdateMetricRequest
    from .update_product_request import UpdateProductRequest
    from .update_webhook_endpoint_request import UpdateWebhookEndpointRequest
    from .usage_at_zero import UsageAtZero, UsageAtZeroLiteral
    from .usage_cost import UsageCost
    from .usage_cost_list_response import UsageCostListResponse
    from .usage_cost_row import UsageCostRow
    from .usage_cost_unit import UsageCostUnit, UsageCostUnitLiteral
    from .usage_event import UsageEvent
    from .usage_event_list_response import UsageEventListResponse
    from .usage_fee import UsageFee
    from .usage_fee_structure import UsageFeeStructure
    from .usage_filter import UsageFilter
    from .usage_limit_id import UsageLimitId
    from .usage_model_enum import UsageModelEnum, UsageModelEnumLiteral
    from .usage_plan_fee import UsagePlanFee
    from .usage_pricing import UsagePricing
    from .usage_pricing_model import UsagePricingModel
    from .usage_response import UsageResponse
    from .volume_plan_pricing import VolumePlanPricing
    from .volume_pricing import VolumePricing
    from .wallet import Wallet
    from .wallet_balance_low_event import WalletBalanceLowEvent
    from .wallet_balance_low_event_data import WalletBalanceLowEventData
    from .wallet_check import WalletCheck
    from .wallet_credit_recovered_event import WalletCreditRecoveredEvent
    from .wallet_credit_recovered_event_data import WalletCreditRecoveredEventData
    from .wallet_credit_unrecovered_event import WalletCreditUnrecoveredEvent
    from .wallet_credit_unrecovered_event_data import WalletCreditUnrecoveredEventData
    from .wallet_debited_event import WalletDebitedEvent
    from .wallet_debited_event_data import WalletDebitedEventData
    from .wallet_depleted_event import WalletDepletedEvent
    from .wallet_depleted_event_data import WalletDepletedEventData
    from .wallet_funded_event import WalletFundedEvent
    from .wallet_funded_event_data import WalletFundedEventData
    from .wallet_list_response import WalletListResponse
    from .wallet_recovered_event import WalletRecoveredEvent
    from .wallet_recovered_event_data import WalletRecoveredEventData
    from .webhook_delivery import WebhookDelivery
    from .webhook_delivery_id import WebhookDeliveryId
    from .webhook_delivery_list_response import WebhookDeliveryListResponse
    from .webhook_delivery_status import (
        WebhookDeliveryStatus,
        WebhookDeliveryStatusLiteral,
    )
    from .webhook_endpoint import WebhookEndpoint
    from .webhook_endpoint_disabled_reason import (
        WebhookEndpointDisabledReason,
        WebhookEndpointDisabledReasonLiteral,
    )
    from .webhook_endpoint_id import WebhookEndpointId
    from .webhook_endpoint_list_response import WebhookEndpointListResponse
    from .webhook_endpoint_secret import WebhookEndpointSecret
    from .webhook_header import WebhookHeader
    from .webhook_header_input import WebhookHeaderInput

_MODULES: dict[str, str] = {
    "Actor": "actor",
    "ActorType": "actor_type",
    "ActorTypeLiteral": "actor_type",
    "AddOn": "add_on",
    "AddOnEvent": "add_on_event",
    "AddOnEventData": "add_on_event_data",
    "AddOnId": "add_on_id",
    "AddOnListResponse": "add_on_list_response",
    "Address": "address",
    "AllComponentsScope": "all_components_scope",
    "AppliedCoupon": "applied_coupon",
    "AppliedCouponDetailed": "applied_coupon_detailed",
    "AppliedCouponId": "applied_coupon_id",
    "AutoTopUp": "auto_top_up",
    "AutoTopUpCapReachedEvent": "auto_top_up_cap_reached_event",
    "AutoTopUpCapReachedEventData": "auto_top_up_cap_reached_event_data",
    "AutoTopUpConsentChangedEvent": "auto_top_up_consent_changed_event",
    "AutoTopUpConsentChangedEventData": "auto_top_up_consent_changed_event_data",
    "AutoTopUpEvent": "auto_top_up_event",
    "AutoTopUpEventData": "auto_top_up_event_data",
    "AutoTopUpMethod": "auto_top_up_method",
    "AutoTopUpMethodLiteral": "auto_top_up_method",
    "AutoTopUpStatus": "auto_top_up_status",
    "AutoTopUpStatusLiteral": "auto_top_up_status",
    "AutoTopUpWriteRequest": "auto_top_up_write_request",
    "AvailableParameters": "available_parameters",
    "BankAccountId": "bank_account_id",
    "BankTransferPaymentMethodConfig": "bank_transfer_payment_method_config",
    "BatchJobChunkId": "batch_job_chunk_id",
    "BatchJobDetailResponse": "batch_job_detail_response",
    "BatchJobFailuresResponse": "batch_job_failures_response",
    "BatchJobId": "batch_job_id",
    "BatchJobItemFailureResponse": "batch_job_item_failure_response",
    "BatchJobListResponse": "batch_job_list_response",
    "BatchJobResponse": "batch_job_response",
    "BatchJobStatus": "batch_job_status",
    "BatchJobStatusLiteral": "batch_job_status",
    "BatchJobType": "batch_job_type",
    "BatchJobTypeLiteral": "batch_job_type",
    "BillableMetricId": "billable_metric_id",
    "BillingConfig": "billing_config",
    "BillingCycleResetPeriod": "billing_cycle_reset_period",
    "BillingMetricAggregateEnum": "billing_metric_aggregate_enum",
    "BillingMetricAggregateEnumLiteral": "billing_metric_aggregate_enum",
    "BillingPeriodEnum": "billing_period_enum",
    "BillingPeriodEnumLiteral": "billing_period_enum",
    "BillingType": "billing_type",
    "BillingTypeLiteral": "billing_type",
    "BillingTypeEnum": "billing_type_enum",
    "BillingTypeEnumLiteral": "billing_type_enum",
    "BooleanConfigValue": "boolean_config_value",
    "BooleanEffectiveEntitlementValue": "boolean_effective_entitlement_value",
    "BooleanEntitlementValue": "boolean_entitlement_value",
    "BooleanFeatureType": "boolean_feature_type",
    "BooleanResolvedEntitlementValue": "boolean_resolved_entitlement_value",
    "Budget": "budget",
    "BudgetAuthor": "budget_author",
    "BudgetAuthorLiteral": "budget_author",
    "BudgetBehavior": "budget_behavior",
    "BudgetBehaviorLiteral": "budget_behavior",
    "BudgetListResponse": "budget_list_response",
    "BudgetPeriod": "budget_period",
    "CalendarResetPeriod": "calendar_reset_period",
    "CalendarUnit": "calendar_unit",
    "CalendarUnitLiteral": "calendar_unit",
    "CancelCheckoutSessionResponse": "cancel_checkout_session_response",
    "CancelSubscriptionRequest": "cancel_subscription_request",
    "CancelSubscriptionResponse": "cancel_subscription_response",
    "CapacityFee": "capacity_fee",
    "CapacityFeeStructure": "capacity_fee_structure",
    "CapacityPlanFee": "capacity_plan_fee",
    "CapacityPricing": "capacity_pricing",
    "CapacityThreshold": "capacity_threshold",
    "CheckoutSession": "checkout_session",
    "CheckoutSessionId": "checkout_session_id",
    "CheckoutSessionStatus": "checkout_session_status",
    "CheckoutSessionStatusLiteral": "checkout_session_status",
    "CheckoutType": "checkout_type",
    "CheckoutTypeLiteral": "checkout_type",
    "ComponentOverride": "component_override",
    "ComponentParameterization": "component_parameterization",
    "ComponentParameters": "component_parameters",
    "ComponentsScope": "components_scope",
    "ConfigEffectiveEntitlementValue": "config_effective_entitlement_value",
    "ConfigEntitlementValue": "config_entitlement_value",
    "ConfigFeatureType": "config_feature_type",
    "ConfigResolvedEntitlementValue": "config_resolved_entitlement_value",
    "ConfigValue": "config_value",
    "ConfigValueType": "config_value_type",
    "ConfigValueTypeLiteral": "config_value_type",
    "ConnectedAccount": "connected_account",
    "ConnectedAccountId": "connected_account_id",
    "ConnectedAccountsResponse": "connected_accounts_response",
    "ConnectionStatus": "connection_status",
    "ConnectionStatusLiteral": "connection_status",
    "ConnectionType": "connection_type",
    "ConnectionTypeLiteral": "connection_type",
    "CountryCode": "country_code",
    "Coupon": "coupon",
    "CouponCreditScope": "coupon_credit_scope",
    "CouponCreditScopeLiteral": "coupon_credit_scope",
    "CouponDiscount": "coupon_discount",
    "CouponEvent": "coupon_event",
    "CouponEventData": "coupon_event_data",
    "CouponFilter": "coupon_filter",
    "CouponFilterLiteral": "coupon_filter",
    "CouponId": "coupon_id",
    "CouponLineItem": "coupon_line_item",
    "CouponListResponse": "coupon_list_response",
    "CreateAddOnRequest": "create_add_on_request",
    "CreateBudgetRequest": "create_budget_request",
    "CreateCheckoutSessionRequest": "create_checkout_session_request",
    "CreateCheckoutSessionResponse": "create_checkout_session_response",
    "CreateConnectedAccountRequest": "create_connected_account_request",
    "CreateConnectedAccountResponse": "create_connected_account_response",
    "CreateCouponRequest": "create_coupon_request",
    "CreateCreditGrantRequest": "create_credit_grant_request",
    "CreateEntitlementsRequest": "create_entitlements_request",
    "CreateFeatureRequest": "create_feature_request",
    "CreateMetricRequest": "create_metric_request",
    "CreateOAuthAppRequest": "create_o_auth_app_request",
    "CreateOnboardingLinkRequest": "create_onboarding_link_request",
    "CreatePlanRequest": "create_plan_request",
    "CreateProductRequest": "create_product_request",
    "CreateSubscriptionAddOn": "create_subscription_add_on",
    "CreateSubscriptionComponents": "create_subscription_components",
    "CreateTopUpRequest": "create_top_up_request",
    "CreateWebhookEndpointRequest": "create_webhook_endpoint_request",
    "CreatedWebhookEndpoint": "created_webhook_endpoint",
    "CreditAppliesTo": "credit_applies_to",
    "CreditAppliesToLiteral": "credit_applies_to",
    "CreditCap": "credit_cap",
    "CreditCaps": "credit_caps",
    "CreditCost": "credit_cost",
    "CreditCostRequest": "credit_cost_request",
    "CreditDiscount": "credit_discount",
    "CreditExhaustedRule": "credit_exhausted_rule",
    "CreditExhaustedRuleInvoiceVariant": "credit_exhausted_rule_invoice_variant",
    "CreditExhaustedRulePauseVariant": "credit_exhausted_rule_pause_variant",
    "CreditExpiryUnit": "credit_expiry_unit",
    "CreditExpiryUnitLiteral": "credit_expiry_unit",
    "CreditFee": "credit_fee",
    "CreditFeeStructure": "credit_fee_structure",
    "CreditGrant": "credit_grant",
    "CreditGrantExpiredEvent": "credit_grant_expired_event",
    "CreditGrantExpiredEventData": "credit_grant_expired_event_data",
    "CreditGrantId": "credit_grant_id",
    "CreditGrantKind": "credit_grant_kind",
    "CreditGrantKindLiteral": "credit_grant_kind",
    "CreditGrantLapseReason": "credit_grant_lapse_reason",
    "CreditGrantLapseReasonLiteral": "credit_grant_lapse_reason",
    "CreditGrantListResponse": "credit_grant_list_response",
    "CreditGrantSource": "credit_grant_source",
    "CreditGrantSourceLiteral": "credit_grant_source",
    "CreditGrantStatus": "credit_grant_status",
    "CreditGrantStatusLiteral": "credit_grant_status",
    "CreditGrantType": "credit_grant_type",
    "CreditGrantTypeLiteral": "credit_grant_type",
    "CreditNote": "credit_note",
    "CreditNoteCustomPropertiesRequest": "credit_note_custom_properties_request",
    "CreditNoteEvent": "credit_note_event",
    "CreditNoteEventData": "credit_note_event_data",
    "CreditNoteId": "credit_note_id",
    "CreditNoteListResponse": "credit_note_list_response",
    "CreditNoteStatus": "credit_note_status",
    "CreditNoteStatusLiteral": "credit_note_status",
    "CreditPackExpiry": "credit_pack_expiry",
    "CreditPackRollover": "credit_pack_rollover",
    "CreditPackUnit": "credit_pack_unit",
    "CreditPlanFee": "credit_plan_fee",
    "CreditType": "credit_type",
    "CreditTypeLiteral": "credit_type",
    "CreditUnit": "credit_unit",
    "CreditUnitCreateRequest": "credit_unit_create_request",
    "CreditUnitListResponse": "credit_unit_list_response",
    "CreditUnitPrice": "credit_unit_price",
    "CreditUnitPriceListResponse": "credit_unit_price_list_response",
    "CreditUnitPriceSetRequest": "credit_unit_price_set_request",
    "CreditUnitUpdateRequest": "credit_unit_update_request",
    "Currency": "currency",
    "CurrencyLiteral": "currency",
    "CustomPropertyDefinition": "custom_property_definition",
    "CustomPropertyDefinitionCreateRequest": "custom_property_definition_create_request",
    "CustomPropertyDefinitionId": "custom_property_definition_id",
    "CustomPropertyDefinitionListResponse": "custom_property_definition_list_response",
    "CustomPropertyDefinitionUpdateRequest": "custom_property_definition_update_request",
    "CustomPropertyEntityType": "custom_property_entity_type",
    "CustomPropertyEntityTypeLiteral": "custom_property_entity_type",
    "CustomPropertyType": "custom_property_type",
    "CustomPropertyTypeLiteral": "custom_property_type",
    "CustomTaxRate": "custom_tax_rate",
    "Customer": "customer",
    "CustomerCreateRequest": "customer_create_request",
    "CustomerDetails": "customer_details",
    "CustomerEvent": "customer_event",
    "CustomerEventData": "customer_event_data",
    "CustomerId": "customer_id",
    "CustomerListResponse": "customer_list_response",
    "CustomerPatchRequest": "customer_patch_request",
    "CustomerPaymentMethodId": "customer_payment_method_id",
    "CustomerPortalScope": "customer_portal_scope",
    "CustomerPortalScopeLiteral": "customer_portal_scope",
    "CustomerPortalTokenRequest": "customer_portal_token_request",
    "CustomerPortalTokenResponse": "customer_portal_token_response",
    "CustomerType": "customer_type",
    "CustomerTypeLiteral": "customer_type",
    "CustomerUpdateRequest": "customer_update_request",
    "DeclineKind": "decline_kind",
    "DeclineKindLiteral": "decline_kind",
    "DoubleSegmentationMatrix": "double_segmentation_matrix",
    "EInvoicingFinding": "e_invoicing_finding",
    "EInvoicingStatus": "e_invoicing_status",
    "EInvoicingStatusLiteral": "e_invoicing_status",
    "EffectiveEntitlement": "effective_entitlement",
    "EffectiveEntitlementListResponse": "effective_entitlement_list_response",
    "EffectiveEntitlementValue": "effective_entitlement_value",
    "Entitlement": "entitlement",
    "EntitlementCheck": "entitlement_check",
    "EntitlementCheckFeature": "entitlement_check_feature",
    "EntitlementCheckLimit": "entitlement_check_limit",
    "EntitlementCheckLimitBehavior": "entitlement_check_limit_behavior",
    "EntitlementCheckLimitBehaviorLiteral": "entitlement_check_limit_behavior",
    "EntitlementCheckPeriod": "entitlement_check_period",
    "EntitlementCheckReason": "entitlement_check_reason",
    "EntitlementCheckReasonLiteral": "entitlement_check_reason",
    "EntitlementId": "entitlement_id",
    "EntitlementListResponse": "entitlement_list_response",
    "EntitlementOverageBehavior": "entitlement_overage_behavior",
    "EntitlementOverageBehaviorLiteral": "entitlement_overage_behavior",
    "EntitlementProductRef": "entitlement_product_ref",
    "EntitlementSpecRequest": "entitlement_spec_request",
    "EntitlementValue": "entitlement_value",
    "ErrorCode": "error_code",
    "ErrorCodeLiteral": "error_code",
    "Event": "event",
    "EventId": "event_id",
    "EventType": "event_type",
    "EventTypeLiteral": "event_type",
    "ExistingPriceRef": "existing_price_ref",
    "ExistingProductRef": "existing_product_ref",
    "ExternalPaymentMethodConfig": "external_payment_method_config",
    "ExtraComponent": "extra_component",
    "ExtraRecurringBillingTypeEnum": "extra_recurring_billing_type_enum",
    "ExtraRecurringBillingTypeEnumLiteral": "extra_recurring_billing_type_enum",
    "ExtraRecurringFeeStructure": "extra_recurring_fee_structure",
    "ExtraRecurringPlanFee": "extra_recurring_plan_fee",
    "ExtraRecurringPricing": "extra_recurring_pricing",
    "Feature": "feature",
    "FeatureId": "feature_id",
    "FeatureListResponse": "feature_list_response",
    "FeatureRef": "feature_ref",
    "FeatureStatus": "feature_status",
    "FeatureStatusLiteral": "feature_status",
    "FeatureType": "feature_type",
    "Fee": "fee",
    "FeeCreditUnit": "fee_credit_unit",
    "FixedDiscount": "fixed_discount",
    "FixedWindowResetPeriod": "fixed_window_reset_period",
    "GetCheckoutSessionResponse": "get_checkout_session_response",
    "GroupedUsage": "grouped_usage",
    "IngestEventsRequest": "ingest_events_request",
    "IngestEventsResponse": "ingest_events_response",
    "IngestFailure": "ingest_failure",
    "IntrospectionRequest": "introspection_request",
    "Invoice": "invoice",
    "InvoiceCustomPropertiesRequest": "invoice_custom_properties_request",
    "InvoiceDocumentsEvent": "invoice_documents_event",
    "InvoiceDocumentsEventData": "invoice_documents_event_data",
    "InvoiceEvent": "invoice_event",
    "InvoiceEventData": "invoice_event_data",
    "InvoiceId": "invoice_id",
    "InvoiceLineCreditUnit": "invoice_line_credit_unit",
    "InvoiceLineItem": "invoice_line_item",
    "InvoiceListResponse": "invoice_list_response",
    "InvoicePaymentStatus": "invoice_payment_status",
    "InvoicePaymentStatusLiteral": "invoice_payment_status",
    "InvoiceStatus": "invoice_status",
    "InvoiceStatusLiteral": "invoice_status",
    "InvoiceType": "invoice_type",
    "InvoiceTypeLiteral": "invoice_type",
    "InvoicingEntityId": "invoicing_entity_id",
    "IssueLicenseRequest": "issue_license_request",
    "IssueLicenseResponse": "issue_license_response",
    "IssueOfflineLicenseRequest": "issue_offline_license_request",
    "JsonConfigValue": "json_config_value",
    "LedgerEntry": "ledger_entry",
    "LedgerEntryId": "ledger_entry_id",
    "LedgerEntryType": "ledger_entry_type",
    "LedgerEntryTypeLiteral": "ledger_entry_type",
    "LedgerListResponse": "ledger_list_response",
    "License": "license",
    "LicenseActivationCode": "license_activation_code",
    "LicenseId": "license_id",
    "LicenseListResponse": "license_list_response",
    "LicenseSigningKey": "license_signing_key",
    "LicenseSigningKeyStatus": "license_signing_key_status",
    "LicenseSigningKeyStatusLiteral": "license_signing_key_status",
    "LicenseSigningKeysResponse": "license_signing_keys_response",
    "LicenseStatus": "license_status",
    "LicenseStatusLiteral": "license_status",
    "LicensingEndpoints": "licensing_endpoints",
    "LinkedSegmentationMatrix": "linked_segmentation_matrix",
    "ListCheckoutSessionsResponse": "list_checkout_sessions_response",
    "ListCustomerUsageCostsGranularity": "list_customer_usage_costs_granularity",
    "ListCustomerUsageCostsGranularityLiteral": "list_customer_usage_costs_granularity",
    "ListSubscriptionUsageCostsGranularity": "list_subscription_usage_costs_granularity",
    "ListSubscriptionUsageCostsGranularityLiteral": "list_subscription_usage_costs_granularity",
    "MatrixDimension": "matrix_dimension",
    "MatrixPlanPricing": "matrix_plan_pricing",
    "MatrixPricing": "matrix_pricing",
    "MatrixRow": "matrix_row",
    "MeteredEffectiveEntitlementValue": "metered_effective_entitlement_value",
    "MeteredEntitlementSpec": "metered_entitlement_spec",
    "MeteredEntitlementUsage": "metered_entitlement_usage",
    "MeteredEntitlementValue": "metered_entitlement_value",
    "MeteredFeatureType": "metered_feature_type",
    "MeteredResolvedEntitlementValue": "metered_resolved_entitlement_value",
    "Metric": "metric",
    "MetricDimension": "metric_dimension",
    "MetricEvent": "metric_event",
    "MetricEventData": "metric_event_data",
    "MetricFilter": "metric_filter",
    "MetricFilterOperator": "metric_filter_operator",
    "MetricFilterOperatorLiteral": "metric_filter_operator",
    "MetricListResponse": "metric_list_response",
    "MetricSegmentationMatrix": "metric_segmentation_matrix",
    "MetricSummary": "metric_summary",
    "MetricUsage": "metric_usage",
    "MinimumCommitment": "minimum_commitment",
    "MinimumCommitmentInput": "minimum_commitment_input",
    "MinimumCommitmentInputScope": "minimum_commitment_input_scope",
    "MinimumCommitmentScope": "minimum_commitment_scope",
    "NeverResetPeriod": "never_reset_period",
    "NewProductRef": "new_product_ref",
    "NumberConfigValue": "number_config_value",
    "OAuthApp": "o_auth_app",
    "OAuthAppId": "o_auth_app_id",
    "OAuthAppWithSecret": "o_auth_app_with_secret",
    "OAuthAppsResponse": "o_auth_apps_response",
    "OAuthErrorCode": "o_auth_error_code",
    "OAuthErrorCodeLiteral": "o_auth_error_code",
    "OAuthErrorResponse": "o_auth_error_response",
    "OfflineLicense": "offline_license",
    "OnboardingLinkResponse": "onboarding_link_response",
    "OnboardingMode": "onboarding_mode",
    "OnboardingModeLiteral": "onboarding_mode",
    "OneTimeFee": "one_time_fee",
    "OneTimeFeeStructure": "one_time_fee_structure",
    "OneTimePlanFee": "one_time_plan_fee",
    "OneTimePricing": "one_time_pricing",
    "OnlineMethodConfig": "online_method_config",
    "OnlineMethodsConfig": "online_methods_config",
    "OnlinePaymentMethodConfig": "online_payment_method_config",
    "OrganizationId": "organization_id",
    "PackagePlanPricing": "package_plan_pricing",
    "PackagePricing": "package_pricing",
    "PaginationResponse": "pagination_response",
    "PatchBudgetRequest": "patch_budget_request",
    "PatchPlanRequest": "patch_plan_request",
    "PatchWalletRequest": "patch_wallet_request",
    "PaymentEvent": "payment_event",
    "PaymentMethodInfo": "payment_method_info",
    "PaymentMethodTypeEnum": "payment_method_type_enum",
    "PaymentMethodTypeEnumLiteral": "payment_method_type_enum",
    "PaymentMethodsConfig": "payment_methods_config",
    "PaymentStatusEnum": "payment_status_enum",
    "PaymentStatusEnumLiteral": "payment_status_enum",
    "PaymentTransactionId": "payment_transaction_id",
    "PaymentTypeEnum": "payment_type_enum",
    "PaymentTypeEnumLiteral": "payment_type_enum",
    "PerUnitPlanPricing": "per_unit_plan_pricing",
    "PerUnitPricing": "per_unit_pricing",
    "PercentageDiscount": "percentage_discount",
    "Plan": "plan",
    "PlanAddOnInput": "plan_add_on_input",
    "PlanEvent": "plan_event",
    "PlanEventData": "plan_event_data",
    "PlanFeeCreditUnit": "plan_fee_credit_unit",
    "PlanId": "plan_id",
    "PlanListResponse": "plan_list_response",
    "PlanStatusEnum": "plan_status_enum",
    "PlanStatusEnumLiteral": "plan_status_enum",
    "PlanTypeEnum": "plan_type_enum",
    "PlanTypeEnumLiteral": "plan_type_enum",
    "PlanUsagePricingModel": "plan_usage_pricing_model",
    "PlanVersionId": "plan_version_id",
    "PlanVersionListResponse": "plan_version_list_response",
    "PlanVersionSummary": "plan_version_summary",
    "PriceComponent": "price_component",
    "PriceComponentId": "price_component_id",
    "PriceComponentInput": "price_component_input",
    "PriceEntry": "price_entry",
    "PriceId": "price_id",
    "PriceInput": "price_input",
    "Pricing": "pricing",
    "Product": "product",
    "ProductEvent": "product_event",
    "ProductEventData": "product_event_data",
    "ProductFamily": "product_family",
    "ProductFamilyCreateRequest": "product_family_create_request",
    "ProductFamilyId": "product_family_id",
    "ProductFamilyListResponse": "product_family_list_response",
    "ProductFeeStructure": "product_fee_structure",
    "ProductFeeTypeEnum": "product_fee_type_enum",
    "ProductFeeTypeEnumLiteral": "product_fee_type_enum",
    "ProductId": "product_id",
    "ProductListResponse": "product_list_response",
    "ProductRef": "product_ref",
    "ProductsScope": "products_scope",
    "PropertyConfig": "property_config",
    "QuoteEvent": "quote_event",
    "QuoteEventData": "quote_event_data",
    "QuoteId": "quote_id",
    "RateFee": "rate_fee",
    "RateFeeStructure": "rate_fee_structure",
    "RatePlanFee": "rate_plan_fee",
    "RatePricing": "rate_pricing",
    "RecurringFee": "recurring_fee",
    "RefundEventData": "refund_event_data",
    "RefundMode": "refund_mode",
    "RefundModeLiteral": "refund_mode",
    "ReplacePlanRequest": "replace_plan_request",
    "ResetPeriod": "reset_period",
    "ResolvedEntitlement": "resolved_entitlement",
    "ResolvedEntitlementListResponse": "resolved_entitlement_list_response",
    "ResolvedEntitlementValue": "resolved_entitlement_value",
    "RestErrorResponse": "rest_error_response",
    "ReversalKind": "reversal_kind",
    "ReversalKindLiteral": "reversal_kind",
    "RevocationRequest": "revocation_request",
    "RevokeLicenseRequest": "revoke_license_request",
    "RotatedSecret": "rotated_secret",
    "SelectOption": "select_option",
    "ShippingAddress": "shipping_address",
    "SlidingWindowResetPeriod": "sliding_window_reset_period",
    "SlotDowngradePolicyEnum": "slot_downgrade_policy_enum",
    "SlotDowngradePolicyEnumLiteral": "slot_downgrade_policy_enum",
    "SlotFee": "slot_fee",
    "SlotFeeStructure": "slot_fee_structure",
    "SlotPlanFee": "slot_plan_fee",
    "SlotPricing": "slot_pricing",
    "SlotUpgradePolicyEnum": "slot_upgrade_policy_enum",
    "SlotUpgradePolicyEnumLiteral": "slot_upgrade_policy_enum",
    "SubLineItem": "sub_line_item",
    "Subscription": "subscription",
    "SubscriptionActivationConditionEnum": "subscription_activation_condition_enum",
    "SubscriptionActivationConditionEnumLiteral": "subscription_activation_condition_enum",
    "SubscriptionAddOn": "subscription_add_on",
    "SubscriptionAddOnCustomization": "subscription_add_on_customization",
    "SubscriptionAddOnId": "subscription_add_on_id",
    "SubscriptionAddOnParameterization": "subscription_add_on_parameterization",
    "SubscriptionAddOnPriceOverride": "subscription_add_on_price_override",
    "SubscriptionComponent": "subscription_component",
    "SubscriptionCoupon": "subscription_coupon",
    "SubscriptionCreateRequest": "subscription_create_request",
    "SubscriptionCredit": "subscription_credit",
    "SubscriptionDetails": "subscription_details",
    "SubscriptionEvent": "subscription_event",
    "SubscriptionEventData": "subscription_event_data",
    "SubscriptionFee": "subscription_fee",
    "SubscriptionFeeBillingPeriodEnum": "subscription_fee_billing_period_enum",
    "SubscriptionFeeBillingPeriodEnumLiteral": "subscription_fee_billing_period_enum",
    "SubscriptionId": "subscription_id",
    "SubscriptionListResponse": "subscription_list_response",
    "SubscriptionStatusEnum": "subscription_status_enum",
    "SubscriptionStatusEnumLiteral": "subscription_status_enum",
    "SubscriptionUpdateRequest": "subscription_update_request",
    "SubscriptionUpdateResponse": "subscription_update_response",
    "SubscriptionUpdateType": "subscription_update_type",
    "SubscriptionUpdateTypeLiteral": "subscription_update_type",
    "TaxBreakdownItem": "tax_breakdown_item",
    "TaxExemptionType": "tax_exemption_type",
    "TaxExemptionTypeLiteral": "tax_exemption_type",
    "TenantId": "tenant_id",
    "TermRate": "term_rate",
    "TextConfigValue": "text_config_value",
    "TierRow": "tier_row",
    "TieredPlanPricing": "tiered_plan_pricing",
    "TieredPricing": "tiered_pricing",
    "TokenIntrospectionResponse": "token_introspection_response",
    "TokenRequest": "token_request",
    "TokenResponse": "token_response",
    "TopUpCollection": "top_up_collection",
    "TopUpCollectionLiteral": "top_up_collection",
    "TopUpResponse": "top_up_response",
    "TopUpStatus": "top_up_status",
    "TopUpStatusLiteral": "top_up_status",
    "Transaction": "transaction",
    "TrialConfig": "trial_config",
    "UnattributedMetricUsage": "unattributed_metric_usage",
    "UnattributedUsageResponse": "unattributed_usage_response",
    "UnitConversion": "unit_conversion",
    "UnitConversionRoundingEnum": "unit_conversion_rounding_enum",
    "UnitConversionRoundingEnumLiteral": "unit_conversion_rounding_enum",
    "UpdateAddOnRequest": "update_add_on_request",
    "UpdateCouponRequest": "update_coupon_request",
    "UpdateEntitlementRequest": "update_entitlement_request",
    "UpdateFeatureRequest": "update_feature_request",
    "UpdateMetricRequest": "update_metric_request",
    "UpdateProductRequest": "update_product_request",
    "UpdateWebhookEndpointRequest": "update_webhook_endpoint_request",
    "UsageAtZero": "usage_at_zero",
    "UsageAtZeroLiteral": "usage_at_zero",
    "UsageCost": "usage_cost",
    "UsageCostListResponse": "usage_cost_list_response",
    "UsageCostRow": "usage_cost_row",
    "UsageCostUnit": "usage_cost_unit",
    "UsageCostUnitLiteral": "usage_cost_unit",
    "UsageEvent": "usage_event",
    "UsageEventListResponse": "usage_event_list_response",
    "UsageFee": "usage_fee",
    "UsageFeeStructure": "usage_fee_structure",
    "UsageFilter": "usage_filter",
    "UsageLimitId": "usage_limit_id",
    "UsageModelEnum": "usage_model_enum",
    "UsageModelEnumLiteral": "usage_model_enum",
    "UsagePlanFee": "usage_plan_fee",
    "UsagePricing": "usage_pricing",
    "UsagePricingModel": "usage_pricing_model",
    "UsageResponse": "usage_response",
    "VolumePlanPricing": "volume_plan_pricing",
    "VolumePricing": "volume_pricing",
    "Wallet": "wallet",
    "WalletBalanceLowEvent": "wallet_balance_low_event",
    "WalletBalanceLowEventData": "wallet_balance_low_event_data",
    "WalletCheck": "wallet_check",
    "WalletCreditRecoveredEvent": "wallet_credit_recovered_event",
    "WalletCreditRecoveredEventData": "wallet_credit_recovered_event_data",
    "WalletCreditUnrecoveredEvent": "wallet_credit_unrecovered_event",
    "WalletCreditUnrecoveredEventData": "wallet_credit_unrecovered_event_data",
    "WalletDebitedEvent": "wallet_debited_event",
    "WalletDebitedEventData": "wallet_debited_event_data",
    "WalletDepletedEvent": "wallet_depleted_event",
    "WalletDepletedEventData": "wallet_depleted_event_data",
    "WalletFundedEvent": "wallet_funded_event",
    "WalletFundedEventData": "wallet_funded_event_data",
    "WalletListResponse": "wallet_list_response",
    "WalletRecoveredEvent": "wallet_recovered_event",
    "WalletRecoveredEventData": "wallet_recovered_event_data",
    "WebhookDelivery": "webhook_delivery",
    "WebhookDeliveryId": "webhook_delivery_id",
    "WebhookDeliveryListResponse": "webhook_delivery_list_response",
    "WebhookDeliveryStatus": "webhook_delivery_status",
    "WebhookDeliveryStatusLiteral": "webhook_delivery_status",
    "WebhookEndpoint": "webhook_endpoint",
    "WebhookEndpointDisabledReason": "webhook_endpoint_disabled_reason",
    "WebhookEndpointDisabledReasonLiteral": "webhook_endpoint_disabled_reason",
    "WebhookEndpointId": "webhook_endpoint_id",
    "WebhookEndpointListResponse": "webhook_endpoint_list_response",
    "WebhookEndpointSecret": "webhook_endpoint_secret",
    "WebhookHeader": "webhook_header",
    "WebhookHeaderInput": "webhook_header_input",
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
    "UNSET",
    "Unset",
    "UnknownVariant",
    "Actor",
    "ActorType",
    "ActorTypeLiteral",
    "AddOn",
    "AddOnEvent",
    "AddOnEventData",
    "AddOnId",
    "AddOnListResponse",
    "Address",
    "AllComponentsScope",
    "AppliedCoupon",
    "AppliedCouponDetailed",
    "AppliedCouponId",
    "AutoTopUp",
    "AutoTopUpCapReachedEvent",
    "AutoTopUpCapReachedEventData",
    "AutoTopUpConsentChangedEvent",
    "AutoTopUpConsentChangedEventData",
    "AutoTopUpEvent",
    "AutoTopUpEventData",
    "AutoTopUpMethod",
    "AutoTopUpMethodLiteral",
    "AutoTopUpStatus",
    "AutoTopUpStatusLiteral",
    "AutoTopUpWriteRequest",
    "AvailableParameters",
    "BankAccountId",
    "BankTransferPaymentMethodConfig",
    "BatchJobChunkId",
    "BatchJobDetailResponse",
    "BatchJobFailuresResponse",
    "BatchJobId",
    "BatchJobItemFailureResponse",
    "BatchJobListResponse",
    "BatchJobResponse",
    "BatchJobStatus",
    "BatchJobStatusLiteral",
    "BatchJobType",
    "BatchJobTypeLiteral",
    "BillableMetricId",
    "BillingConfig",
    "BillingCycleResetPeriod",
    "BillingMetricAggregateEnum",
    "BillingMetricAggregateEnumLiteral",
    "BillingPeriodEnum",
    "BillingPeriodEnumLiteral",
    "BillingType",
    "BillingTypeLiteral",
    "BillingTypeEnum",
    "BillingTypeEnumLiteral",
    "BooleanConfigValue",
    "BooleanEffectiveEntitlementValue",
    "BooleanEntitlementValue",
    "BooleanFeatureType",
    "BooleanResolvedEntitlementValue",
    "Budget",
    "BudgetAuthor",
    "BudgetAuthorLiteral",
    "BudgetBehavior",
    "BudgetBehaviorLiteral",
    "BudgetListResponse",
    "BudgetPeriod",
    "CalendarResetPeriod",
    "CalendarUnit",
    "CalendarUnitLiteral",
    "CancelCheckoutSessionResponse",
    "CancelSubscriptionRequest",
    "CancelSubscriptionResponse",
    "CapacityFee",
    "CapacityFeeStructure",
    "CapacityPlanFee",
    "CapacityPricing",
    "CapacityThreshold",
    "CheckoutSession",
    "CheckoutSessionId",
    "CheckoutSessionStatus",
    "CheckoutSessionStatusLiteral",
    "CheckoutType",
    "CheckoutTypeLiteral",
    "ComponentOverride",
    "ComponentParameterization",
    "ComponentParameters",
    "ComponentsScope",
    "ConfigEffectiveEntitlementValue",
    "ConfigEntitlementValue",
    "ConfigFeatureType",
    "ConfigResolvedEntitlementValue",
    "ConfigValue",
    "ConfigValueType",
    "ConfigValueTypeLiteral",
    "ConnectedAccount",
    "ConnectedAccountId",
    "ConnectedAccountsResponse",
    "ConnectionStatus",
    "ConnectionStatusLiteral",
    "ConnectionType",
    "ConnectionTypeLiteral",
    "CountryCode",
    "Coupon",
    "CouponCreditScope",
    "CouponCreditScopeLiteral",
    "CouponDiscount",
    "CouponEvent",
    "CouponEventData",
    "CouponFilter",
    "CouponFilterLiteral",
    "CouponId",
    "CouponLineItem",
    "CouponListResponse",
    "CreateAddOnRequest",
    "CreateBudgetRequest",
    "CreateCheckoutSessionRequest",
    "CreateCheckoutSessionResponse",
    "CreateConnectedAccountRequest",
    "CreateConnectedAccountResponse",
    "CreateCouponRequest",
    "CreateCreditGrantRequest",
    "CreateEntitlementsRequest",
    "CreateFeatureRequest",
    "CreateMetricRequest",
    "CreateOAuthAppRequest",
    "CreateOnboardingLinkRequest",
    "CreatePlanRequest",
    "CreateProductRequest",
    "CreateSubscriptionAddOn",
    "CreateSubscriptionComponents",
    "CreateTopUpRequest",
    "CreateWebhookEndpointRequest",
    "CreatedWebhookEndpoint",
    "CreditAppliesTo",
    "CreditAppliesToLiteral",
    "CreditCap",
    "CreditCaps",
    "CreditCost",
    "CreditCostRequest",
    "CreditDiscount",
    "CreditExhaustedRule",
    "CreditExhaustedRuleInvoiceVariant",
    "CreditExhaustedRulePauseVariant",
    "CreditExpiryUnit",
    "CreditExpiryUnitLiteral",
    "CreditFee",
    "CreditFeeStructure",
    "CreditGrant",
    "CreditGrantExpiredEvent",
    "CreditGrantExpiredEventData",
    "CreditGrantId",
    "CreditGrantKind",
    "CreditGrantKindLiteral",
    "CreditGrantLapseReason",
    "CreditGrantLapseReasonLiteral",
    "CreditGrantListResponse",
    "CreditGrantSource",
    "CreditGrantSourceLiteral",
    "CreditGrantStatus",
    "CreditGrantStatusLiteral",
    "CreditGrantType",
    "CreditGrantTypeLiteral",
    "CreditNote",
    "CreditNoteCustomPropertiesRequest",
    "CreditNoteEvent",
    "CreditNoteEventData",
    "CreditNoteId",
    "CreditNoteListResponse",
    "CreditNoteStatus",
    "CreditNoteStatusLiteral",
    "CreditPackExpiry",
    "CreditPackRollover",
    "CreditPackUnit",
    "CreditPlanFee",
    "CreditType",
    "CreditTypeLiteral",
    "CreditUnit",
    "CreditUnitCreateRequest",
    "CreditUnitListResponse",
    "CreditUnitPrice",
    "CreditUnitPriceListResponse",
    "CreditUnitPriceSetRequest",
    "CreditUnitUpdateRequest",
    "Currency",
    "CurrencyLiteral",
    "CustomPropertyDefinition",
    "CustomPropertyDefinitionCreateRequest",
    "CustomPropertyDefinitionId",
    "CustomPropertyDefinitionListResponse",
    "CustomPropertyDefinitionUpdateRequest",
    "CustomPropertyEntityType",
    "CustomPropertyEntityTypeLiteral",
    "CustomPropertyType",
    "CustomPropertyTypeLiteral",
    "CustomTaxRate",
    "Customer",
    "CustomerCreateRequest",
    "CustomerDetails",
    "CustomerEvent",
    "CustomerEventData",
    "CustomerId",
    "CustomerListResponse",
    "CustomerPatchRequest",
    "CustomerPaymentMethodId",
    "CustomerPortalScope",
    "CustomerPortalScopeLiteral",
    "CustomerPortalTokenRequest",
    "CustomerPortalTokenResponse",
    "CustomerType",
    "CustomerTypeLiteral",
    "CustomerUpdateRequest",
    "DeclineKind",
    "DeclineKindLiteral",
    "DoubleSegmentationMatrix",
    "EInvoicingFinding",
    "EInvoicingStatus",
    "EInvoicingStatusLiteral",
    "EffectiveEntitlement",
    "EffectiveEntitlementListResponse",
    "EffectiveEntitlementValue",
    "Entitlement",
    "EntitlementCheck",
    "EntitlementCheckFeature",
    "EntitlementCheckLimit",
    "EntitlementCheckLimitBehavior",
    "EntitlementCheckLimitBehaviorLiteral",
    "EntitlementCheckPeriod",
    "EntitlementCheckReason",
    "EntitlementCheckReasonLiteral",
    "EntitlementId",
    "EntitlementListResponse",
    "EntitlementOverageBehavior",
    "EntitlementOverageBehaviorLiteral",
    "EntitlementProductRef",
    "EntitlementSpecRequest",
    "EntitlementValue",
    "ErrorCode",
    "ErrorCodeLiteral",
    "Event",
    "EventId",
    "EventType",
    "EventTypeLiteral",
    "ExistingPriceRef",
    "ExistingProductRef",
    "ExternalPaymentMethodConfig",
    "ExtraComponent",
    "ExtraRecurringBillingTypeEnum",
    "ExtraRecurringBillingTypeEnumLiteral",
    "ExtraRecurringFeeStructure",
    "ExtraRecurringPlanFee",
    "ExtraRecurringPricing",
    "Feature",
    "FeatureId",
    "FeatureListResponse",
    "FeatureRef",
    "FeatureStatus",
    "FeatureStatusLiteral",
    "FeatureType",
    "Fee",
    "FeeCreditUnit",
    "FixedDiscount",
    "FixedWindowResetPeriod",
    "GetCheckoutSessionResponse",
    "GroupedUsage",
    "IngestEventsRequest",
    "IngestEventsResponse",
    "IngestFailure",
    "IntrospectionRequest",
    "Invoice",
    "InvoiceCustomPropertiesRequest",
    "InvoiceDocumentsEvent",
    "InvoiceDocumentsEventData",
    "InvoiceEvent",
    "InvoiceEventData",
    "InvoiceId",
    "InvoiceLineCreditUnit",
    "InvoiceLineItem",
    "InvoiceListResponse",
    "InvoicePaymentStatus",
    "InvoicePaymentStatusLiteral",
    "InvoiceStatus",
    "InvoiceStatusLiteral",
    "InvoiceType",
    "InvoiceTypeLiteral",
    "InvoicingEntityId",
    "IssueLicenseRequest",
    "IssueLicenseResponse",
    "IssueOfflineLicenseRequest",
    "JsonConfigValue",
    "LedgerEntry",
    "LedgerEntryId",
    "LedgerEntryType",
    "LedgerEntryTypeLiteral",
    "LedgerListResponse",
    "License",
    "LicenseActivationCode",
    "LicenseId",
    "LicenseListResponse",
    "LicenseSigningKey",
    "LicenseSigningKeyStatus",
    "LicenseSigningKeyStatusLiteral",
    "LicenseSigningKeysResponse",
    "LicenseStatus",
    "LicenseStatusLiteral",
    "LicensingEndpoints",
    "LinkedSegmentationMatrix",
    "ListCheckoutSessionsResponse",
    "ListCustomerUsageCostsGranularity",
    "ListCustomerUsageCostsGranularityLiteral",
    "ListSubscriptionUsageCostsGranularity",
    "ListSubscriptionUsageCostsGranularityLiteral",
    "MatrixDimension",
    "MatrixPlanPricing",
    "MatrixPricing",
    "MatrixRow",
    "MeteredEffectiveEntitlementValue",
    "MeteredEntitlementSpec",
    "MeteredEntitlementUsage",
    "MeteredEntitlementValue",
    "MeteredFeatureType",
    "MeteredResolvedEntitlementValue",
    "Metric",
    "MetricDimension",
    "MetricEvent",
    "MetricEventData",
    "MetricFilter",
    "MetricFilterOperator",
    "MetricFilterOperatorLiteral",
    "MetricListResponse",
    "MetricSegmentationMatrix",
    "MetricSummary",
    "MetricUsage",
    "MinimumCommitment",
    "MinimumCommitmentInput",
    "MinimumCommitmentInputScope",
    "MinimumCommitmentScope",
    "NeverResetPeriod",
    "NewProductRef",
    "NumberConfigValue",
    "OAuthApp",
    "OAuthAppId",
    "OAuthAppWithSecret",
    "OAuthAppsResponse",
    "OAuthErrorCode",
    "OAuthErrorCodeLiteral",
    "OAuthErrorResponse",
    "OfflineLicense",
    "OnboardingLinkResponse",
    "OnboardingMode",
    "OnboardingModeLiteral",
    "OneTimeFee",
    "OneTimeFeeStructure",
    "OneTimePlanFee",
    "OneTimePricing",
    "OnlineMethodConfig",
    "OnlineMethodsConfig",
    "OnlinePaymentMethodConfig",
    "OrganizationId",
    "PackagePlanPricing",
    "PackagePricing",
    "PaginationResponse",
    "PatchBudgetRequest",
    "PatchPlanRequest",
    "PatchWalletRequest",
    "PaymentEvent",
    "PaymentMethodInfo",
    "PaymentMethodTypeEnum",
    "PaymentMethodTypeEnumLiteral",
    "PaymentMethodsConfig",
    "PaymentStatusEnum",
    "PaymentStatusEnumLiteral",
    "PaymentTransactionId",
    "PaymentTypeEnum",
    "PaymentTypeEnumLiteral",
    "PerUnitPlanPricing",
    "PerUnitPricing",
    "PercentageDiscount",
    "Plan",
    "PlanAddOnInput",
    "PlanEvent",
    "PlanEventData",
    "PlanFeeCreditUnit",
    "PlanId",
    "PlanListResponse",
    "PlanStatusEnum",
    "PlanStatusEnumLiteral",
    "PlanTypeEnum",
    "PlanTypeEnumLiteral",
    "PlanUsagePricingModel",
    "PlanVersionId",
    "PlanVersionListResponse",
    "PlanVersionSummary",
    "PriceComponent",
    "PriceComponentId",
    "PriceComponentInput",
    "PriceEntry",
    "PriceId",
    "PriceInput",
    "Pricing",
    "Product",
    "ProductEvent",
    "ProductEventData",
    "ProductFamily",
    "ProductFamilyCreateRequest",
    "ProductFamilyId",
    "ProductFamilyListResponse",
    "ProductFeeStructure",
    "ProductFeeTypeEnum",
    "ProductFeeTypeEnumLiteral",
    "ProductId",
    "ProductListResponse",
    "ProductRef",
    "ProductsScope",
    "PropertyConfig",
    "QuoteEvent",
    "QuoteEventData",
    "QuoteId",
    "RateFee",
    "RateFeeStructure",
    "RatePlanFee",
    "RatePricing",
    "RecurringFee",
    "RefundEventData",
    "RefundMode",
    "RefundModeLiteral",
    "ReplacePlanRequest",
    "ResetPeriod",
    "ResolvedEntitlement",
    "ResolvedEntitlementListResponse",
    "ResolvedEntitlementValue",
    "RestErrorResponse",
    "ReversalKind",
    "ReversalKindLiteral",
    "RevocationRequest",
    "RevokeLicenseRequest",
    "RotatedSecret",
    "SelectOption",
    "ShippingAddress",
    "SlidingWindowResetPeriod",
    "SlotDowngradePolicyEnum",
    "SlotDowngradePolicyEnumLiteral",
    "SlotFee",
    "SlotFeeStructure",
    "SlotPlanFee",
    "SlotPricing",
    "SlotUpgradePolicyEnum",
    "SlotUpgradePolicyEnumLiteral",
    "SubLineItem",
    "Subscription",
    "SubscriptionActivationConditionEnum",
    "SubscriptionActivationConditionEnumLiteral",
    "SubscriptionAddOn",
    "SubscriptionAddOnCustomization",
    "SubscriptionAddOnId",
    "SubscriptionAddOnParameterization",
    "SubscriptionAddOnPriceOverride",
    "SubscriptionComponent",
    "SubscriptionCoupon",
    "SubscriptionCreateRequest",
    "SubscriptionCredit",
    "SubscriptionDetails",
    "SubscriptionEvent",
    "SubscriptionEventData",
    "SubscriptionFee",
    "SubscriptionFeeBillingPeriodEnum",
    "SubscriptionFeeBillingPeriodEnumLiteral",
    "SubscriptionId",
    "SubscriptionListResponse",
    "SubscriptionStatusEnum",
    "SubscriptionStatusEnumLiteral",
    "SubscriptionUpdateRequest",
    "SubscriptionUpdateResponse",
    "SubscriptionUpdateType",
    "SubscriptionUpdateTypeLiteral",
    "TaxBreakdownItem",
    "TaxExemptionType",
    "TaxExemptionTypeLiteral",
    "TenantId",
    "TermRate",
    "TextConfigValue",
    "TierRow",
    "TieredPlanPricing",
    "TieredPricing",
    "TokenIntrospectionResponse",
    "TokenRequest",
    "TokenResponse",
    "TopUpCollection",
    "TopUpCollectionLiteral",
    "TopUpResponse",
    "TopUpStatus",
    "TopUpStatusLiteral",
    "Transaction",
    "TrialConfig",
    "UnattributedMetricUsage",
    "UnattributedUsageResponse",
    "UnitConversion",
    "UnitConversionRoundingEnum",
    "UnitConversionRoundingEnumLiteral",
    "UpdateAddOnRequest",
    "UpdateCouponRequest",
    "UpdateEntitlementRequest",
    "UpdateFeatureRequest",
    "UpdateMetricRequest",
    "UpdateProductRequest",
    "UpdateWebhookEndpointRequest",
    "UsageAtZero",
    "UsageAtZeroLiteral",
    "UsageCost",
    "UsageCostListResponse",
    "UsageCostRow",
    "UsageCostUnit",
    "UsageCostUnitLiteral",
    "UsageEvent",
    "UsageEventListResponse",
    "UsageFee",
    "UsageFeeStructure",
    "UsageFilter",
    "UsageLimitId",
    "UsageModelEnum",
    "UsageModelEnumLiteral",
    "UsagePlanFee",
    "UsagePricing",
    "UsagePricingModel",
    "UsageResponse",
    "VolumePlanPricing",
    "VolumePricing",
    "Wallet",
    "WalletBalanceLowEvent",
    "WalletBalanceLowEventData",
    "WalletCheck",
    "WalletCreditRecoveredEvent",
    "WalletCreditRecoveredEventData",
    "WalletCreditUnrecoveredEvent",
    "WalletCreditUnrecoveredEventData",
    "WalletDebitedEvent",
    "WalletDebitedEventData",
    "WalletDepletedEvent",
    "WalletDepletedEventData",
    "WalletFundedEvent",
    "WalletFundedEventData",
    "WalletListResponse",
    "WalletRecoveredEvent",
    "WalletRecoveredEventData",
    "WebhookDelivery",
    "WebhookDeliveryId",
    "WebhookDeliveryListResponse",
    "WebhookDeliveryStatus",
    "WebhookDeliveryStatusLiteral",
    "WebhookEndpoint",
    "WebhookEndpointDisabledReason",
    "WebhookEndpointDisabledReasonLiteral",
    "WebhookEndpointId",
    "WebhookEndpointListResponse",
    "WebhookEndpointSecret",
    "WebhookHeader",
    "WebhookHeaderInput",
]
