import requests
from megaloader.http import http_download
import xml.etree.ElementTree as XML_ET

class Rule34:
    def __init__(self, tags: list, verbose = False):
        self.__tags = ["ass"]
        self.verbose = verbose

    @property
    def tags(self): return self.__tags

    def url_builder(self, pid, limit):
        l = f'https://rule34.xxx/index.php?page=dapi&s=post&q=index&tags={",".join(self.tags)}&pid={pid}&limit={limit}'
        if self.verbose: print(l)
        return l

    def export(self):
        mediarray = []; c = 0
        pid = -1; limit = 100
        while True:
            url = self.url_builder(pid:=pid+1, limit=limit)
            data = requests.get(url).text
            data = XML_ET.fromstringlist([data])
            posts = data.iter("post")
            for post in posts: mediarray.append((c:=c+1, post.get("file_url")))
            if limit == pid: break
        return mediarray

    def download(self, output: str):
        mediarray = self.export()
        filec = mediarray[-1][0]
        if self.verbose: print(f"\033[33;1mFiles\t%\tCurrent file\033[0m")
        for (counter, media) in mediarray:
            http_download(media, output, filec=filec, counter=counter, verbose=self.verbose)
        return
