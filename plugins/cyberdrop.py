import re
import requests
from megaloader.http import http_download

REGEX_MEDIA = r"(?:https:\/\/)[^cdn\.][a-z0-9\-\/\.]+.cyberdrop.(?:to|me)\/[a-z0-9_\-A-Z \(\)\/]+.(?:mp4|mov|m4v|ts|mkv|avi|wmv|webm|vob|gifv|mpg|mpeg|mp3|flac|wav|png|jpeg|jpg|gif|bmp|webp|heif|heic|tiff|svf|svg|ico|psd|ai|pdf|txt|log|csv|xml|cbr|zip|rar|7z|tar|gz|xz|targz|tarxz|iso|torrent|kdbx)"

class Cyberdrop:
    def __init__(self, url: str, verbose = False) -> None:
        self.url = url
        self.verbose = verbose

    def export(self):
        mediarray = []; c = 0
        response = requests.get(self.url)
        for url in re.findall(REGEX_MEDIA, response.text):
            if "/thumbs/" in url or "/s/" in url: continue
            if url.index("cyberdrop") < 14 or url.index("cyberdrop") > 18: continue
            mediarray.append((c:=c+1, url))
        return mediarray

    def download(self, output: str):
        mediarray = self.export()
        filec = mediarray[-1][0]
        if self.verbose: print(f"\033[33;1mFiles\t%\tCurrent file\033[0m")
        for (counter, media) in mediarray:
            http_download(media, output, filec=filec, counter=counter, verbose=self.verbose)
        return