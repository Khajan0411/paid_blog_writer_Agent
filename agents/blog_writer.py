import requests
from bs4 import BeautifulSoup
from config import BLOG_AGENT_API_KEY

def generate_blog(topic):
    # Simulated blog writing using web scraping (you can replace this with Groq/OpenAI API)
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    blog_text = ""
    for para in paragraphs[:5]:
        blog_text += para.text.strip() + "\n\n"
    return blog_text or "No content found. Try a different topic."


if __name__ == "__main__":
    print(generate_blog("Artificial Intelligence"))