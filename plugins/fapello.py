import re, requests
from megaloader.http import http_download

VID = r"^\s+<video.*src=\"(https:\/\/cdn.fapello.com\/content.+)\".*<\/video>$"
IMG = r"^\s+<img src=\"(https:\/\/fapello.com\/content\/.+)\" alt=\".+\">$"

class Fapello:
    def __init__(self, url: str, verbose = False):
        self.model = None
        self.verbose = verbose
        match = re.search(r"https://fapello.com/([a-zA-Z0-9_\-\~\.]+)", url)
        if not match: raise ValueError("Invalid fapello url provided.")
        
        self.model = match[1]
        if verbose: 
            print(f"\033[32;1mModel found:\033[0m {self.model} ---> proceeding to download")

    def __get_pages(self):
        i = 1
        while True:
            url = f"https://fapello.com/ajax/model/{self.model}/page-{i}/"
            page = requests.get(url)
            if not page.text: break
            i += 1
            yield page.text

    @staticmethod
    def __get_media_links(page: str):
        return re.findall(r"https://fapello.com/[a-zA-Z0-9_\-\~\.]+/\d+", page, re.M)

    @staticmethod
    def __get_media(page_url: str):
        page = requests.get(page_url).text
        f = v if (v := re.findall(VID, page, re.M)) else re.findall(IMG, page, re.M)
        return f

    def export(self):
        mediarray = []; c = 0
        for page in self.__get_pages():
            for media_link in self.__get_media_links(page):
                for media in self.__get_media(media_link):
                    mediarray.append((c := c+1, media))
        return mediarray
    
    def download(self, output: str):
        mediarray = self.export()
        filec = mediarray[-1][0]
        if self.verbose: print(f"\033[33;1mFiles\t%\tCurrent file\033[0m")
        for (counter, media) in mediarray:
            http_download(media, output, filec=filec, counter=counter, verbose=self.verbose)
        return