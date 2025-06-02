from typing import Any, Literal, Optional

import attrs

URL = str
TimestampMs = int


def _split_str(x: str | list[str]):
    return x.split(" ") if isinstance(x, str) else x


@attrs.frozen(slots=True, kw_only=True)
class AccessToken[State]:
    """Access token as described in the [Salesforce docs](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_web_server_flow.htm&type=5)."""

    access_token: str
    signature: str
    scope: list[str] = attrs.field(converter=_split_str)
    id_token: str
    instance_url: URL
    id: URL
    token_type: Literal["Bearer"] = "Bearer"
    issued_at: TimestampMs = attrs.field(converter=int)
    refresh_token: Optional[str]
    sfdc_site_url: Optional[URL]
    sfdc_site_id: Optional[str]
    state: State

    def asdict(self) -> dict[str, Any]:
        return attrs.asdict(inst=self)
