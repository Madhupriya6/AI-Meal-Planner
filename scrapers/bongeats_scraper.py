import requests
from bs4 import BeautifulSoup


def search_recipe(query):
    url = f"https://www.bongeats.com/?s={query}"

    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    recipes = []
    seen_titles = set()

    for heading in soup.find_all("h2"):
        link_tag = heading.find("a")
        title = link_tag.get_text(strip=True) if link_tag else heading.get_text(strip=True)
        href = link_tag["href"] if link_tag and link_tag.has_attr("href") else None

        if not title or title in seen_titles:
            continue

        seen_titles.add(title)
        recipes.append({
            "title": title,
            "url": href or url,
        })

    return recipes
