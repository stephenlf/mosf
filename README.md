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

# Create a `simple_salesforce` client.
from simple_salesforce import Salesforce
sf: Salesforce = Salesforce(
    **login_button.simple_salesforce_args
)

# Alternatively, you can use the authenticated requests session directly
import requests
session: requests.Session = login_button.session
# ==================
```

## Getting Started

1. Follow the instructions in [Setting up your External Client App](docs/setting-up-your-external-client-app.md) to create an External Client App in your target org.
2. Pass your External Client App's configuration into the `login_button` function.
  - By default, `login_button` will spin up a local, oneshot HTTP server to handle individual callback requests. This is enough for local development, but it may not be suitable for shared or remote environments. For remote, single-user environments, read [Using the Standalone Callback Server](docs/using-the-standalone-callback-server.md). For Marimo environments served from JupyterHub, read [The JupyterHub Callback Service](docs/the-jupyterhub-callback-service).

```python
import mosf
import requests
from simple_salesforce import Salesforce

login_button = mosf.login_button(,
    consumer_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', # Defaults to os.environ.get('MOSF_CONSUMER_KEY')
    consumer_secret='xxxxxxxxxxxxxxxxx', # Optional, since mosf uses PKCE. Enhances security. Defaults to os.environ.get('MOSF_CONSUMER_SECRET')
    callbacK_type='oneshot', # Default option. Use an integrated, oneshot callback server, rather than a standalone server.
)
```

## Running `mosf` in a script

`mosf`'s interactive web flow is not available when your notebook is being [run as a script](https://docs.marimo.io/guides/scripts/). Instead, `mosf` falls back to simple [security token](https://help.salesforce.com/s/articleView?id=xcloud.user_security_token.htm&type=5) authentication. You can pass your credentials to `mosf` directly or through environment variables.

```python
import mosf

login_button = mosf.login_button(
    username='example@example.com',      # Don't hard code credentials. Defaults to os.environ.get('MOSF_USERNAME')
    password='super-secret-password',    # Don't hard code credentials. Defaults to os.environ.get('MOSF_PASSWORD')
    security_token='xxxxxxxxxxxxxxxx',   # Don't hard code credentials. Defaults to os.environ.get('MOSF_SECURITY_TOKEN')
)
```

