import re
import requests
from megaloader.http import http_download

class Pixiv:

    def __init__(self, url: str, PHPSESSID: str = None, verbose = False):
        self.__creator_id = None
        self.__headers = {"Accept": "application/json",}
        match = re.search(r"https://www.pixiv.net/\w+/users/(\d+)", url)

        if not match: raise ValueError("Invalid pixiv url provided.")
        if PHPSESSID is not None: self.__headers["Cookie"] = "PHPSESSID=" + PHPSESSID
        self.__creator_id = match[1]
        self.verbose = verbose

    @property
    def creator_id(self):
        return self.__creator_id

    def get_user_home(self, top_only: bool = False):
        return requests.get("https://www.pixiv.net/ajax/user/" + self.creator_id + "/profile/" + ("top" if top_only else "all") + "?lang=en", headers=self.__headers).json()

    def get_user_home_illusts(self):
        return tuple(self.get_user_home()["body"]["illusts"].keys())

    def build_artwork_urls(self, artwork_id: str):
        # For loop to handle group illustrations.
        for illust in requests.get("https://www.pixiv.net/ajax/illust/" + artwork_id + "/pages?lang=en", headers=self.__headers).json()["body"]:
            yield illust["urls"]["original"]

    def export(self):
        mediarray = []; c = 0
        for artwork_id in self.get_user_home_illusts():
            for url in self.build_artwork_urls(artwork_id):
                mediarray.append((c:=c+1, url))
        return mediarray

    def download(self, output: str):
        mediarray = self.export()
        filec = mediarray[-1][0]
        if self.verbose: print(f"\033[33;1mFiles\t%\tCurrent file\033[0m")
        for (counter, media) in mediarray:
            http_download(media, output, filec=filec, counter=counter, verbose=self.verbose)
        return