# this file is @generated
"""Connect API."""

from __future__ import annotations

import typing as t

from .. import models as _models
from ..models import (
    ConnectedAccount,
    ConnectedAccountsResponse,
    CountryCode,
    CreateConnectedAccountRequest,
    CreateConnectedAccountResponse,
    CreateOnboardingLinkRequest,
    OnboardingLinkResponse,
    OnboardingMode,
    OnboardingModeLiteral,
)
from ..serialization import UNSET, Unset, to_json_value
from ._response import async_to_raw_response_wrapper, to_raw_response_wrapper
from .common import (
    ApiBaseAsync,
    ApiBaseSync,
    ApiRequest,
    Timeout,
    decode_response,
)


class AsyncConnect(ApiBaseAsync):
    """Connect API, for asyncio."""

    @property
    def with_raw_response(self) -> AsyncConnectWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return AsyncConnectWithRawResponse(self)

    async def list_connected_accounts(
        self,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> ConnectedAccountsResponse:
        """List connected accounts

        List all connected accounts for this platform."""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/connected-accounts",
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
        return decode_response(response, ConnectedAccountsResponse)

    async def create_connected_account(
        self,
        *,
        email: str,
        organization_name: str,
        country: CountryCode | None | Unset = UNSET,
        metadata: t.Any = None,
        mode: OnboardingMode | OnboardingModeLiteral | None | Unset = UNSET,
        redirect_url: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreateConnectedAccountResponse:
        """Create connected account

        Create a new pending connected account (Express flow). Returns the
        account and an onboarding link for the user to complete setup."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/connected-accounts",
                json_body=to_json_value(
                    CreateConnectedAccountRequest(
                        country=country,
                        email=email,
                        metadata=metadata,
                        mode=t.cast("OnboardingMode | None | Unset", mode),
                        organization_name=organization_name,
                        redirect_url=redirect_url,
                    ),
                    CreateConnectedAccountRequest,
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
        return decode_response(response, CreateConnectedAccountResponse)

    async def retrieve_connected_account(
        self,
        id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> ConnectedAccount:
        """Get connected account

        Retrieve a connected account by ID."""
        response = await self._request(
            ApiRequest(
                method="get",
                path="/api/v1/connected-accounts/{id}",
                path_params={
                    "id": id,
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
        return decode_response(response, ConnectedAccount)

    async def disconnect_account(
        self,
        id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Disconnect account

        Revoke a connected account. All associated tokens are invalidated."""
        await self._request(
            ApiRequest(
                method="delete",
                path="/api/v1/connected-accounts/{id}",
                path_params={
                    "id": id,
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

    async def create_onboarding_link(
        self,
        id: str,
        *,
        redirect_url: str,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> OnboardingLinkResponse:
        """Create onboarding link

        Generate a new onboarding link for a connected account. Any existing
        unused link is invalidated. The link expires after a configured duration."""
        response = await self._request(
            ApiRequest(
                method="post",
                path="/api/v1/connected-accounts/{id}/onboarding",
                path_params={
                    "id": id,
                },
                json_body=to_json_value(
                    CreateOnboardingLinkRequest(
                        redirect_url=redirect_url,
                    ),
                    CreateOnboardingLinkRequest,
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
        return decode_response(response, OnboardingLinkResponse)


class AsyncConnectWithRawResponse:
    """The methods of :class:`AsyncConnect`, returning an :class:`APIResponse`."""

    def __init__(self, resource: AsyncConnect) -> None:
        self.list_connected_accounts = async_to_raw_response_wrapper(
            resource.list_connected_accounts
        )
        self.create_connected_account = async_to_raw_response_wrapper(
            resource.create_connected_account
        )
        self.retrieve_connected_account = async_to_raw_response_wrapper(
            resource.retrieve_connected_account
        )
        self.disconnect_account = async_to_raw_response_wrapper(
            resource.disconnect_account
        )
        self.create_onboarding_link = async_to_raw_response_wrapper(
            resource.create_onboarding_link
        )


class Connect(ApiBaseSync):
    """Connect API."""

    @property
    def with_raw_response(self) -> ConnectWithRawResponse:
        """These methods, returning an :class:`APIResponse` with the status and headers."""
        return ConnectWithRawResponse(self)

    def list_connected_accounts(
        self,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> ConnectedAccountsResponse:
        """List connected accounts

        List all connected accounts for this platform."""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/connected-accounts",
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
        return decode_response(response, ConnectedAccountsResponse)

    def create_connected_account(
        self,
        *,
        email: str,
        organization_name: str,
        country: CountryCode | None | Unset = UNSET,
        metadata: t.Any = None,
        mode: OnboardingMode | OnboardingModeLiteral | None | Unset = UNSET,
        redirect_url: str | None | Unset = UNSET,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> CreateConnectedAccountResponse:
        """Create connected account

        Create a new pending connected account (Express flow). Returns the
        account and an onboarding link for the user to complete setup."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/connected-accounts",
                json_body=to_json_value(
                    CreateConnectedAccountRequest(
                        country=country,
                        email=email,
                        metadata=metadata,
                        mode=t.cast("OnboardingMode | None | Unset", mode),
                        organization_name=organization_name,
                        redirect_url=redirect_url,
                    ),
                    CreateConnectedAccountRequest,
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
        return decode_response(response, CreateConnectedAccountResponse)

    def retrieve_connected_account(
        self,
        id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> ConnectedAccount:
        """Get connected account

        Retrieve a connected account by ID."""
        response = self._request(
            ApiRequest(
                method="get",
                path="/api/v1/connected-accounts/{id}",
                path_params={
                    "id": id,
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
        return decode_response(response, ConnectedAccount)

    def disconnect_account(
        self,
        id: str,
        *,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> None:
        """Disconnect account

        Revoke a connected account. All associated tokens are invalidated."""
        self._request(
            ApiRequest(
                method="delete",
                path="/api/v1/connected-accounts/{id}",
                path_params={
                    "id": id,
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

    def create_onboarding_link(
        self,
        id: str,
        *,
        redirect_url: str,
        extra_headers: t.Mapping[str, str] | None = None,
        extra_query: t.Mapping[str, object] | None = None,
        extra_body: t.Mapping[str, object] | None = None,
        timeout: Timeout | Unset = UNSET,
        max_retries: int | None = None,
    ) -> OnboardingLinkResponse:
        """Create onboarding link

        Generate a new onboarding link for a connected account. Any existing
        unused link is invalidated. The link expires after a configured duration."""
        response = self._request(
            ApiRequest(
                method="post",
                path="/api/v1/connected-accounts/{id}/onboarding",
                path_params={
                    "id": id,
                },
                json_body=to_json_value(
                    CreateOnboardingLinkRequest(
                        redirect_url=redirect_url,
                    ),
                    CreateOnboardingLinkRequest,
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
        return decode_response(response, OnboardingLinkResponse)


class ConnectWithRawResponse:
    """The methods of :class:`Connect`, returning an :class:`APIResponse`."""

    def __init__(self, resource: Connect) -> None:
        self.list_connected_accounts = to_raw_response_wrapper(
            resource.list_connected_accounts
        )
        self.create_connected_account = to_raw_response_wrapper(
            resource.create_connected_account
        )
        self.retrieve_connected_account = to_raw_response_wrapper(
            resource.retrieve_connected_account
        )
        self.disconnect_account = to_raw_response_wrapper(resource.disconnect_account)
        self.create_onboarding_link = to_raw_response_wrapper(
            resource.create_onboarding_link
        )
