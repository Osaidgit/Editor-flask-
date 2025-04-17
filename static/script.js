function setTool(tool) {
  fetch('/set_tool', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ tool: tool })
  });
}
