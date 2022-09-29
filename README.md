# Megaloader

## Introduction
Load is a fork of [megaloader](https://github.com/Ximaz/megaloader) that
allows you automate the download of images and videos for many websites, such as [Cyberdrop](http://www.cyberdrop.me/), [fanbox](https://www.fanbox.cc) *(in progress)*, [GoFile](http://www.gofile.io/), [Pixiv](http://www.pixiv.net/), [Rule34](http://www.rule34.xxx/) and [Fapello](http://www.fapello.com/). Load also interfaces with [youtube-dl](https://github.com/ytdl-org/youtube-dl) to provide support for [YouTube](https://youtube.com/), [PornHub](https://pornhub.com), [RedTube](https://www.redtube.com/), [XHamster](https://xhamster.com/), [Reddit](https://reddit.com) and many, many more (you can find an complete list [here]())

If you know how to use *youtube_dl*, there's little reason to use Load to download PH videos and the like. Load's main concern is Cyberdrop, GoFile, Fapello and Mega *(in progress)*, but it comes in handy to be able to download videos from a variety of other websites using the same command (Load) you use to download from Fapello and GoFile while you're at it, and it's just as efficient.

Load comes with a GUI version so you don't need to bother yourself with the command line, and it's fairly straight foward.

## Setup

First of all, you're gonna need `Python 3.8+` for Load to work (this is because I decided to use the [asignment expressions](https://docs.python.org/3/reference/expressions.html#assignment-expressions) which aren't available in prior versions). To check your Python's version, do:
```
python3 --version // python --version on Windows
```

You're also gonna need `requests`, which can be installed with:
```
pip install requests
```
If you're gonna use the GUI version, you're gonna need `tkinter`, which depending on which OS you're using, it might be already installed along with your Python installation. If not:
```
pip install python3-tk
```
Lastly, if you intend to use Load to download PornHub videos, or YouTube videos, or basically anything that's not Cyberdrop, GoFile, Pixiv, Rule34 or Fapello, you're gonna need `youtube_dl`:
```
pip install youtube_dl
```
Or, for short, just do:
```
python3 -m pip install -r requirements.txt
```
## How to use

```
python3 load.py [-h] [-v] [-o OUTPUT] [-u URL]
```
### Arguments (required):
> `-u, --url: url of the website to download from`

### Optional arguments:
> `-h, --help: shows help message` \
> `-v, --verbose: enable verbose mode, print logs to stdout` \
> `-o, --output: set download location. default is ./downloads`

## Contribution
If you want to contribute, you can either make a pull request to patch an error in a Megaloader's plugin, or create yours which I just have to validate before merging. If you're facing any errors, please open an issue.

## Donate
If you like my work, please consider donating! USDT, ETH or MATIC:
```
0xfbccdd2e2f17c72fbdc41f172c9f572017b57e30
```

Also consider donating to [Ximaz](https://github.com/Ximaz), megaloader's author, who's work is the foundation of Load. You can find the link to their PayPal on [megaloader's github page]((https://github.com/Ximaz/megaloader))
