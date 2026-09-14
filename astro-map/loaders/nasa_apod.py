import requests
import os
from config import NASA_API_KEY, DATA_RAW

def load_apod():
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    r = requests.get(url).json()

    img_url = r.get("hdurl") or r.get("url")
    img_data = requests.get(img_url).content

    filename = os.path.join(DATA_RAW, img_url.split("/")[-1])

    with open(filename, "wb") as f:
        f.write(img_data)

    return filename
