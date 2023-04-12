from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

import requests
from requests.auth import HTTPProxyAuth

import urllib.parse
import random
import threading


def proxy_get(
        url: str, 
        proxy: str, 
        auth: tuple | None = None,
        schemes: tuple = ("http", ),
        **kwargs
    ):
    """Send a GET request through a proxy.

    Args:
        url (str): The server to send the GET request to
        proxy (str): The proxy server as http(s)://ip:port
        auth (tuple | None): Username/password for proxy (username, password)
        schemes (tuple): Url schemes to be used ('http', 'https', etc)
        **kwargs: Arguments to be passed to requests.Session.get()

    Returns:
        requests.Response: The server's response to the GET request
    """
    s = requests.Session()

    proxies = {scheme: f"{scheme}://" + proxy for scheme in schemes}

    s.proxies = proxies

    if auth:
        s.auth = HTTPProxyAuth(*auth)
    
    return s.get(url, **kwargs)


def app(proxies: list[str],
        username: str | None = None, 
        password: str | None = None,
        schemes: tuple[str] = ("http", ),
        headers: dict = {"User-Agent": "Chrome"}):
    """Create a FastAPI which routes GET requests through proxies.

    Args:
        proxies (list[str]): List of proxies to route traffic through
        username (str | None): Username for authentication if any
        password: (str | None): Password for authenticaiton if any
        schemes: (tuple[str]): URI schemes for proxies (http, https, socks5)
        headers (dict): HTTP Headers to attach to requests

    Returns:
        FastAPI: The proxy-redirect server
    """

    app = FastAPI()

    @app.get("/")
    def forward_proxy(url: str):
        """Forward a request through a proxy and return the response

        Args:
            url (str): URL to get encoded with urllib.parse.quote_plus()

        Returns:
            HTMLResponse: The requested page obtained through proxy
        """
        # Decode url
        url = urllib.parse.unquote_plus(url)

        # Randomly select proxy
        proxy = random.choice(proxies)
        
        # Create authentication tuple
        if username and password:
            auth = (username, password)
        else:
            auth = None

        # Get the page through a proxy
        response = proxy_get(url, 
                             proxy, 
                             auth, 
                             schemes=schemes, 
                             headers=headers)

        # Return the page as HTML response
        return HTMLResponse(response.text)

    print("Makin the app")
    return app


def start_server(proxies: list[str], port: int = 8000, **kwargs):
    """Start a FastAPI server for routing requests through proxies.

    Args:
        proxies (list[str]): List of proxies to route traffic through
        username (str | None): Username for authentication if any
        password: (str | None): Password for authenticaiton if any
        schemes: (tuple[str]): URI schemes for proxies (http, https, socks5)
        headers (dict): HTTP Headers to attach to requests
        port (int): The port to run the FastAPI server on
    """
    api = app(proxies, **kwargs)
    thread = threading.Thread(target=uvicorn.run,
                              args=[api],
                              kwargs={"port": port},
                              name="uvicorn_proxy_server")

    thread.start()
    #uvicorn.run(app(proxies, **kwargs), port=port)
