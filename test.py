from pyppeteer_page_proxy import start_server

# Your list of proxies
proxies = [
    "45.9.122.111:8192",
    "154.85.125.136:6347",
    "45.146.180.239:9309"
]

username = "get_pass_from_g"
password = "get_pass_from_g"
schemes = ("http", )
headers = {"User-Agent": "Chrome"}
port = 8000

start_server(proxies=proxies, 
             username=username, 
             password=password, 
             schemes=schemes, 
             headers=headers, 
             port=port)

# Try this URL now:
# http://127.0.0.1:8000/?url=http%3A%2F%2Fcheckip.dyndns.org
