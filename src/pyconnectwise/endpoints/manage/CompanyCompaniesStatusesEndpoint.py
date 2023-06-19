from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyCompaniesStatusesIdEndpoint import CompanyCompaniesStatusesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesStatusesCountEndpoint import CompanyCompaniesStatusesCountEndpoint
from pyconnectwise.models.manage.CompanyStatusModel import CompanyStatusModel

class CompanyCompaniesStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesStatusesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyCompaniesStatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesStatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesStatusesIdEndpoint: The initialized CompanyCompaniesStatusesIdEndpoint object.
        """
        child = CompanyCompaniesStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CompanyStatusModel]:
        """
        Performs a GET request against the /company/companies/statuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyStatusModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CompanyStatusModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CompanyStatusModel]:
        """
        Performs a GET request against the /company/companies/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyStatusModel]: The parsed response data.
        """
        return self._parse_many(CompanyStatusModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyStatusModel:
        """
        Performs a POST request against the /company/companies/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyStatusModel: The parsed response data.
        """
        return self._parse_one(CompanyStatusModel, super().make_request("POST", params=params).json())
        