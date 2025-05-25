# Using the Standalone Callback Server

When hosting your Marimo notebook in a remote or shared environment, it may not be prudent to use a simple oneoff server to handle OAuth callbacks. Multiple users attempting to log in at the same time may cause port collisions, and without a shared proxy, cross-origin request issues are a guarantee. 

To resolve this, you may spin up the standalone callback server.

```bash
# The standalone callback server is part of an optional `server` dependency.
pip add mosf[server]

# Run with fastapi
fastapi mosf.server
```

You may also run the server programmatically.

## Configuring the callback server

Configure the standalone server with these environment variables.

<details>
    <summary>MOSF_CONSUMER_KEY</summary>
    - **Required**
    - See [Setting up your External Client App](docs/setting-up-your-external-client-app.md) to create an External Client App and get your consumer key.
</details>
<details>
    <summary>MOSF_CONSUMER_SECRET</summary>
    - Optional, since `mosf` uses PKCE. But it add security.
    - See [Setting up your External Client App](docs/setting-up-your-external-client-app.md) to create an External Client App and get your consumer secret.
</details>
<details>
    <summary>MOSF_TARGET_ORIGIN</summary>
    - Optional. The url of the Marimo server.
    - This parameter is passed to the [`targetOrigin`](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage#targetorigin) parameter in the OAuth response. It must be set if the callback server and marimo server are hosted on different URLs (scheme, hostname, and port). For instance, if your Marimo Edit Server is hosted at `https://mo.mydomain.com/` and your callback server is hosted at `https://callback.mydomain.com/`, then you must set this env with `MOSF_Target_ORIGIN="https://mo.mydomain.com/"`
</details>

## Running the callback server programmatically

If the behavior of `fastapi mosf.server` is not enough for your needs, you may run the callback server programmatically. For instance, you may want to do this if you have multiple External Client Apps across multiple orgs that you want to authenticate to, and you are using custom logic to map requests to orgs.

```python
import uvicorn
from mosf.server import build_callback_server

def get_consumer_key(request):
    if request.org_alias == 'prod':
        return 'PRODUCTION_CONSUMER_KEY_HERE'
    else:
        return 'SANDBOX_CONSUMER_KEY_HERE'


app = build_callback_server(
    consumer_key=get_consumer_key
)

if __name__ == '__main__:
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
```

All environment variables listed above have a corresponding parameter in the `build_callback_server` function, which may accept a literal value or a `Callable`.

```python
import os
import uvicorn
from mosf.server import build_callback_server

def get_target_origin(request):
    if request.origin in ('127.0.0.1', 'localhost'):
        # Use local server
        return 'https://127.0.0.1:2718'
    else:
        # Use remote server
        return os.environ.get("MOSF_TARGET_ORIGIN")


app = build_callback_server(
    target_origin=get_target_origin,

)

if __name__ == '__main__:
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
```