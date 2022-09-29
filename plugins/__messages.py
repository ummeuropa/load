help = "\n\
------------------------- LOAD v0.1 ------------------------\n\n\
\033[33mDescription:\033[0m this program automates the download of images\n\
and videos from a variety of websites. The currently supported\n\
websites are:\n\
                fapello.com      bunkr.io      cyberdrop.me\n\
                fanbox.cc        gofile.io     pixiv.net\n\
                rule34.xxx\n\n\
\033[33m* Open a feature request on GitHub for new websites *\033[0m\n\n\
\033[33mUsage:\033[0m python load.py [-h] [-v] [-o OUTPUT] [-u URL]\n\n\
arguments:\n\
  -u, --url             url of the website to download from\n\n\
optional arguments:\n\
  -h, --help            show this help message and exit\n\
  -v, --verbose         enable verbose mode, print logs to stdout\n\
  -o, --output          set download location. default is ./downloads\n\n\
\033[33m*** If you like my work, please consider donating! ***\033[0m\n\n\
USDT/ETH/MATIC: \033[33m0xfbccdd2e2f17c72fbdc41f172c9f572017b57e30\033[0m\n\
\
"

nourl = "\033[91mError:\033[0m you need to provide a url. \
Use \033[33mpython\033[0m load.py \033[38;2;100;100;100m-h\033[0m for help"