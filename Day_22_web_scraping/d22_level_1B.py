# Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
# ================================================================================================================
import json
import pathlib
import requests
from bs4 import BeautifulSoup

url = "https://archive.ics.uci.edu/dataset/101/tic+tac+toe+endgame"
print(f"Fetching url : {url} \nPlease Wait..")
page_data_raw = requests.get(url)
if page_data_raw.status_code == 200:
    soup = BeautifulSoup(page_data_raw.content, "html.parser")
    var_table_elm = (soup.find("h1", attrs={"data-svelte-h": "svelte-fywzbh"}).find_parent("div", class_='shadow').select_one("table.my-4.w-full"))
    json_data = {}
    var_table_data = dict()
    content_list = list()
    body_row = var_table_elm.select("tbody > tr")
    all_headers = var_table_elm.find_all("th")
    for body_elm in body_row:
        cell_elm = body_elm.find_all("td")
        for header,cell in zip(all_headers,cell_elm):
            key = header.get_text(strip=True)
            value = cell.get_text(strip=True)
            var_table_data[key] = value
        content_list.append(var_table_data.copy())
        var_table_data.clear()
    json_data["variables_table:"] = content_list
    print(json_data)
    path_to_json = pathlib.Path(__file__).resolve().parents[1] / "Day_22_web_scraping" / "tic-tac-tow.json"
    with open(path_to_json, mode="+w", encoding="utf-8") as file:
        file.write(json.dumps(json_data, indent=2))
        file.close()
else:
    print("Sorry! Something went wrong!. Please double check the url.. ")