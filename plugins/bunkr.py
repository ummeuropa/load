import re
import json
import requests
from megaloader.http import http_download

REGEX_BUILD_ID = r"<script id=\"__NEXT_DATA__\" type=\"application\/json\">(\{.*\})<\/script>"

class Bunkr:
    def __init__(self, url: str, verbose = False):
        self.__url = url
        self.verbose = verbose

    @property
    def url(self): return self.__url

    def getBuildId(self, resText):
        return json.loads(re.search(REGEX_BUILD_ID, resText)[1])["buildId"]

    def getNextUrl(self, url, buildId, isAlbum = True):
        valToReplace = "/a/" if isAlbum else "/v/"
        url = url.replace(valToReplace, f"/_next/data/{buildId}{valToReplace}") + ".json"
        return url

    def export(self):
        response = requests.get(self.url)
        buildId = self.getBuildId(response.text)
        # is album
        if "/a/" in self.url:
            mediarray = []; c = 0
            nextUrl = self.getNextUrl(self.url, buildId)
            files = json.loads(requests.get(nextUrl).text)["pageProps"]["files"]
            for url in files:
                mediarray.append((c:=c+1, url["cdn"].replace("cdn", "media-files") + '/' + url["name"]))
            return mediarray
        # is specific resource
        else:
            nextUrl = self.getNextUrl(self.url, buildId, False)
            file = json.loads(requests.get(nextUrl).text)["pageProps"]["file"]
            domain = file["mediafiles"]
            name = file["name"]
            return [(1, (f"{domain}/{name}"))]

    def download(self, output: str):
        mediarray = self.export()
        filec = mediarray[-1][0]
        if self.verbose: print(f"\033[33;1mFiles\t%\tCurrent file\033[0m")
        for (counter, media) in mediarray:
            http_download(media, output, filec=filec, counter=counter, verbose=self.verbose)
        return