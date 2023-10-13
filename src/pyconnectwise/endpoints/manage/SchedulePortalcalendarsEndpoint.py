from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SchedulePortalcalendarsCountEndpoint import SchedulePortalcalendarsCountEndpoint
from pyconnectwise.endpoints.manage.SchedulePortalcalendarsIdEndpoint import SchedulePortalcalendarsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import PortalCalendar
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SchedulePortalcalendarsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[PortalCalendar], ConnectWiseManageRequestParams],
    IPaginateable[PortalCalendar, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "portalcalendars", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[PortalCalendar])
        IPaginateable.__init__(self, PortalCalendar)

        self.count = self._register_child_endpoint(SchedulePortalcalendarsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SchedulePortalcalendarsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SchedulePortalcalendarsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SchedulePortalcalendarsIdEndpoint: The initialized SchedulePortalcalendarsIdEndpoint object.
        """
        child = SchedulePortalcalendarsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[PortalCalendar]:
        """
        Performs a GET request against the /schedule/portalcalendars endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalCalendar]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), PortalCalendar, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[PortalCalendar]:
        """
        Performs a GET request against the /schedule/portalcalendars endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalCalendar]: The parsed response data.
        """
        return self._parse_many(PortalCalendar, super()._make_request("GET", data=data, params=params).json())
