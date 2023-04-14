from setuptools import setup, find_packages

setup(
    name="async_rotating_proxy",
    version="0.1",
    license="MIT",
    author="Gregory Bizup",
    author_email = "g.bizup@gmail.com",
    packages=find_packages("async_rotating_proxy"),
    pacakge_dir={'': 'async_rotating_proxy'},
    url="https://github.com/gbiz123/async-rotating-proxy",
    keywords=["proxy", "rotating proxy", "pyppeteer proxy", "selenium proxy", "scraping"],
    install_requires=[
        "aiohttp==3.8.4",
        "fastapi==0.95.1",
        "pyppeteer==1.0.2",
        "uvicorn==0.21.1",
    ],
)


