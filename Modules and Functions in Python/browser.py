import webbrowser

# webbrowser.open("https://www.python.org")
chrome = webbrowser.get(using='chromium-browser')
chrome.open_new_tab("https://www.python.org")