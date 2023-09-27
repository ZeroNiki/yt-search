# yt-search (Linux) (RU)
Позволяет прсмотривать видео не заходя на сам youtube

Библеотеки задействованны:

- Bs4 ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/beautifulsoup4)

- request ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/requests)

- pyfzf ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyfzf)


## Перед устоновкой
Установите медиаплеер `mpv`

## Устоновка

склонируйтие репозиторий и перейдите в него:
```
git clone https://github.com/ZeroNiki/yt-search.git
cd yt-search
```

Установите зависимости:
```
pip install -r requirements.txt
```
По желанию можете делать это в виртуальном окружении

Запустите файл ytsearch.py:
```
python3 ytsearch.py
```

### Channel.py
Для того чтобы просматривать видео с любимых каналов, вы должны найти их на одном из сайтов [Invidious](https://docs.invidious.io/instances/), скопируйте сылку на них и вствьте в файл `channel.txt`

---------------

# yt-search (Linux) (EN)
Allows you to watch videos without going to YouTube itself

Libraries involved:

- Bs4 ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/beautifulsoup4)

- request ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/requests)

- pyfzf ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyfzf)


## Before installation
Install media player `mpv`

## Installation

Clone the repository and go to it:
```
git clone https://github.com/ZeroNiki/yt-search.git
cd yt-search
```

Install dependencies:
```
pip install -r requirements.txt
```
If you wish, you can do this in a virtual environment.

Run the ytsearch.py file:
```
python3 ytsearch.py
```

### Channel.py
In order to view videos from your favorite channels, you must find them on one of the sites [Invidious](https://docs.invidious.io/instances/), copy the link to them and paste them into the `channel.txt` file


