import abc

import requests

from ._access_token import AccessToken


class LoginButton(abc.ABC):
    @property
    @abc.abstractmethod
    def connected(self) -> bool: ...

    @property
    @abc.abstractmethod
    def simple_salesforce_args(self): ...

    @property
    @abc.abstractmethod
    def session(self) -> requests.Session: ...

    @property
    @abc.abstractmethod
    def access_token(self) -> AccessToken[None]: ...

    @abc.abstractmethod
    def refresh(self) -> None:
        """Attempt to refresh the connection using a refresh token."""
        ...


class Oneshot(LoginButton):
    pass


class JH(LoginButton):
    pass


class Server(LoginButton):
    pass
