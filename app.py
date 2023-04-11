import random
from fastapi.responses import HTMLResponse
import requests
from fastapi import FastAPI, Request, Response
from pydantic import HttpUrl
import urllib.parse


# Your list of proxies
proxies = [
    "http://proxy1.com:port",
    "http://proxy2.com:port",
    "http://proxy3.com:port",
]

# Create an app
app = FastAPI()

# Route a URL to forward our request through the proxy
@app.get("/forward-proxy/{url:path}")
def forward_proxy(url: str):
    """Forward a request through a proxy and return the response

    Args:
        url (str): URL to get encoded with urllib.parse.quote_plus()
    """
    # Decode url
    url = urllib.parse.unquote_plus(url)

    # Randomly select proxy
    proxy = random.choice(proxies)

    # Get the page through a proxy
    response = requests.get(url, proxies={"http": proxy})

    # Return the page as HTML response
    return HTMLResponse(response.text)
