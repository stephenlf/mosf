from dataclasses import dataclass
from typing import Any, Literal, NewType, Optional
from urllib.parse import urlparse

import anywidget
import traitlets
from requests_oauthlib import OAuth2Session

SerializedState = NewType("SerializedState", str)
# """A JSON serialized, URL-encoded State"""

TimestampMilli = NewType("TimestampMilli", int)

# @dataclass(slots=True)
# class State:
#     """"""
#     ...


@dataclass
class AccessToken:
    access_token: str
    signature: Optional[str]
    scope: list[str]
    id_token: str
    instance_url: str
    id: str
    issued_at: TimestampMilli
    refresh_token: Optional[str]
    sfdc_site_url: Optional[str]
    sfdc_site_id: Optional[str]
    state: Optional[SerializedState]

    token_type: Literal["Bearer"] = "Bearer"


class SFLoginWidget(anywidget.AnyWidget):
    """Salesforce Login Anywidget"""

    _esm = "static/widget.js"
    _css = "static/widget.css"

    def __init__(
        self,
        label: str = "Sign in to Salesforce",
        alias: Optional[str] = None,
        domain: str = "login",
    ):
        self.label = label
        self._alias = alias

    connected = traitlets.Bool(False).tag(sync=True)
    session: OAuth2Session | None = None

    @property
    def access_token(self) -> AccessToken | None:
        if self.session is None:
            return None
        access_token_dict: dict[str, Any] = self.session.access_token  # type: ignore[access_token]
        return AccessToken(**access_token_dict)

    @property
    def instance_url(self) -> str | None:
        if self.access_token is not None:
            return self.access_token.instance_url

    @property
    def alias(self) -> str | None:
        if (
            self.access_token is None
            or (hostname := urlparse(self.access_token.instance_url).hostname)
            is None
        ):
            return None
        [instance, *_] = hostname.split(".")
        return self._alias or instance
