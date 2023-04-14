from setuptools import setup, find_packages

setup(
    name="rotating_proxy_api",
    version="0.1",
    license="MIT",
    author="Gregory Bizup",
    author_email = "g.bizup@gmail.com",
    packages=find_packages("rotating_proxy_api"),
    pacakge_dir={'': 'proxy_api'},
    url="https://github.com/gbiz123/rotating-proxy-api",
    keywords=["proxy", "rotating proxy", "pyppeteer proxy", "selenium proxy", "scraping"],
    install_requires=[
        "aiohttp==3.8.4",
        "fastapi==0.95.1",
        "pyppeteer==1.0.2",
        "uvicorn==0.21.1",
    ],
)


