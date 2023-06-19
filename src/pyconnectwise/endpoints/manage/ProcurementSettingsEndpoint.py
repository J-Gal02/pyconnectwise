from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementSettingsIdEndpoint import ProcurementSettingsIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementSettingsCountEndpoint import ProcurementSettingsCountEndpoint
from pyconnectwise.models.manage.ProcurementSettingModel import ProcurementSettingModel

class ProcurementSettingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "settings", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementSettingsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProcurementSettingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementSettingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementSettingsIdEndpoint: The initialized ProcurementSettingsIdEndpoint object.
        """
        child = ProcurementSettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProcurementSettingModel]:
        """
        Performs a GET request against the /procurement/settings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProcurementSettingModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProcurementSettingModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProcurementSettingModel]:
        """
        Performs a GET request against the /procurement/settings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProcurementSettingModel]: The parsed response data.
        """
        return self._parse_many(ProcurementSettingModel, super().make_request("GET", params=params).json())
        