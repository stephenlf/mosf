function render({ model, el }) {
  let connected = model.get("connected");
  const label = model.get("label");
  const alias = model.get("alias");
  let div = document.createElement("div");

  div.innerHTML = `
    <button class="login">${label}</button>
    ${!connected ? "" : 
        `<span class="status">Connected to "${alias}"</span>`
      }
  `;

  div.addEventListener('click', () => {
    
  })
  
  el.appendChild(div);
}