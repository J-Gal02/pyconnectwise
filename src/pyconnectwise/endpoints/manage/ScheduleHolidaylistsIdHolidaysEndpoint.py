from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleHolidaylistsIdHolidaysIdEndpoint import (
    ScheduleHolidaylistsIdHolidaysIdEndpoint,
)
from pyconnectwise.endpoints.manage.ScheduleHolidaylistsIdHolidaysInfoEndpoint import (
    ScheduleHolidaylistsIdHolidaysInfoEndpoint,
)

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ScheduleHolidaylistsIdHolidaysEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "holidays", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(
            ScheduleHolidaylistsIdHolidaysInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> ScheduleHolidaylistsIdHolidaysIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ScheduleHolidaylistsIdHolidaysIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ScheduleHolidaylistsIdHolidaysIdEndpoint: The initialized ScheduleHolidaylistsIdHolidaysIdEndpoint object.
        """
        child = ScheduleHolidaylistsIdHolidaysIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
