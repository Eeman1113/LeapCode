// popup.js
chrome.runtime.sendMessage({command: "extract_code", url: document.URL}, function(response) {
  document.getElementById('code').textContent = response;
});
