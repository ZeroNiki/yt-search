from bs4 import BeautifulSoup
from pyfzf import FzfPrompt

import subprocess
import requests
import re

fzf = FzfPrompt()


def scrape():
    print("Scraping...")

    # get links from txt file
    with open("channel.txt", "r", encoding="utf-8") as file:
        links = file.read().splitlines()

    about_video = []
    for link in links:
        link_list = []

        r = requests.get(link, stream=True, timeout=20)

        soup = BeautifulSoup(r.content, "lxml",
                             multi_valued_attributes=None)

        channel_name = []
        for p_channel in soup.find_all("p", class_="channel-name"):
            text_p = p_channel.text.strip()
            channel_name.append(text_p)

        for div_card in soup.find_all("div", class_="video-card-row"):
            find_a = div_card.find("a").get("href")
            find_a_name = div_card.find("a").text
            for channel in channel_name:
                link_list.append(
                    f"{channel}  ||  {find_a_name}  ||  https://www.youtube.com{find_a}")

        about_video.append(link_list)

    not_data = []
    for info in about_video:
        for more in info:
            not_data.append(more)

    seen = set()
    clear_data = []
    for item in not_data:
        if item not in seen:
            seen.add(item)
            clear_data.append(item)

    get_data = fzf.prompt(clear_data)

    data_to_str = ''.join(get_data)

    video_link = re.search(
        "(?P<url>https?://[^\s]+)", data_to_str).group("url")

    subprocess.run(["mpv", video_link])
