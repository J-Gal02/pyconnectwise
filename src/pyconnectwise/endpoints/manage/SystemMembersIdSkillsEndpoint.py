from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdSkillsCountEndpoint import SystemMembersIdSkillsCountEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdSkillsIdEndpoint import SystemMembersIdSkillsIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import MemberSkill
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemMembersIdSkillsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[MemberSkill], ConnectWiseManageRequestParams],
    IPostable[MemberSkill, ConnectWiseManageRequestParams],
    IPaginateable[MemberSkill, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "skills", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[MemberSkill])
        IPostable.__init__(self, MemberSkill)
        IPaginateable.__init__(self, MemberSkill)

        self.count = self._register_child_endpoint(SystemMembersIdSkillsCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> SystemMembersIdSkillsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMembersIdSkillsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemMembersIdSkillsIdEndpoint: The initialized SystemMembersIdSkillsIdEndpoint object.
        """
        child = SystemMembersIdSkillsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[MemberSkill]:
        """
        Performs a GET request against the /system/members/{id}/skills endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberSkill]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), MemberSkill, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[MemberSkill]:
        """
        Performs a GET request against the /system/members/{id}/skills endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberSkill]: The parsed response data.
        """
        return self._parse_many(MemberSkill, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> MemberSkill:
        """
        Performs a POST request against the /system/members/{id}/skills endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberSkill: The parsed response data.
        """
        return self._parse_one(MemberSkill, super()._make_request("POST", data=data, params=params).json())
