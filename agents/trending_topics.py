import requests
from bs4 import BeautifulSoup

def fetch_trending_topics(user_interest=None):
    if user_interest:
        search_term = user_interest.replace(" ", "+")
    else:
        search_term = "technology+trending"
    url = f"https://news.google.com/search?q={search_term}&hl=en-IN&gl=IN&ceid=IN%3Aen"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.select('article h3')
    topics = [headline.text.strip() for headline in headlines[:5]]
    return topics


if __name__ == "__main__":
    print(fetch_trending_topics("AI"))
    print(fetch_trending_topics())
