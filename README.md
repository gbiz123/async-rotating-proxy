# pyppeteer-page-proxy
Implement page-by-page proxy switching for pyppeteer.

## Purpose
The article referenced below sums it up pretty well:
"The chrome browser does not support fain-grained proxy configuration out of the box. Therefore, the following use cases are not possible when using puppeteer in combination with Google Chrome:

    Using different proxies for different tabs/windows
    Switching proxies without restarting the browser

This is a bit annoying, because restarting the entire browser is an expensive operation in terms of computational resources. The chrome restart takes up to two seconds (depending on the system). We ideally want to switch proxies whenever the need arises without restarting the entire chrome process. This is a common requirement when scraping websites in scale."

## Reference
Reimplementation of the nodejs code in https://incolumitas.com/2020/12/20/dynamically-changing-puppeteer-proxies/
