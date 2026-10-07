# this file is @generated
"""Features API."""

from __future__ import annotations

import builtins
import typing as t

from .. import models as _models
from ..models import (
    CreateFeatureRequest,
    EntitlementValue,
    Feature,
    FeatureListResponse,
    FeatureStatus,
    FeatureType,
    ProductId,
    UpdateFeatureRequest,
)
from ..serialization import UNSET, Unset, to_json_value
from ._pages import (
    AsyncFeaturesListPage,
    FeaturesListPage,
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


class AsyncFeatures(ApiBaseAsync):
    """Features API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncFeaturesWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncFeaturesWithRawResponse(self)

    def list(
        self,
        *,
        statuses: builtins.list[FeatureStatus] | None = None,
        product_id: ProductId | None = None,
        search: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> AsyncPaginator[Feature, AsyncFeaturesListPage]:
        """List features

        :param statuses: Filter by feature status. Repeat the param to select multiple, omit to return all.
        :param product_id: Filter by product. Omit to return features across all products.
        :param search: Search by feature name.
        :param page: Page number (0-indexed)
        :param per_page: Number of items per page"""

        async def fetch(page_param: int | None) -> FeatureListResponse:
            response = await self._request(
                ApiRequest(
                    method="get",
                    path="/api/v1/features",
                    query_params=serialize_query_params(
                        {
                            "statuses": statuses,
                            "product_id": product_id,
                            "search": search,
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
            return decode_response(response, FeatureListResponse)

        paging = PagePaging[FeatureListResponse, Feature](
            items=lambda body: body.data,
            total_pages=lambda body: step(
                body.pagination_meta, lambda v: v.total_pages
            ),
            first_page=0,
        )
        return AsyncPaginator(lambda: AsyncFeaturesListPage._first(fetch, page, paging))

    async def create(
        self,
        *,
        code: str,
        feature_type: FeatureType,
        name: str,
        description: str | None | Unset = UNSET,
        entitlement: EntitlementValue | None | Unset = UNSET,
        product_id: ProductId | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Feature:
        """Create a feature

        :param code: Unique key used to reference this feature in your code. Cannot be changed after creation.
        :param feature_type: Fixed at creation — a feature never changes type."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/features",
                json_body=to_json_value(
                    CreateFeatureRequest(
                        code=code,
                        description=description,
                        entitlement=entitlement,
                        feature_type=feature_type,
                        name=name,
                        product_id=product_id,
                    ),
                    CreateFeatureRequest,
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
        return decode_response(response, Feature)

    async def retrieve(
        self,
        id_or_code: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Feature:
        """Get feature details"""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/features/{id_or_code}",
                path_params={
                    "id_or_code": id_or_code,
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
        return decode_response(response, Feature)

    async def update(
        self,
        id_or_code: str,
        *,
        description: str | None | Unset = UNSET,
        name: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Feature:
        """Update a feature

        Partially update feature fields. Code, feature type and product are immutable.

        :param description: Omit to leave unchanged; send `null` to clear."""
        response = await self._request(
            ApiRequest(
                method="patch",
                path="/api/v1/features/{id_or_code}",
                path_params={
                    "id_or_code": id_or_code,
                },
                json_body=to_json_value(
                    UpdateFeatureRequest(
                        description=description,
                        name=name,
                    ),
                    UpdateFeatureRequest,
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
        return decode_response(response, Feature)

    async def archive(
        self,
        id_or_code: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Archive a feature

        Keeps the feature and its entitlements but hides them from resolution."""
        await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/features/{id_or_code}/archive",
                path_params={
                    "id_or_code": id_or_code,
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

    async def unarchive(
        self,
        id_or_code: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Unarchive a feature"""
        await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/features/{id_or_code}/unarchive",
                path_params={
                    "id_or_code": id_or_code,
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


class AsyncFeaturesWithRawResponse:
    """The methods of :class:`AsyncFeatures`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncFeatures) -> None:
        self.list = async_to_raw_response_wrapper(resource.list)
        self.create = async_to_raw_response_wrapper(resource.create)
        self.retrieve = async_to_raw_response_wrapper(resource.retrieve)
        self.update = async_to_raw_response_wrapper(resource.update)
        self.archive = async_to_raw_response_wrapper(resource.archive)
        self.unarchive = async_to_raw_response_wrapper(resource.unarchive)


class Features(ApiBaseSync):
    """Features API."""

    @property
    def with_raw_response(self) -> FeaturesWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return FeaturesWithRawResponse(self)

    def list(
        self,
        *,
        statuses: builtins.list[FeatureStatus] | None = None,
        product_id: ProductId | None = None,
        search: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> FeaturesListPage:
        """List features

        :param statuses: Filter by feature status. Repeat the param to select multiple, omit to return all.
        :param product_id: Filter by product. Omit to return features across all products.
        :param search: Search by feature name.
        :param page: Page number (0-indexed)
        :param per_page: Number of items per page"""

        def fetch(page_param: int | None) -> FeatureListResponse:
            response = self._request(
                ApiRequest(
                    method="get",
                    path="/api/v1/features",
                    query_params=serialize_query_params(
                        {
                            "statuses": statuses,
                            "product_id": product_id,
                            "search": search,
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
            return decode_response(response, FeatureListResponse)

        paging = PagePaging[FeatureListResponse, Feature](
            items=lambda body: body.data,
            total_pages=lambda body: step(
                body.pagination_meta, lambda v: v.total_pages
            ),
            first_page=0,
        )
        return FeaturesListPage._first(fetch, page, paging)

    def create(
        self,
        *,
        code: str,
        feature_type: FeatureType,
        name: str,
        description: str | None | Unset = UNSET,
        entitlement: EntitlementValue | None | Unset = UNSET,
        product_id: ProductId | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Feature:
        """Create a feature

        :param code: Unique key used to reference this feature in your code. Cannot be changed after creation.
        :param feature_type: Fixed at creation — a feature never changes type."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/features",
                json_body=to_json_value(
                    CreateFeatureRequest(
                        code=code,
                        description=description,
                        entitlement=entitlement,
                        feature_type=feature_type,
                        name=name,
                        product_id=product_id,
                    ),
                    CreateFeatureRequest,
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
        return decode_response(response, Feature)

    def retrieve(
        self,
        id_or_code: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Feature:
        """Get feature details"""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/features/{id_or_code}",
                path_params={
                    "id_or_code": id_or_code,
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
        return decode_response(response, Feature)

    def update(
        self,
        id_or_code: str,
        *,
        description: str | None | Unset = UNSET,
        name: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> Feature:
        """Update a feature

        Partially update feature fields. Code, feature type and product are immutable.

        :param description: Omit to leave unchanged; send `null` to clear."""
        response = self._request(
            ApiRequest(
                method="patch",
                path="/api/v1/features/{id_or_code}",
                path_params={
                    "id_or_code": id_or_code,
                },
                json_body=to_json_value(
                    UpdateFeatureRequest(
                        description=description,
                        name=name,
                    ),
                    UpdateFeatureRequest,
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
        return decode_response(response, Feature)

    def archive(
        self,
        id_or_code: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Archive a feature

        Keeps the feature and its entitlements but hides them from resolution."""
        self._request(
            ApiRequest(
                method="post",
                path="/api/v1/features/{id_or_code}/archive",
                path_params={
                    "id_or_code": id_or_code,
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

    def unarchive(
        self,
        id_or_code: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Unarchive a feature"""
        self._request(
            ApiRequest(
                method="post",
                path="/api/v1/features/{id_or_code}/unarchive",
                path_params={
                    "id_or_code": id_or_code,
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


class FeaturesWithRawResponse:
    """The methods of :class:`Features`, returning an :class:`APIResponse`."""

    def __init__(self, resource: Features) -> None:
        self.list = to_raw_response_wrapper(resource.list)
        self.create = to_raw_response_wrapper(resource.create)
        self.retrieve = to_raw_response_wrapper(resource.retrieve)
        self.update = to_raw_response_wrapper(resource.update)
        self.archive = to_raw_response_wrapper(resource.archive)
        self.unarchive = to_raw_response_wrapper(resource.unarchive)
