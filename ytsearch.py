import requests
import re
import subprocess

from pyfzf import FzfPrompt
from bs4 import BeautifulSoup

from channel import scrape

fzf = FzfPrompt()


def search(keyword):
    try:
        url = f"https://invidious.tiekoetter.com/search?q={keyword}"

        r = requests.get(url)

        soup = BeautifulSoup(r.content, "lxml",
                             multi_valued_attributes=None)

        clear_list = []
        for div_card in soup.find_all("div", class_="video-card-row"):
            find_a = div_card.find("a").get("href")
            find_a_name = div_card.find("a").text

            clear_list.append(
                f"{find_a_name}  ||  https://www.youtube.com{find_a}")

        ui = fzf.prompt(clear_list)

        convert_to_str = "".join(ui)

        video_link = re.search(
            "(?P<url>https?://[^\s]+)", convert_to_str).group("url")

        subprocess.run(["mpv", video_link])

    except Exception:
        print("\nGoodBye\n")


def main():
    try:
        user_action = input(
            "Welcome! Enter action: \n1.Search, 2.Channel\n--->")

        if user_action == "1":
            word = input("Search:\n")
            search(word)
        else:
            scrape()

    except KeyboardInterrupt:
        print("\nGoodBye\n")


if __name__ == "__main__":
    main()
