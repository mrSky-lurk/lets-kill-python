# Scrape the presidents table and store the data as json
# (https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States).
# The table is not very structured and the scrapping may take very long time.
# ================================================================================================================
# Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
# ================================================================================================================
import json
import pathlib
from bs4 import BeautifulSoup
from selenium import webdriver
import re


def prepare_usa_president_data():
    url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
    page_data_raw = launch_driver(url)
    if page_data_raw:
        json_data = {}
        var_table_data = dict()
        content_list = list()
        soup = BeautifulSoup(page_data_raw, "html.parser")
        var_table_elm = soup.select_one("div.mw-content-ltr.mw-parser-output > table")
        body_row = var_table_elm.select("tbody > tr")
        all_headers = var_table_elm.select("thead > tr > th")
        president_index = 1
        for body_elm in body_row:
            cell_elm = filtered_cell_elements(body_elm)
            skip_first = True
            for header, cell in zip(all_headers, cell_elm):
                if header:
                    if skip_first:
                        skip_first = False
                        continue
                    value = get_value(cell)
                    key = get_key(header)
                    var_table_data[key] = value
            content_list.append({f"{president_index}": var_table_data.copy()})
            president_index += 1
            var_table_data.clear()
            cell_elm.clear()
        json_data["presidents_table:"] = content_list
        print(json_data)
        write_to_file(json_data)
    else:
        print("Sorry! Something went wrong!. Please double check the url.. ")


def write_to_file(json_data):
    path_to_json = pathlib.Path(__file__).resolve().parents[1] / "Day_22_web_scraping" / "USA-presidents.json"
    with open(path_to_json, mode="+w", encoding="utf-8") as file:
        file.write(json.dumps(json_data, indent=2))
        file.close()


def get_key(header):
    key = header.get_text(" ", strip=True).replace("\u2013", "-")
    key = re.sub(r"\s*\[[^\]]*\]\s*", "", key).strip()
    return key


def get_value(cell):
    img = cell.find("img")
    if img:
        alt_text = img.get("alt")
        if not alt_text and img.get("src", "").lower().endswith((".jpg", ".png")):
            alt_text = "N/A"
        value = f"Available - Alt text:: {alt_text}"
    else:
        value = cell.get_text(" ", strip=True).replace("\u2013", "-").replace("\u00a0", " ")
        value = re.sub(r"\s*\[[^\]]*\]\s*", "", value).strip()
    return value


def launch_driver(url):
    driver = webdriver.Chrome()
    print(f"Fetching url : {url} \nPlease Wait..")
    driver.get(url)
    return driver.page_source


def filtered_cell_elements(body_elm):
    flt_elm = list()
    raw_cell_elm = body_elm.find_all(["td", "th", "img"])
    for elm in raw_cell_elm:
        img = elm.find("img")
        if img:
            value = "true" if img.get("alt", "").strip() or img.get("src", "").lower().endswith(
                (".jpg", ".png")) else ""
        else:
            value = elm.get_text(" ", strip=True)
        if value:
            flt_elm.append(elm)
    return flt_elm

prepare_usa_president_data()