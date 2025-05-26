# mosf

> A "Sign in to Salesforce" Anywidget button for Marimo

`mosf` makes it easy to connect your Marimo notebooks to Salesforce using a web-based oauth flow. There's no need to store rotating passwords and security tokens. Sign in with just a click. `pip install mosf[widget]`

## Usage

```python
# ======cell 1======
import marimo as mo
import mosf

    # Use one-shot callback server; local dev only
login_button = mosf.login_button()
# ==================

# ======cell 2======
mo.stop(not login_button.connected)

    # Create a `simple_salesforce` client. You can also use a standard
    # `requests` session for REST calls not supported by `simple_salesforce`
from simple_salesforce import Salesforce
sf: Salesforce = Salesforce(
    instance_url=login_button.token.instance_url,
    session_id=login_button.token.access_token,
)
# ==================
```

## Getting Started

1. Follow the instructions in [Setting up your External Client App](docs/setting-up-your-external-client-app.md) to create an External Client App in your target org.
2. Pass your External Client App's configuration into the `login_button` function.
  - By default, `login_button` will spin up a local, oneshot HTTP server to handle individual callback requests. This is enough for local development, but it may not be suitable for shared or remote environments. For remote, single-user environments, read [Using the Standalone Callback Server](docs/using-the-standalone-callback-server.md). For Marimo environments served from JupyterHub, read [The JupyterHub Callback Service](docs/the-jupyterhub-callback-service).

```python
import mosf
login_button = mosf.login_button(
    consumer_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', # Defaults to os.environ.get('MOSF_CONSUMER_KEY')
    consumer_secret='xxxxxxxxxxxxxxxxx', # Optional, since mosf uses PKCE. Enhances security. Defaults to os.environ.get('MOSF_CONSUMER_SECRET')
    oneshot=True, # Default option. Use an integrated, oneshot callback server, rather than a standalone server.
)
```
