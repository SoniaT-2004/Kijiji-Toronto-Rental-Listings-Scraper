This project aims to scrape rental listings from [Kijiji Toronto](https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273) to extract key rental information.
This project also processes the address data to extract the FSA for each listing, which can be used for further analysis on rental affordability across regions.

Features:
- Scrapes rental listings in Toronto from Kijiji
- Extracts key info: Title, Link, Address, Price, Bedrooms, Bathrooms, Unit Type, Parking Included, Size (sqft), and Pets Friendly
- Extracts FSA (postal code prefix) from the Address field for each listing

Project Structure
- scrap.py: The main script for scraping rental data from Kijiji, extracting the necessary fields, and saving them to a CSV file.
- kijiji.csv: A CSV file containing all the scraped rental data with fields like Title, Link, Address, Price, etc.
- raw_html/: A folder to store raw HTML pages retrieved during scraping for future debugging and analysis.
