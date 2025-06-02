"""TODO."""

import os
from typing import Literal, Optional, Union


def login_button(
    consumer_key: Optional[str] = os.environ.get("MOSF_CONSUMER_KEY"),
    consumer_secret: Optional[str] = os.environ.get("MOSF_CONSUMER_SECRET"),
    username: Optional[str] = os.environ.get("MOSF_USERNAME"),
    password: Optional[str] = os.environ.get("MOSF_PASSWORD"),
    security_token: Optional[str] = os.environ.get("MOSF_SECURITY_TOKEN"),
    callback_type: Literal["oneshot", "jh", "server"] = "oneshot",
    login_url: Optional[str] = None,
    callback_url: Optional[str] = None,
    domain: Union[Literal["login", "test"], str, None] = "login",
):
    """TODO."""
    if callback_type == "oneshot":
        ...
    if callback_type == "server":
        ...
    if callback_type == "jh":
        ...
