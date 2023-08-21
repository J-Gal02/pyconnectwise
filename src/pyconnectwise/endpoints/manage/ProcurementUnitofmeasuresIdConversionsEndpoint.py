from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementUnitofmeasuresIdConversionsCountEndpoint import \
    ProcurementUnitofmeasuresIdConversionsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementUnitofmeasuresIdConversionsIdEndpoint import \
    ProcurementUnitofmeasuresIdConversionsIdEndpoint
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.models.manage import Conversion
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementUnitofmeasuresIdConversionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "conversions", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProcurementUnitofmeasuresIdConversionsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementUnitofmeasuresIdConversionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementUnitofmeasuresIdConversionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementUnitofmeasuresIdConversionsIdEndpoint: The initialized ProcurementUnitofmeasuresIdConversionsIdEndpoint object.
        """
        child = ProcurementUnitofmeasuresIdConversionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Conversion]:
        """
        Performs a GET request against the /procurement/unitOfMeasures/{id}/conversions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Conversion]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Conversion,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Conversion]:
        """
        Performs a GET request against the /procurement/unitOfMeasures/{id}/conversions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Conversion]: The parsed response data.
        """
        return self._parse_many(Conversion, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Conversion:
        """
        Performs a POST request against the /procurement/unitOfMeasures/{id}/conversions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Conversion: The parsed response data.
        """
        return self._parse_one(Conversion, super()._make_request("POST", data=data, params=params).json())