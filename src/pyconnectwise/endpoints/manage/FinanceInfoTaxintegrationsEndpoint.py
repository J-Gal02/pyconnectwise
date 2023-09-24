from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceInfoTaxintegrationsCountEndpoint import \
    FinanceInfoTaxintegrationsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceInfoTaxintegrationsIdEndpoint import FinanceInfoTaxintegrationsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import TaxIntegrationInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceInfoTaxintegrationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TaxIntegrationInfo], ConnectWiseManageRequestParams],
    IPaginateable[TaxIntegrationInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxIntegrations", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceInfoTaxintegrationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceInfoTaxintegrationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceInfoTaxintegrationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceInfoTaxintegrationsIdEndpoint: The initialized FinanceInfoTaxintegrationsIdEndpoint object.
        """
        child = FinanceInfoTaxintegrationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[TaxIntegrationInfo]:
        """
        Performs a GET request against the /finance/info/taxIntegrations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxIntegrationInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), TaxIntegrationInfo, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[TaxIntegrationInfo]:
        """
        Performs a GET request against the /finance/info/taxIntegrations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxIntegrationInfo]: The parsed response data.
        """
        return self._parse_many(TaxIntegrationInfo, super()._make_request("GET", data=data, params=params).json())
