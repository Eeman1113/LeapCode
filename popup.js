// popup.js
document.addEventListener('DOMContentLoaded', function() {
  chrome.runtime.sendMessage({command: "extract_code", url: document.URL}, function(response) {
    document.getElementById('code').textContent = response;
  });
});
