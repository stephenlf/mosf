from dataclasses import dataclass
from typing import Optional, NewType, Literal

import anywidget
import traitlets
from requests_oauthlib import OAuth2Session


# SerializedState = NewType("SerializedState", str)
# """A JSON serialized, URL-encoded State"""

# TimestampMilli = NewType("TimestampMilli", int)

# @dataclass(slots=True)
# class State:
#     """"""
#     ...


# @dataclass
# class AccessToken:
#     access_token: str
#     signature: Optional[str]
#     scope: list[str]
#     id_token: str
#     instance_url: str
#     id: str
#     issued_at: TimestampMilli
#     refresh_token: Optional[str]
#     sfdc_site_url: Optional[str]
#     sfdc_site_id: Optional[str]
#     state: Optional[SerializedState]

#     token_type: Literal["Bearer"] = "Bearer"

class SFLoginWidget(anywidget.AnyWidget): 
    """Salesforce Login Anywidget"""
    
    _esm = "static/widget.js"
    _css = "static/widget.css"
    
    connected = traitlets.Bool(False).tag(sync=True)
    session: OAuth2Session | None = None