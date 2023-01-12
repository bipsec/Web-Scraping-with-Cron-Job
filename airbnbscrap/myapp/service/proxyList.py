# import modules
import random
import requests
from lxml.html import fromstring


class DynamicProxy:
    def __init__(self):
        title = "Dynamic Proxy"

    def get_proxies(self):
        url = 'https://free-proxy-list.net/'
        response = requests.get(url)
        parser = fromstring(response.text)
        proxies = set()
        for i in parser.xpath('//tbody/tr')[:10]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                # grabbing IP and Port
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)
        return list(proxies)

    def get_single_proxy(self):
        proxy = self.get_proxies()
        proxies = list(proxy)
        proxy = random.choice(proxies)
        # if type(proxy) == 'NoneType':
        #     return pr.get_proxies()
        return proxy

######### Cross Checking the function whether it works or not ##############3

#
# pr = DynamicProxy()
# print(pr.get_single_proxy())