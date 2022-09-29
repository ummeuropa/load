import hashlib, requests
from megaloader.http import http_download

class GoFile:
    def __init__(self, url: str, password: str = None, verbose = False):
        self.__password = None
        self.__content_id = url[len("https://gofile.io/d/"):]
        self.__api_key = self.__get_api_key()
        self.verbose = verbose

        if password:
            self.__password = hashlib.sha256(password.encode()).hexdigest()

    @property
    def content_id(self): return self.__content_id

    @property
    def api_key(self): return self.__api_key

    @property
    def password(self): return self.__password

    @staticmethod
    def __get_api_key():
        data = requests.get("https://api.gofile.io/createAccount").json()
        api_token = data["data"]["token"]
        data = requests.get("https://api.gofile.io/getAccountDetails?token=" + api_token).json()
        if data["status"] != 'ok':
            raise Exception("The account was not successfully activated.")
        return api_token

    def export(self):
        url = "https://api.gofile.io/getContent?contentId={}&token={}&websiteToken=12345&cache=true"
        url = url.format(self.content_id, self.api_key)

        mediarray = []; c = 0
        if self.password:
            url += "&password=" + self.password
        resources = requests.get(url).json()
        if "contents" in resources["data"].keys():
            contents = resources["data"]["contents"]
            for content in contents.values():
                mediarray.append((c:=c+1, content["link"]))
        return mediarray

    def download(self, output: str):
        mediarray = self.export()
        filec = mediarray[-1][0]
        if self.verbose: print(f"\033[33;1mFiles\t%\tCurrent file\033[0m")
        for (counter, media) in mediarray:
            http_download(media, output, filec=filec, counter=counter, verbose=self.verbose,
            custom_headers={"Cookie": "accountToken=" + self.api_key})
        return