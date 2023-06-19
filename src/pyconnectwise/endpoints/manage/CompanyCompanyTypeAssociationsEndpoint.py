from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyCompanyTypeAssociationsIdEndpoint import CompanyCompanyTypeAssociationsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyCompanyTypeAssociationsCountEndpoint import CompanyCompanyTypeAssociationsCountEndpoint
from pyconnectwise.models.manage.CompanyTypeAssociationModel import CompanyTypeAssociationModel

class CompanyCompanyTypeAssociationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "companyTypeAssociations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompanyTypeAssociationsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyCompanyTypeAssociationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompanyTypeAssociationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompanyTypeAssociationsIdEndpoint: The initialized CompanyCompanyTypeAssociationsIdEndpoint object.
        """
        child = CompanyCompanyTypeAssociationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CompanyTypeAssociationModel]:
        """
        Performs a GET request against the /company/companyTypeAssociations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyTypeAssociationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CompanyTypeAssociationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CompanyTypeAssociationModel]:
        """
        Performs a GET request against the /company/companyTypeAssociations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyTypeAssociationModel]: The parsed response data.
        """
        return self._parse_many(CompanyTypeAssociationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyTypeAssociationModel:
        """
        Performs a POST request against the /company/companyTypeAssociations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyTypeAssociationModel: The parsed response data.
        """
        return self._parse_one(CompanyTypeAssociationModel, super().make_request("POST", params=params).json())
        