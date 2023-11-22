from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementShipmentmethodsIdUsagesListEndpoint import (
    ProcurementShipmentmethodsIdUsagesListEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable
from pyconnectwise.models.manage import Usage
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ProcurementShipmentmethodsIdUsagesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Usage], ConnectWiseManageRequestParams],
    IPaginateable[Usage, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "usages", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[Usage])
        IPaginateable.__init__(self, Usage)

        self.list = self._register_child_endpoint(
            ProcurementShipmentmethodsIdUsagesListEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Usage]:
        """
        Performs a GET request against the /procurement/shipmentmethods/{id}/usages endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Usage]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Usage, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Usage]:
        """
        Performs a GET request against the /procurement/shipmentmethods/{id}/usages endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Usage]: The parsed response data.
        """
        return self._parse_many(Usage, super()._make_request("GET", data=data, params=params).json())
