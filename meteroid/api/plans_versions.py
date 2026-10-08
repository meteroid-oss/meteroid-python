# this file is @generated
"""Plans versions API."""

from __future__ import annotations

import typing as t

from .. import models as _models
from ..models import (
    MinimumCommitment,
    MinimumCommitmentScope,
    PlanVersionListResponse,
    PlanVersionSummary,
)
from ..serialization import UNSET, Unset, to_json_value
from ._pages import (
    AsyncPlansVersionsListPage,
    PlansVersionsListPage,
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


class AsyncPlansVersions(ApiBaseAsync):
    """Plans versions API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncPlansVersionsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncPlansVersionsWithRawResponse(self)

    async def update_minimum(
        self,
        plan_version_id: str,
        *,
        amount: str,
        scope: MinimumCommitmentScope,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> MinimumCommitment:
        """Set or replace the plan-level minimum commitment for a draft plan version.

        :param amount: Decimal string in the plan currency, e.g. "100.00"."""
        response = await self._request(
            ApiRequest(
                method="put",
                path="/api/v1/plans/versions/{plan_version_id}/minimum",
                path_params={
                    "plan_version_id": plan_version_id,
                },
                json_body=to_json_value(
                    MinimumCommitment(
                        amount=amount,
                        scope=scope,
                    ),
                    MinimumCommitment,
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
        return decode_response(response, MinimumCommitment)

    async def delete_minimum(
        self,
        plan_version_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Remove the plan-level minimum commitment for a draft plan version."""
        await self._request(
            ApiRequest(
                method="delete",
                path="/api/v1/plans/versions/{plan_version_id}/minimum",
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

    def list(
        self,
        plan_id: str,
        *,
        page: int | None = None,
        per_page: int | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> AsyncPaginator[PlanVersionSummary, AsyncPlansVersionsListPage]:
        """List plan versions

        :param page: Page number (0-indexed)
        :param per_page: Number of items per page"""

        async def fetch(page_param: int | None) -> PlanVersionListResponse:
            response = await self._request(
                ApiRequest(
                    method="get",
                    path="/api/v1/plans/{plan_id}/versions",
                    path_params={
                        "plan_id": plan_id,
                    },
                    query_params=serialize_query_params(
                        {
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
            return decode_response(response, PlanVersionListResponse)

        paging = PagePaging[PlanVersionListResponse, PlanVersionSummary](
            items=lambda body: body.data,
            total_pages=lambda body: step(
                body.pagination_meta, lambda v: v.total_pages
            ),
            first_page=0,
        )
        return AsyncPaginator(
            lambda: AsyncPlansVersionsListPage._first(fetch, page, paging)
        )


class AsyncPlansVersionsWithRawResponse:
    """The methods of :class:`AsyncPlansVersions`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncPlansVersions) -> None:
        self.update_minimum = async_to_raw_response_wrapper(resource.update_minimum)
        self.delete_minimum = async_to_raw_response_wrapper(resource.delete_minimum)
        self.list = async_to_raw_response_wrapper(resource.list)


class PlansVersions(ApiBaseSync):
    """Plans versions API."""

    @property
    def with_raw_response(self) -> PlansVersionsWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return PlansVersionsWithRawResponse(self)

    def update_minimum(
        self,
        plan_version_id: str,
        *,
        amount: str,
        scope: MinimumCommitmentScope,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> MinimumCommitment:
        """Set or replace the plan-level minimum commitment for a draft plan version.

        :param amount: Decimal string in the plan currency, e.g. "100.00"."""
        response = self._request(
            ApiRequest(
                method="put",
                path="/api/v1/plans/versions/{plan_version_id}/minimum",
                path_params={
                    "plan_version_id": plan_version_id,
                },
                json_body=to_json_value(
                    MinimumCommitment(
                        amount=amount,
                        scope=scope,
                    ),
                    MinimumCommitment,
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
        return decode_response(response, MinimumCommitment)

    def delete_minimum(
        self,
        plan_version_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Remove the plan-level minimum commitment for a draft plan version."""
        self._request(
            ApiRequest(
                method="delete",
                path="/api/v1/plans/versions/{plan_version_id}/minimum",
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

    def list(
        self,
        plan_id: str,
        *,
        page: int | None = None,
        per_page: int | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> PlansVersionsListPage:
        """List plan versions

        :param page: Page number (0-indexed)
        :param per_page: Number of items per page"""

        def fetch(page_param: int | None) -> PlanVersionListResponse:
            response = self._request(
                ApiRequest(
                    method="get",
                    path="/api/v1/plans/{plan_id}/versions",
                    path_params={
                        "plan_id": plan_id,
                    },
                    query_params=serialize_query_params(
                        {
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
            return decode_response(response, PlanVersionListResponse)

        paging = PagePaging[PlanVersionListResponse, PlanVersionSummary](
            items=lambda body: body.data,
            total_pages=lambda body: step(
                body.pagination_meta, lambda v: v.total_pages
            ),
            first_page=0,
        )
        return PlansVersionsListPage._first(fetch, page, paging)


class PlansVersionsWithRawResponse:
    """The methods of :class:`PlansVersions`, returning an :class:`APIResponse`."""

    def __init__(self, resource: PlansVersions) -> None:
        self.update_minimum = to_raw_response_wrapper(resource.update_minimum)
        self.delete_minimum = to_raw_response_wrapper(resource.delete_minimum)
        self.list = to_raw_response_wrapper(resource.list)
