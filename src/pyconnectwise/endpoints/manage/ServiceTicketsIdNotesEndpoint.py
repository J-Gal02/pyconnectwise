from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceTicketsIdNotesIdEndpoint import ServiceTicketsIdNotesIdEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdNotesCountEndpoint import ServiceTicketsIdNotesCountEndpoint
from pyconnectwise.models.manage.ServiceNoteModel import ServiceNoteModel

class ServiceTicketsIdNotesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceTicketsIdNotesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceTicketsIdNotesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceTicketsIdNotesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceTicketsIdNotesIdEndpoint: The initialized ServiceTicketsIdNotesIdEndpoint object.
        """
        child = ServiceTicketsIdNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ServiceNoteModel]:
        """
        Performs a GET request against the /service/tickets/{parentId}/notes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceNoteModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ServiceNoteModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ServiceNoteModel]:
        """
        Performs a GET request against the /service/tickets/{parentId}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceNoteModel]: The parsed response data.
        """
        return self._parse_many(ServiceNoteModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceNoteModel:
        """
        Performs a POST request against the /service/tickets/{parentId}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceNoteModel: The parsed response data.
        """
        return self._parse_one(ServiceNoteModel, super().make_request("POST", params=params).json())
        