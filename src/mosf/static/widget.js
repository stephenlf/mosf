/** @param {{ model: DOMWidgetModel, el: HTMLElement }} context */
export function render({ model, el }) {
  const connected = model.get("connected");
  const label = model.get("label") ?? "Log in to Salesforce";
  const alias = model.get("alias");

  /** "Sign in to Salesforce" button */
  const btn = document.createElement("button");
  btn.classList = "button";
  btn.innerHTML = label;

  /** "Connected to login" status text */
  const span = document.createElement("span");
  span.classList = "status";
  span.innerHTML = `Connected to "${alias}"`;

  el.appendChild(div);
  if (connected) {
    el.appendChild(span);
  }

  /**
   * 1) Request an authentication URL from the backend
   * 2) Open the URL in a new window
   * 3) Wait for the window to write the token back
   * 4) Forward the token to the backend widget
   */
  btn.onclick = () => {
    const loginUrl = model.get("login_url");
    /** 
     * @type {Array<string>} list of domains the callback server is hosted on.
     * E.g. ["http://localhost:5000", "https://callback.example.com"] 
     */
    const allowedOrigins = model.get("allowed_origins");

    window.open(loginUrl, "_blank", "width=400,height=400");

    function onMessage(event) {
      /** Validation. */
      if (event.data.type !== 'mosf-callback') {
        return;
      }
      if (!allowedOrigins.includes(event.origin)) {
        throw new Error(`Origin not allowed:  ${event.origin}`);
      }

      /** Parse token data from window response and send to backend */
      const token = event.data.token;
      model.set('token', token);
      model.set('connected', true);
      model.save_changes();

      /** Auth flow complete. Remove listener. */
      window.removeEventListener('message', onMessage);
    }
    window.addEventListener('message', onMessage);
  };
  
  el.appendChild(div);
}