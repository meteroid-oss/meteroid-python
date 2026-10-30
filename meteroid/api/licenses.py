# this file is @generated
"""Licenses API."""

from __future__ import annotations

import typing as t

from .. import models as _models
from ..models import (
    IssueLicenseRequest,
    IssueLicenseResponse,
    IssueOfflineLicenseRequest,
    License,
    LicenseActivationCode,
    LicenseListResponse,
    LicenseSigningKeysResponse,
    OfflineLicense,
    RevokeLicenseRequest,
)
from ..serialization import UNSET, Unset, to_json_value
from ._response import async_to_raw_response_wrapper, to_raw_response_wrapper
from .common import (
    ApiBaseAsync,
    ApiBaseSync,
    ApiRequest,
    Timeout,
    decode_response,
    serialize_query_params,
)


class AsyncLicenses(ApiBaseAsync):
    """Licenses API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncLicensesWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncLicensesWithRawResponse(self)

    async def list(
        self,
        *,
        customer_id: str | None = None,
        subscription_id: str | None = None,
        include_revoked: bool | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> LicenseListResponse:
        """List licenses

        :param customer_id: Filter by customer ID or alias
        :param include_revoked: Include revoked licenses. Default: false."""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/licenses",
                query_params=serialize_query_params(
                    {
                        "customer_id": customer_id,
                        "subscription_id": subscription_id,
                        "include_revoked": include_revoked,
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
        return decode_response(response, LicenseListResponse)

    async def create(
        self,
        *,
        customer_id: str,
        instance_id: str | None | Unset = UNSET,
        offline: bool | None = None,
        subscription_id: str | None | Unset = UNSET,
        validity_days: int | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> IssueLicenseResponse:
        """Issue a license

        Issues a license to a customer, optionally tied to one of its subscriptions. Online, the
        license is pending until their installation activates it with the returned one-time code.
        Offline, it is returned signed at once, for an installation that can't reach the server.

        :param customer_id: Customer ID or alias
        :param instance_id: Offline only. The installation's id as it reports it, up to 255 characters without spaces: the license names it (`aud`) and stays bound to it. Without one, the license is not tied to an installation.
        :param offline: Delivers the license at once as a signed offline license, for an installation that can't reach the license server: no activation code, no refresh. Default: false.
        :param subscription_id: Ties the license to this subscription of the customer: it is renewed while the subscription is paid, and carries its plan's entitlements.
        :param validity_days: Online: lifetime of each license token the installation refreshes, 1 to 31 days. Default: 7. Offline: lifetime of the signed license, 1 to 400 days. Default: 365."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/licenses",
                json_body=to_json_value(
                    IssueLicenseRequest(
                        customer_id=customer_id,
                        instance_id=instance_id,
                        offline=offline,
                        subscription_id=subscription_id,
                        validity_days=validity_days,
                    ),
                    IssueLicenseRequest,
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
        return decode_response(response, IssueLicenseResponse)

    async def retrieve(
        self,
        license_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> License:
        """Get a license"""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/licenses/{license_id}",
                path_params={
                    "license_id": license_id,
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
        return decode_response(response, License)

    async def retrieve_activation_code(
        self,
        license_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> LicenseActivationCode:
        """Get a license's activation code

        Available until the license is activated or revoked."""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/licenses/{license_id}/activation-code",
                path_params={
                    "license_id": license_id,
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
        return decode_response(response, LicenseActivationCode)

    async def offline(
        self,
        license_id: str,
        *,
        valid_days: int,
        instance_id: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> OfflineLicense:
        """Issue an offline license

        Signs a long-lived license for an air-gapped installation from an existing license, e.g. to
        renew an offline license before it expires. Given an instance id, binds the license to it.

        :param instance_id: The installation's id as it reports it, up to 255 characters without spaces: the license names it (`aud`) and stays bound to it. Without one, the license is not tied to one.
        :param valid_days: Lifetime of the offline license, 1 to 400 days."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/licenses/{license_id}/offline",
                path_params={
                    "license_id": license_id,
                },
                json_body=to_json_value(
                    IssueOfflineLicenseRequest(
                        instance_id=instance_id,
                        valid_days=valid_days,
                    ),
                    IssueOfflineLicenseRequest,
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
        return decode_response(response, OfflineLicense)

    async def revoke(
        self,
        license_id: str,
        *,
        immediately: bool | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> License:
        """Revoke a license

        :param immediately: Stop at once: the installation drops its license on its next refresh. Otherwise the license keeps working until it expires, and is not renewed."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/licenses/{license_id}/revoke",
                path_params={
                    "license_id": license_id,
                },
                json_body=to_json_value(
                    RevokeLicenseRequest(
                        immediately=immediately,
                    ),
                    RevokeLicenseRequest,
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
        return decode_response(response, License)

    async def list_licensing_signing_keys(
        self,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> LicenseSigningKeysResponse:
        """Get the licensing signing keys

        The keys licenses are signed with, and the public endpoints installations talk to."""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/licensing/signing-keys",
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
        return decode_response(response, LicenseSigningKeysResponse)


class AsyncLicensesWithRawResponse:
    """The methods of :class:`AsyncLicenses`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncLicenses) -> None:
        self.list = async_to_raw_response_wrapper(resource.list)
        self.create = async_to_raw_response_wrapper(resource.create)
        self.retrieve = async_to_raw_response_wrapper(resource.retrieve)
        self.retrieve_activation_code = async_to_raw_response_wrapper(
            resource.retrieve_activation_code
        )
        self.offline = async_to_raw_response_wrapper(resource.offline)
        self.revoke = async_to_raw_response_wrapper(resource.revoke)
        self.list_licensing_signing_keys = async_to_raw_response_wrapper(
            resource.list_licensing_signing_keys
        )


class Licenses(ApiBaseSync):
    """Licenses API."""

    @property
    def with_raw_response(self) -> LicensesWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return LicensesWithRawResponse(self)

    def list(
        self,
        *,
        customer_id: str | None = None,
        subscription_id: str | None = None,
        include_revoked: bool | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> LicenseListResponse:
        """List licenses

        :param customer_id: Filter by customer ID or alias
        :param include_revoked: Include revoked licenses. Default: false."""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/licenses",
                query_params=serialize_query_params(
                    {
                        "customer_id": customer_id,
                        "subscription_id": subscription_id,
                        "include_revoked": include_revoked,
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
        return decode_response(response, LicenseListResponse)

    def create(
        self,
        *,
        customer_id: str,
        instance_id: str | None | Unset = UNSET,
        offline: bool | None = None,
        subscription_id: str | None | Unset = UNSET,
        validity_days: int | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> IssueLicenseResponse:
        """Issue a license

        Issues a license to a customer, optionally tied to one of its subscriptions. Online, the
        license is pending until their installation activates it with the returned one-time code.
        Offline, it is returned signed at once, for an installation that can't reach the server.

        :param customer_id: Customer ID or alias
        :param instance_id: Offline only. The installation's id as it reports it, up to 255 characters without spaces: the license names it (`aud`) and stays bound to it. Without one, the license is not tied to an installation.
        :param offline: Delivers the license at once as a signed offline license, for an installation that can't reach the license server: no activation code, no refresh. Default: false.
        :param subscription_id: Ties the license to this subscription of the customer: it is renewed while the subscription is paid, and carries its plan's entitlements.
        :param validity_days: Online: lifetime of each license token the installation refreshes, 1 to 31 days. Default: 7. Offline: lifetime of the signed license, 1 to 400 days. Default: 365."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/licenses",
                json_body=to_json_value(
                    IssueLicenseRequest(
                        customer_id=customer_id,
                        instance_id=instance_id,
                        offline=offline,
                        subscription_id=subscription_id,
                        validity_days=validity_days,
                    ),
                    IssueLicenseRequest,
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
        return decode_response(response, IssueLicenseResponse)

    def retrieve(
        self,
        license_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> License:
        """Get a license"""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/licenses/{license_id}",
                path_params={
                    "license_id": license_id,
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
        return decode_response(response, License)

    def retrieve_activation_code(
        self,
        license_id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> LicenseActivationCode:
        """Get a license's activation code

        Available until the license is activated or revoked."""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/licenses/{license_id}/activation-code",
                path_params={
                    "license_id": license_id,
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
        return decode_response(response, LicenseActivationCode)

    def offline(
        self,
        license_id: str,
        *,
        valid_days: int,
        instance_id: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> OfflineLicense:
        """Issue an offline license

        Signs a long-lived license for an air-gapped installation from an existing license, e.g. to
        renew an offline license before it expires. Given an instance id, binds the license to it.

        :param instance_id: The installation's id as it reports it, up to 255 characters without spaces: the license names it (`aud`) and stays bound to it. Without one, the license is not tied to one.
        :param valid_days: Lifetime of the offline license, 1 to 400 days."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/licenses/{license_id}/offline",
                path_params={
                    "license_id": license_id,
                },
                json_body=to_json_value(
                    IssueOfflineLicenseRequest(
                        instance_id=instance_id,
                        valid_days=valid_days,
                    ),
                    IssueOfflineLicenseRequest,
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
        return decode_response(response, OfflineLicense)

    def revoke(
        self,
        license_id: str,
        *,
        immediately: bool | None = None,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> License:
        """Revoke a license

        :param immediately: Stop at once: the installation drops its license on its next refresh. Otherwise the license keeps working until it expires, and is not renewed."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/licenses/{license_id}/revoke",
                path_params={
                    "license_id": license_id,
                },
                json_body=to_json_value(
                    RevokeLicenseRequest(
                        immediately=immediately,
                    ),
                    RevokeLicenseRequest,
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
        return decode_response(response, License)

    def list_licensing_signing_keys(
        self,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> LicenseSigningKeysResponse:
        """Get the licensing signing keys

        The keys licenses are signed with, and the public endpoints installations talk to."""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/licensing/signing-keys",
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
        return decode_response(response, LicenseSigningKeysResponse)


class LicensesWithRawResponse:
    """The methods of :class:`Licenses`, returning an :class:`APIResponse`."""

    def __init__(self, resource: Licenses) -> None:
        self.list = to_raw_response_wrapper(resource.list)
        self.create = to_raw_response_wrapper(resource.create)
        self.retrieve = to_raw_response_wrapper(resource.retrieve)
        self.retrieve_activation_code = to_raw_response_wrapper(
            resource.retrieve_activation_code
        )
        self.offline = to_raw_response_wrapper(resource.offline)
        self.revoke = to_raw_response_wrapper(resource.revoke)
        self.list_licensing_signing_keys = to_raw_response_wrapper(
            resource.list_licensing_signing_keys
        )
