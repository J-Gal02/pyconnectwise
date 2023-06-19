from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProjectProjectsIdEndpoint import ProjectProjectsIdEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsCountEndpoint import ProjectProjectsCountEndpoint
from pyconnectwise.models.manage.ProjectModel import ProjectModel

class ProjectProjectsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "projects", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectProjectsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProjectProjectsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectProjectsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectProjectsIdEndpoint: The initialized ProjectProjectsIdEndpoint object.
        """
        child = ProjectProjectsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProjectModel]:
        """
        Performs a GET request against the /project/projects endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProjectModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectModel]:
        """
        Performs a GET request against the /project/projects endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectModel]: The parsed response data.
        """
        return self._parse_many(ProjectModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectModel:
        """
        Performs a POST request against the /project/projects endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectModel: The parsed response data.
        """
        return self._parse_one(ProjectModel, super().make_request("POST", params=params).json())
        