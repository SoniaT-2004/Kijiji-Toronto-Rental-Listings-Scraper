from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

with open('raw_html/1700273.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = bs(html_content, 'html.parser')

headers = {"User-Agent": "Mozilla/5.0"}

data = []

# locate the listing cards
listings = soup.find_all("section", {"data-testid": "listing-card"})

# retrieve the title and link of each listing
for listing in listings:
    row = {}

    # retrieve the title and link
    title_tag = listing.find("a", href=True) # only find <a> tags with href attribute
    row['Title'] = title_tag.text.strip() if title_tag else "No title"
    link = title_tag["href"] if title_tag else "No link"
    row['Link'] = link

    # retrieve the address
    resp = requests.get(link, headers=headers)
    if resp.status_code == 200:
        soup = bs(resp.text, "html.parser")

        addr_tag = soup.find("button", class_="sc-c8742e84-0 fukShK")
        row['Address'] = addr_tag.get_text(strip=True) if addr_tag else "N/A"
    else:
        print("Request failed")

    # retrieve the price
    price_tag = listing.find("div", {"data-testid": "listing-price-container"})
    price = price_tag.text.strip() if price_tag else "No price"
    row['Price'] = int(price.replace(",", "").split("$")[1].split(".")[0]) # clean price

    # retrieve other attributes
    keys = ['Bedrooms', 'Bathrooms', 'Unit type', 'Parking included', 'Size (sqft)', 'Pets friendly']
    for key in keys:
        tag = listing.find("li", {"aria-label": key})
        value = tag.get_text(strip=True) if tag else "N/A"
        if key == 'Parking included':
            value = 'Yes' if value == '0' else 'No'
        elif key == 'Size (sqft)' and 'sqft' in value:
            value = value.rstrip('sqft')
        row[key] = value

    data.append(row)

# export as csv
df = pd.DataFrame(data)
df.to_csv("kijiji.csv", index=False)
