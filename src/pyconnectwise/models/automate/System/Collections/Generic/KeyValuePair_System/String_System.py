
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class String(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    key: (str | None) = Field(default=None, alias='Key')
    value: (str | None) = Field(default=None, alias='Value')