import requests
import os

# send request
url = "https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273"
headers = {"User-Agent": "Mozilla/5.0"} # pretend accessing through browser
response = requests.get(url, headers=headers)

# check if request is successful
if response.status_code == 200:
    # save raw HTML
    html_content = response.text
    id = url.split("l")[-1]
    folder = "raw_html"
    os.makedirs(folder, exist_ok=True)
    with open(f"{folder}/{id}.html", "w", encoding="utf-8") as f:
        f.write(html_content)
else:
    print("Failed to retrieve the page.")
