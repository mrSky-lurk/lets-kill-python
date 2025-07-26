# Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
# ================================================================================================================
import requests

headers = {
    "User-Agent": "Mozilla/5.0"
}
word_response = requests.get("https://www.gutenberg.org/files/1112/old/1112-0.txt", headers=headers, timeout=10)
print(word_response.status_code)


# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
# the min, max, mean, median, standard deviation of cats' weight in metric units.
# the min, max, mean, median, standard deviation of cats' lifespan in years.
# Create a frequency table of country and breed of cats
# ================================================================================================================
import statistics

cat_response = requests.get("https://api.thecatapi.com/v1/breeds")
res_text = cat_response.text
print(res_text)
cat_weights = [cat['weight'].get('metric') for cat in cat_response.json()]
print(cat_weights)
cat_min_ages = [cat.split('-')[0].strip() for cat in cat_weights]
cat_max_ages = [cat.split('-')[1].strip() for cat in cat_weights]
print('The min cat weights can be:: ', int(min(cat_min_ages)))
print('The max weight of cat can be:: ', int(max(cat_max_ages)))
print('The mean of cat weights:: ', statistics.mean(range(int(int(min(cat_min_ages))), int(max(cat_max_ages)) + 1)))
print('The median of cat weights:: ', statistics.median(range(int(min(cat_min_ages)), int(max(cat_max_ages)) + 1)))
print('The SD of cat weights:: ', statistics.stdev(range(int(min(cat_min_ages)), int(max(cat_max_ages)) + 1)))
print(" ================================================================================================================")
cat_lifespan = [cat.get('life_span') for cat in cat_response.json()]
cat_min_life = [cat.split('-')[0].strip() for cat in cat_lifespan]
cat_max_life = [cat.split('-')[1].strip() for cat in cat_lifespan]
print('The min cat life can be:: ', int(min(cat_min_life)))
print('The max life of cat can be:: ', int(max(cat_max_ages)))
print('The mean of cat life span:: ', statistics.mean(range(int(min(cat_min_life)), int(max(cat_max_life)) + 1)))
print('The median of cat life span:: ', statistics.median(range(int(min(cat_min_life)), int(max(cat_max_life)) + 1)))
print('The SD of cat life span:: ', statistics.stdev(range(int(min(cat_min_life)), int(max(cat_max_life)) + 1)))
print(" ================================================================================================================")
cat_origins = dict()
for cat in cat_response.json():
    if cat.get('origin') in cat_origins.keys():
        cat_origins[cat.get('origin')] = cat_origins[cat.get('origin')] + 1
    else:
        cat_origins[cat.get('origin')] = 1
print('frequency map:: ', cat_origins)

# Read the countries API https://restcountries.eu/rest/v2/all and find
# the 10 largest countries
# the 10 most spoken languages
# the total number of languages in the countries API
# ================================================================================================================




# UCI is one of the most common places to get data sets for data science and machine learning.
# Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php).
# Without additional libraries it will be difficult, so you may try it with BeautifulSoup4
# ================================================================================================================
from bs4 import BeautifulSoup
dataset_response = requests.get("https://archive.ics.uci.edu/dataset/19/car+evaluation")
# print(dataset_response.text)
soup = BeautifulSoup(dataset_response.text, 'html.parser')
get_title = soup.find_all('title')
gt_text = soup.text #All text content of the page
get_css = soup.select_one("div[class='shadow']>div[class='p-4 pt-0']>div>div>p").get('class')
print(get_title)
