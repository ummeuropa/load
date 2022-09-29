import re

def main(url: str = None, output = None):
    if not url: url = args.url
    if not output: output = "downloads"

    website = None

    if   re.match(r"https?://.*.fapello.com.*", url)  : website = "Fapello"
    elif re.match(r"https?://.*.bunkr.is.*", url)     : website = "Bunkr"
    elif re.match(r"https?://.*.gofile.io.*", url)    : website = "GoFile"
    elif re.match(r"https?://.*.cyberdrop.me.*", url) : website = "Cyberdrop"
    elif re.match(r"https?://.*.fanbox.cc.*", url)    : website = "Fanbox"    # ---> work in progress!
    elif re.match(r"https?://.*.pixiv.net.*", url)    : website = "Pixiv"
    elif re.match(r"https?://.*.rule34.xxx.*", url)   : website = "Rule34"
    else:
        with open("ydl.txt") as f:
            ydl_supported = f.readlines()
            for supported in ydl_supported: 
                re_pattern = f"https?://.*{supported.strip().lower()}.*"
                if re.match(re_pattern, url):
                    import youtube_dl

                    class MyLogger(object):
                        def debug(self, msg): pass
                        def warning(self, msg): pass
                        def error(self, msg): print(msg)

                    def my_hook(d):
                        if d['status'] == 'finished':
                            print('Done downloading, now converting ...')
                    ydl_opts = {
                        'outtmpl': f'{output}/%(title)s.%(ext)s',
                        'logger': MyLogger(),
                        'progress_hooks': [my_hook] }
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url]); return
        print("\033[31;1mError:\033[0m cannot recognize url"); return

    params = "url"
    if args.verbose: params += ", verbose=True"
    if website:
        exec(f"from plugins import {website}")
        global api; exec(f"global api; api = {website}({params})")
        api.download(output)
    return

if __name__ == "__main__":
    import argparse, plugins.__messages as __messages
    
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-u", "--url")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-o", "--output")
    parser.add_argument("-h", "--help", action="store_true")
    args = parser.parse_args()

    if args.help:
        print(__messages.help) ; exit(0)

    if not args.url:
        print(__messages.nourl); exit(1)

    if args.output: main(output=args.output)
    else: main()