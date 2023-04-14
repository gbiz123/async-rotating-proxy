from pyppeteer import launch
from pyppeteer_page_proxy import ProxyAPI

# Your list of proxies
proxies = [
    "45.9.122.111:8192",
    "154.85.125.136:6347",
    "45.146.180.239:9309"
]

username = "humsvtdp"
password = "vqvum5ujzbw6"
scheme = "http"
headers = {"User-Agent": "Chrome"}
port = 8000

proxy_api = ProxyAPI(proxies, username, password, port, scheme)

proxy_api.start_server()

url = proxy_api.format_url("http://checkip.dyndns.org/")

# Try this URL now:
# http://127.0.0.1:8000/?url=http%3A%2F%2Fcheckip.dyndns.org
