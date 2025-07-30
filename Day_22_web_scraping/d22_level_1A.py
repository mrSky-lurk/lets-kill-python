# Exercises: Day 22
# Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
# ================================================================================================================
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import json

url = "http://www.bu.edu/president/boston-university-facts-stats/"
print("Fetching details.. Please Wait..")
bu_web = requests.get(url)
print(f"Status Code: {bu_web.status_code}")
soup = BeautifulSoup(bu_web.content, "html.parser")
clean_content = ' '.join(soup.get_text().split())
data = {
    "title": soup.find('title').get_text(strip=True),
    "content_header": soup.select_one("h4.bu-banner-subtitle").get_text(strip=True),
    "quick-facts": dict(
        (article.find('h3').get_text(strip=True), article.find("div", class_='bu-stat-element').get_text(strip=True))
        for article in soup.select("div.bu-stat-list.bu-stat-count-3 > article > div.bu-stat-inner.js-bu-stat-inner"))

}
data.update(dict((elm.select_one("h4.stat-group-title").get_text(strip=True),
                  dict((item.select_one("span.stat-label").get_text(strip=True),
                        item.select_one("span.stat-figure").get_text(strip=True))
                       for item in elm.select("div.facts-stats-content > section > ul > li")))
                 for elm in soup.select("div.facts-stats-content > section")))
campus_value = dict((elm.find("h3").get_text(strip=True), elm.find("span", class_='bu-stat-value').get_text(strip=True)) for elm in
         soup.select("div.facts-stats-content > div > article > div.bu-stat-inner.js-bu-stat-inner"))
data.update({"campus": campus_value})
print(data)

path_to_json = Path(__file__).resolve().parents[1] / "Day_22_web_scraping" / "BU_data.json"
with path_to_json.open(mode="+w", encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2))
    print(f"data file created - {path_to_json}")

