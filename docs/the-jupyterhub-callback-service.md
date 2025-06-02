# The JupyterHub Callback Service

If you are already running Marimo from JupyterHub, you can simplify things by running the callback server as a [JupyterHub-Managed Service](https://jupyterhub.readthedocs.io/en/stable/reference/services.html#launching-a-hub-managed-service).

## Usage

First, install the `jh` optional dependency.

```bash
pip install mosf[jh]
```

Then, add the following to `jupyterhub_config.py`. This will 

```python
c.JupyterHub.load_roles += [
    {
        "name": "mosf-callback",
        "scopes": []
    }
]

c.JupyterHub.services += [
    {
        "name": "mosf-callback",
        "command": [sys.executable, "-m", "mosf.jh"]
    }
]
```

With the JupyterHub service registered, users may create their "Sign in to Salesforce" by using the appropriate `callback_type`.

```python
import mosf
login_button = mosf.login_button(callback_type='jh')
```