# this file is @generated
"""Plans API."""

from __future__ import annotations

import builtins
import functools
import typing as t

from .. import models as _models
from ..models import (
    BillingConfig,
    CreateEntitlementsRequest,
    CreatePlanRequest,
    EntitlementListResponse,
    EntitlementSpecRequest,
    MinimumCommitmentInput,
    PatchPlanRequest,
    Plan,
    PlanAddOnInput,
    PlanListResponse,
    PlanStatusEnum,
    PlanStatusEnumLiteral,
    PlanTypeEnum,
    PlanTypeEnumLiteral,
    PriceComponentInput,
    ProductFamilyId,
    ReplacePlanRequest,
    ResolvedEntitlementListResponse,
    TrialConfig,
)
from ..serialization import UNSET, Unset, to_json_value
from ._pages import (
    AsyncPlansListPage,
    PlansListPage,
)
from ._pagination import (
    AsyncPaginator,
    PagePaging,
    step,
)
from ._response import async_to_raw_response_wrapper, to_raw_response_wrapper
from .common import (
    ApiBaseAsync,
    ApiBaseSync,
    ApiRequest,
    Timeout,
    decode_response,
    serialize_query_params,
)
from .plans_versions import (
    AsyncPlansVersions,
    AsyncPlansVersionsWithRawResponse,
    PlansVersions,
    PlansVersionsWithRawResponse,
)


