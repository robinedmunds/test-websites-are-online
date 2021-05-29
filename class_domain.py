#!/usr/bin/env python3
#
# https://urllib3.readthedocs.io/en/latest/user-guide.html

import re
import urllib3

class Domain:
    def __init__(self, domain, www=True, https=True):
        self.domain = domain  # without protocol or www
        self.www = www
        self.https = https

        self.strip_prefix_from_url()

    def strip_prefix_from_url(self):
        self.domain = re.sub(r"^https?://", "", self.domain, count=1)
        self.domain = re.sub(r"^www\.", "", self.domain, count=1)

    def __test_domain(self, url):
        http = urllib3.PoolManager()
        try:
            res = http.request("GET", f"{url}", redirect=True)
            err = "OK"
            if res.status != 200:
                err = "!!! ERROR !!!"
            print(f"{err}\t{res.status}\t{url}")
        except Exception:
            print(f"!!! ERROR !!! Server could not be contacted - {url}")

    def test(self):
        url = f"http://{self.domain}"
        self.__test_domain(url)

        if self.www:
            url = f"http://www.{self.domain}"
            self.__test_domain(url)

        if self.https:
            url = f"https://{self.domain}"
            self.__test_domain(url)

        if self.https and self.www:
            url = f"https://www.{self.domain}"
            self.__test_domain(url)
