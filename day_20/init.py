import requests
import re
from collections import Counter, defaultdict
import statistics
from bs4 import BeautifulSoup

# Task 1: Romeo and Juliet – 10 most frequent words
def romeo_and_juliet_word_freq():
    url = 'http://www.gutenberg.org/files/1112/1112.txt'
    text = requests.get(url).text
    words = re.findall(r'\b[a-z]+\b', text.lower())  # only lowercase alphabetic words
    common = Counter(words).most_common(10)
    print("Top 10 words in Romeo and Juliet:")
    for word, count in common:
        print(f"{word}: {count}")

# Task 2: The Cat API Analysis
def analyze_cats():
    url = 'https://api.thecatapi.com/v1/breeds'
    data = requests.get(url).json()

    weights = []
    lifespans = []
    country_breeds = defaultdict(list)

    for cat in data:
        # Parse weights
        weight_str = cat.get("weight", {}).get("metric", "")
        if weight_str and " - " in weight_str:
            low, high = map(float, weight_str.split(" - "))
            weights.append((low + high) / 2)

        # Parse lifespans
        lifespan_str = cat.get("life_span", "")
        if lifespan_str and " - " in lifespan_str:
            low, high = map(float, lifespan_str.split(" - "))
            lifespans.append((low + high) / 2)

        # Country and breed mapping
        origin = cat.get("origin", "Unknown")
        breed = cat.get("name", "Unknown")
        country_breeds[origin].append(breed)

    print("\n🐱 Cat Weights (metric kg):")
    print_stats(weights)

    print("\n🐱 Cat Lifespans (years):")
    print_stats(lifespans)

    print("\n📊 Frequency table of country and cat breeds:")
    for country, breeds in country_breeds.items():
        print(f"{country}: {len(breeds)} breeds")

def print_stats(data):
    print(f"Min: {min(data):.2f}")
    print(f"Max: {max(data):.2f}")
    print(f"Mean: {statistics.mean(data):.2f}")
    print(f"Median: {statistics.median(data):.2f}")
    print(f"Standard Deviation: {statistics.stdev(data):.2f}")

# Task 3: Countries API
def analyze_countries():
    url = 'https://restcountries.com/v3.1/all'
    countries = requests.get(url).json()

    # 10 largest countries by area
    countries_with_area = [(c['name']['common'], c.get('area', 0)) for c in countries]
    largest = sorted(countries_with_area, key=lambda x: x[1], reverse=True)[:10]
    print("\n🌍 10 Largest Countries by Area:")
    for name, area in largest:
        print(f"{name}: {area:.0f} km²")

    # Most spoken languages
    lang_counter = Counter()
    all_languages = set()
    for c in countries:
        langs = c.get('languages', {})
        all_languages.update(langs.values())
        lang_counter.update(langs.values())

    print("\n🗣️ 10 Most Spoken Languages:")
    for lang, count in lang_counter.most_common(10):
        print(f"{lang}: spoken in {count} countries")

    print(f"\n🔢 Total number of distinct languages: {len(all_languages)}")

# Task 4: UCI Machine Learning Repository
def list_uci_datasets():
    url = 'https://archive.ics.uci.edu/ml/datasets.php'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    # Datasets are in <table> tags, inside <p><b> or <a>
    print("\n📚 UCI Machine Learning Repository datasets (sample list):")
    table = soup.find('table', {'border': '1'})
    if not table:
        print("Failed to locate dataset table.")
        return

    rows = table.find_all('tr')[1:]  # skip header
    for row in rows[:10]:  # first 10 datasets
        cells = row.find_all('td')
        if cells and cells[0].find('a'):
            dataset_name = cells[0].find('a').text.strip()
            print(f"- {dataset_name}")

# Run all tasks
if __name__ == "__main__":
    romeo_and_juliet_word_freq()
    analyze_cats()
    analyze_countries()
    list_uci_datasets()