class AsyncPlans(ApiBaseAsync):
    """Plans API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncPlansWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncPlansWithRawResponse(self)

    @functools.cached_property
    def versions(self) -> AsyncPlansVersions:
        """The versions API."""
        return AsyncPlansVersions(self._cfg, self._httpx_client)

    async def list_plan_version_entitlements(
        self,
        plan_version_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> ResolvedEntitlementListResponse:
        """List plan version entitlements"""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/plan-versions/{plan_version_id}/entitlements",
                path_params={
                    "plan_version_id": plan_version_id,
                },
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
        return decode_response(response, ResolvedEntitlementListResponse)

    async def create_plan_version_entitlement(
        self,
        plan_version_id: str,
        *,
        entitlements: builtins.list[EntitlementSpecRequest],
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> EntitlementListResponse:
        """Create plan version entitlements

        Entitlements already present on this plan version are skipped."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/plan-versions/{plan_version_id}/entitlements",
                path_params={
                    "plan_version_id": plan_version_id,
                },
                json_body=to_json_value(
                    CreateEntitlementsRequest(
                        entitlements=entitlements,
                    ),
                    CreateEntitlementsRequest,
                ),
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
        return decode_response(response, EntitlementListResponse)

    def list(
        self,
        *,
        product_family_id: ProductFamilyId | None = None,
        search: str | None = None,
        status: builtins.list[PlanStatusEnum] | None = None,
        plan_type: builtins.list[PlanTypeEnum] | None = None,
        order_by: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> AsyncPaginator[Plan, AsyncPlansListPage]:
        """List plans

        :param search: Search by plan name
        :param status: Filter by plan status (can be repeated)
        :param plan_type: Filter by plan type (can be repeated)
        :param order_by: Sort order. Format: `column.direction`. Allowed columns: `name`, `status`, `plan_type`, `created_at`. Direction: `asc` or `desc`. Default: `created_at.desc`.
        :param page: Page number (0-indexed)
        :param per_page: Number of items per page"""

        async def fetch(page_param: int | None) -> PlanListResponse:
            response = await self._request(
                ApiRequest(
                    method="get",
                    path="/api/v1/plans",
                    query_params=serialize_query_params(
                        {
                            "product_family_id": product_family_id,
                            "search": search,
                            "status": status,
                            "plan_type": plan_type,
                            "order_by": order_by,
                            "page": page_param,
                            "per_page": per_page,
                        },
                    ),
                    error_types={
                        "default": _models.RestErrorResponse,
                    },
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    max_retries=max_retries,
                )
            )
            return decode_response(response, PlanListResponse)

        paging = PagePaging[PlanListResponse, Plan](
            items=lambda body: body.data,
            total_pages=lambda body: step(
                body.pagination_meta, lambda v: v.total_pages
            ),
            first_page=0,
        )
        return AsyncPaginator(lambda: AsyncPlansListPage._first(fetch, page, paging))

    async def create(
        self,
        *,
        components: builtins.list[PriceComponentInput],
        currency: str,
        name: str,
        plan_type: PlanTypeEnum | PlanTypeEnumLiteral,
        product_family_id: ProductFamilyId,
        status: PlanStatusEnum | PlanStatusEnumLiteral,
        add_ons: builtins.list[PlanAddOnInput] | None = None,
        billing: BillingConfig | None | Unset = UNSET,
        description: str | None | Unset = UNSET,
        entitlements: builtins.list[EntitlementSpecRequest] | None = None,
        self_service_rank: int | None | Unset = UNSET,
        tax_inclusive: bool | None = None,
        trial: TrialConfig | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Plan:
        """Create a plan

        Create a new plan with components and pricing. Set `status` to `ACTIVE` to
        publish immediately, or `DRAFT` to stage for review.

        :param entitlements: Entitlements to attach to this plan's version. Replacing a published plan creates a new version, and entitlements belong to a version, so passing them here keeps them attached to whichever version the call produces.
        :param tax_inclusive: The plan's amounts are quoted tax-included ("9.99 incl. VAT"): tax is carved out of them at invoice time instead of being added on top, so the customer pays the quoted price whatever rate applies. A customer who bears no tax (reverse charge, exempt, export) still pays it in full. Defaults to `false`."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/plans",
                json_body=to_json_value(
                    CreatePlanRequest(
                        add_ons=add_ons,
                        billing=billing,
                        components=components,
                        currency=currency,
                        description=description,
                        entitlements=entitlements,
                        name=name,
                        plan_type=t.cast("PlanTypeEnum", plan_type),
                        product_family_id=product_family_id,
                        self_service_rank=self_service_rank,
                        status=t.cast("PlanStatusEnum", status),
                        tax_inclusive=tax_inclusive,
                        trial=trial,
                    ),
                    CreatePlanRequest,
                ),
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
        return decode_response(response, Plan)

    async def retrieve(
        self,
        plan_id: str,
        *,
        version: str | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Plan:
        """Get plan details

        Retrieve a specific plan. Use `?version=draft` for the draft version,
        `?version=2` for a specific version number, or omit for the active version.

        :param version: Filter by version: "draft", a version number, or omitted for active"""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/plans/{plan_id}",
                path_params={
                    "plan_id": plan_id,
                },
                query_params=serialize_query_params(
                    {
                        "version": version,
                    },
                ),
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
        return decode_response(response, Plan)

    async def replace(
        self,
        plan_id: str,
        *,
        components: builtins.list[PriceComponentInput],
        currency: str,
        name: str,
        add_ons: builtins.list[PlanAddOnInput] | None = None,
        billing: BillingConfig | None | Unset = UNSET,
        description: str | None | Unset = UNSET,
        entitlements: builtins.list[EntitlementSpecRequest] | None = None,
        minimum_commitment: MinimumCommitmentInput | None | Unset = UNSET,
        status: PlanStatusEnum | PlanStatusEnumLiteral | None | Unset = UNSET,
        tax_inclusive: bool | None = None,
        trial: TrialConfig | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Plan:
        """Replace a plan

        Full replacement of a plan's version. On a draft plan, updates in-place.
        On a published plan, creates a new version. Set `status` to `DRAFT` to
        stage as a new draft without publishing.

        :param entitlements: Entitlements to attach to this plan's version. Replacing a published plan creates a new version, and entitlements belong to a version, so passing them here keeps them attached to whichever version the call produces.
        :param tax_inclusive: The plan's amounts are quoted tax-included ("9.99 incl. VAT"): tax is carved out of them at invoice time instead of being added on top, so the customer pays the quoted price whatever rate applies. A customer who bears no tax (reverse charge, exempt, export) still pays it in full. Defaults to `false`."""
        response = await self._request(
            ApiRequest(
                method="put",
                path="/api/v1/plans/{plan_id}",
                path_params={
                    "plan_id": plan_id,
                },
                json_body=to_json_value(
                    ReplacePlanRequest(
                        add_ons=add_ons,
                        billing=billing,
                        components=components,
                        currency=currency,
                        description=description,
                        entitlements=entitlements,
                        minimum_commitment=minimum_commitment,
                        name=name,
                        status=t.cast("PlanStatusEnum | None | Unset", status),
                        tax_inclusive=tax_inclusive,
                        trial=trial,
                    ),
                    ReplacePlanRequest,
                ),
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
        return decode_response(response, Plan)

    async def update(
        self,
        plan_id: str,
        *,
        description: str | None | Unset = UNSET,
        name: str | None | Unset = UNSET,
        self_service_rank: int | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Plan:
        """Update plan metadata

        Partially update plan-level fields (name, description, self_service_rank).
        Does not modify version-level configuration or components."""
        response = await self._request(
            ApiRequest(
                method="patch",
                path="/api/v1/plans/{plan_id}",
                path_params={
                    "plan_id": plan_id,
                },
                json_body=to_json_value(
                    PatchPlanRequest(
                        description=description,
                        name=name,
                        self_service_rank=self_service_rank,
                    ),
                    PatchPlanRequest,
                ),
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
        return decode_response(response, Plan)

    async def archive(
        self,
        plan_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Archive a plan"""
        await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/plans/{plan_id}/archive",
                path_params={
                    "plan_id": plan_id,
                },
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )

    async def publish(
        self,
        plan_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Plan:
        """Publish a draft plan version

        Publishes the current draft version, making it the active version."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/plans/{plan_id}/publish",
                path_params={
                    "plan_id": plan_id,
                },
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
        return decode_response(response, Plan)

    async def unarchive(
        self,
        plan_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Unarchive a plan"""
        await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/plans/{plan_id}/unarchive",
                path_params={
                    "plan_id": plan_id,
                },
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )


class AsyncPlansWithRawResponse:
    """The methods of :class:`AsyncPlans`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncPlans) -> None:
        self._resource = resource
        self.list_plan_version_entitlements = async_to_raw_response_wrapper(
            resource.list_plan_version_entitlements
        )
        self.create_plan_version_entitlement = async_to_raw_response_wrapper(
            resource.create_plan_version_entitlement
        )
        self.list = async_to_raw_response_wrapper(resource.list)
        self.create = async_to_raw_response_wrapper(resource.create)
        self.retrieve = async_to_raw_response_wrapper(resource.retrieve)
        self.replace = async_to_raw_response_wrapper(resource.replace)
        self.update = async_to_raw_response_wrapper(resource.update)
        self.archive = async_to_raw_response_wrapper(resource.archive)
        self.publish = async_to_raw_response_wrapper(resource.publish)
        self.unarchive = async_to_raw_response_wrapper(resource.unarchive)

    @property
    def versions(self) -> AsyncPlansVersionsWithRawResponse:
        """The versions API."""
        return AsyncPlansVersionsWithRawResponse(self._resource.versions)


class Plans(ApiBaseSync):
    """Plans API."""

    @property
    def with_raw_response(self) -> PlansWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return PlansWithRawResponse(self)

    @functools.cached_property
    def versions(self) -> PlansVersions:
        """The versions API."""
        return PlansVersions(self._cfg, self._httpx_client)

    def list_plan_version_entitlements(
        self,
        plan_version_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> ResolvedEntitlementListResponse:
        """List plan version entitlements"""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/plan-versions/{plan_version_id}/entitlements",
                path_params={
                    "plan_version_id": plan_version_id,
                },
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
        return decode_response(response, ResolvedEntitlementListResponse)

    def create_plan_version_entitlement(
        self,
        plan_version_id: str,
        *,
        entitlements: builtins.list[EntitlementSpecRequest],
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> EntitlementListResponse:
        """Create plan version entitlements

        Entitlements already present on this plan version are skipped."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/plan-versions/{plan_version_id}/entitlements",
                path_params={
                    "plan_version_id": plan_version_id,
                },
                json_body=to_json_value(
                    CreateEntitlementsRequest(
                        entitlements=entitlements,
                    ),
                    CreateEntitlementsRequest,
                ),
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
        return decode_response(response, EntitlementListResponse)

    def list(
        self,
        *,
        product_family_id: ProductFamilyId | None = None,
        search: str | None = None,
        status: builtins.list[PlanStatusEnum] | None = None,
        plan_type: builtins.list[PlanTypeEnum] | None = None,
        order_by: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> PlansListPage:
        """List plans

        :param search: Search by plan name
        :param status: Filter by plan status (can be repeated)
        :param plan_type: Filter by plan type (can be repeated)
        :param order_by: Sort order. Format: `column.direction`. Allowed columns: `name`, `status`, `plan_type`, `created_at`. Direction: `asc` or `desc`. Default: `created_at.desc`.
        :param page: Page number (0-indexed)
        :param per_page: Number of items per page"""

        def fetch(page_param: int | None) -> PlanListResponse:
            response = self._request(
                ApiRequest(
                    method="get",
                    path="/api/v1/plans",
                    query_params=serialize_query_params(
                        {
                            "product_family_id": product_family_id,
                            "search": search,
                            "status": status,
                            "plan_type": plan_type,
                            "order_by": order_by,
                            "page": page_param,
                            "per_page": per_page,
                        },
                    ),
                    error_types={
                        "default": _models.RestErrorResponse,
                    },
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    max_retries=max_retries,
                )
            )
            return decode_response(response, PlanListResponse)

        paging = PagePaging[PlanListResponse, Plan](
            items=lambda body: body.data,
            total_pages=lambda body: step(
                body.pagination_meta, lambda v: v.total_pages
            ),
            first_page=0,
        )
        return PlansListPage._first(fetch, page, paging)

    def create(
        self,
        *,
        components: builtins.list[PriceComponentInput],
        currency: str,
        name: str,
        plan_type: PlanTypeEnum | PlanTypeEnumLiteral,
        product_family_id: ProductFamilyId,
        status: PlanStatusEnum | PlanStatusEnumLiteral,
        add_ons: builtins.list[PlanAddOnInput] | None = None,
        billing: BillingConfig | None | Unset = UNSET,
        description: str | None | Unset = UNSET,
        entitlements: builtins.list[EntitlementSpecRequest] | None = None,
        self_service_rank: int | None | Unset = UNSET,
        tax_inclusive: bool | None = None,
        trial: TrialConfig | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Plan:
        """Create a plan

        Create a new plan with components and pricing. Set `status` to `ACTIVE` to
        publish immediately, or `DRAFT` to stage for review.

        :param entitlements: Entitlements to attach to this plan's version. Replacing a published plan creates a new version, and entitlements belong to a version, so passing them here keeps them attached to whichever version the call produces.
        :param tax_inclusive: The plan's amounts are quoted tax-included ("9.99 incl. VAT"): tax is carved out of them at invoice time instead of being added on top, so the customer pays the quoted price whatever rate applies. A customer who bears no tax (reverse charge, exempt, export) still pays it in full. Defaults to `false`."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/plans",
                json_body=to_json_value(
                    CreatePlanRequest(
                        add_ons=add_ons,
                        billing=billing,
                        components=components,
                        currency=currency,
                        description=description,
                        entitlements=entitlements,
                        name=name,
                        plan_type=t.cast("PlanTypeEnum", plan_type),
                        product_family_id=product_family_id,
                        self_service_rank=self_service_rank,
                        status=t.cast("PlanStatusEnum", status),
                        tax_inclusive=tax_inclusive,
                        trial=trial,
                    ),
                    CreatePlanRequest,
                ),
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
        return decode_response(response, Plan)

    def retrieve(
        self,
        plan_id: str,
        *,
        version: str | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Plan:
        """Get plan details

        Retrieve a specific plan. Use `?version=draft` for the draft version,
        `?version=2` for a specific version number, or omit for the active version.

        :param version: Filter by version: "draft", a version number, or omitted for active"""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/plans/{plan_id}",
                path_params={
                    "plan_id": plan_id,
                },
                query_params=serialize_query_params(
                    {
                        "version": version,
                    },
                ),
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
        return decode_response(response, Plan)

    def replace(
        self,
        plan_id: str,
        *,
        components: builtins.list[PriceComponentInput],
        currency: str,
        name: str,
        add_ons: builtins.list[PlanAddOnInput] | None = None,
        billing: BillingConfig | None | Unset = UNSET,
        description: str | None | Unset = UNSET,
        entitlements: builtins.list[EntitlementSpecRequest] | None = None,
        minimum_commitment: MinimumCommitmentInput | None | Unset = UNSET,
        status: PlanStatusEnum | PlanStatusEnumLiteral | None | Unset = UNSET,
        tax_inclusive: bool | None = None,
        trial: TrialConfig | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Plan:
        """Replace a plan

        Full replacement of a plan's version. On a draft plan, updates in-place.
        On a published plan, creates a new version. Set `status` to `DRAFT` to
        stage as a new draft without publishing.

        :param entitlements: Entitlements to attach to this plan's version. Replacing a published plan creates a new version, and entitlements belong to a version, so passing them here keeps them attached to whichever version the call produces.
        :param tax_inclusive: The plan's amounts are quoted tax-included ("9.99 incl. VAT"): tax is carved out of them at invoice time instead of being added on top, so the customer pays the quoted price whatever rate applies. A customer who bears no tax (reverse charge, exempt, export) still pays it in full. Defaults to `false`."""
        response = self._request(
            ApiRequest(
                method="put",
                path="/api/v1/plans/{plan_id}",
                path_params={
                    "plan_id": plan_id,
                },
                json_body=to_json_value(
                    ReplacePlanRequest(
                        add_ons=add_ons,
                        billing=billing,
                        components=components,
                        currency=currency,
                        description=description,
                        entitlements=entitlements,
                        minimum_commitment=minimum_commitment,
                        name=name,
                        status=t.cast("PlanStatusEnum | None | Unset", status),
                        tax_inclusive=tax_inclusive,
                        trial=trial,
                    ),
                    ReplacePlanRequest,
                ),
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
        return decode_response(response, Plan)

    def update(
        self,
        plan_id: str,
        *,
        description: str | None | Unset = UNSET,
        name: str | None | Unset = UNSET,
        self_service_rank: int | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Plan:
        """Update plan metadata

        Partially update plan-level fields (name, description, self_service_rank).
        Does not modify version-level configuration or components."""
        response = self._request(
            ApiRequest(
                method="patch",
                path="/api/v1/plans/{plan_id}",
                path_params={
                    "plan_id": plan_id,
                },
                json_body=to_json_value(
                    PatchPlanRequest(
                        description=description,
                        name=name,
                        self_service_rank=self_service_rank,
                    ),
                    PatchPlanRequest,
                ),
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
        return decode_response(response, Plan)

    def archive(
        self,
        plan_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Archive a plan"""
        self._request(
            ApiRequest(
                method="post",
                path="/api/v1/plans/{plan_id}/archive",
                path_params={
                    "plan_id": plan_id,
                },
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )

    def publish(
        self,
        plan_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Plan:
        """Publish a draft plan version

        Publishes the current draft version, making it the active version."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/plans/{plan_id}/publish",
                path_params={
                    "plan_id": plan_id,
                },
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
        return decode_response(response, Plan)

    def unarchive(
        self,
        plan_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Unarchive a plan"""
        self._request(
            ApiRequest(
                method="post",
                path="/api/v1/plans/{plan_id}/unarchive",
                path_params={
                    "plan_id": plan_id,
                },
                error_types={
                    "default": _models.RestErrorResponse,
                },
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            )
        )


class PlansWithRawResponse:
    """The methods of :class:`Plans`, returning an :class:`APIResponse`."""

    def __init__(self, resource: Plans) -> None:
        self._resource = resource
        self.list_plan_version_entitlements = to_raw_response_wrapper(
            resource.list_plan_version_entitlements
        )
        self.create_plan_version_entitlement = to_raw_response_wrapper(
            resource.create_plan_version_entitlement
        )
        self.list = to_raw_response_wrapper(resource.list)
        self.create = to_raw_response_wrapper(resource.create)
        self.retrieve = to_raw_response_wrapper(resource.retrieve)
        self.replace = to_raw_response_wrapper(resource.replace)
        self.update = to_raw_response_wrapper(resource.update)
        self.archive = to_raw_response_wrapper(resource.archive)
        self.publish = to_raw_response_wrapper(resource.publish)
        self.unarchive = to_raw_response_wrapper(resource.unarchive)

    @property
    def versions(self) -> PlansVersionsWithRawResponse:
        """The versions API."""
        return PlansVersionsWithRawResponse(self._resource.versions)
