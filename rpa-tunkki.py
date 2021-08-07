from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time
import sys
from urllib.request import urlopen
import re

try:
    room = sys.argv[1]
    playlist = sys.argv[2]
except:
    print("not enough arguments, quitting.")
    quit()

driver = None

def init_webdriver():
    global driver
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")  # Last I checked this was necessary.
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

def join_room(url):
    driver.get(url)

def add_video_to_playlist(list):
    for video in list:
        driver.find_element(By.XPATH, "//input[@class='searchInput']").send_keys(video)
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@class='searchInput']").send_keys(
            Keys.ENTER
        )
        time.sleep(1)
        print("Video added ", video)

def main():
    init_webdriver()
    join_room("https://sync-tube.de/rooms/" + str(room))
    print("Joining SyncTube room {}".format(str(room)))
    url = playlist
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    material = str(html)
    res = [i.start() for i in re.finditer("watch\\?v", material)]
    songs_in_scraped_playlist = []

    for id in res:
        songs_in_scraped_playlist.append(
            "https://www.youtube.com/watch?v=" + material[(id + 8) : (id + 8 + 11)]
        )
    songs_in_scraped_playlist = list(dict.fromkeys(songs_in_scraped_playlist))
    add_video_to_playlist(songs_in_scraped_playlist)

main()
