import os
import requests
from dotenv import load_dotenv

load_dotenv()

news_api_key = os.getenv("NEWS_API_KEY")

def fetch_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&pageSize=5&apiKey={news_api_key}"
    response = requests.get(url)
    data = response.json()

    if data["status"] != "ok":
        print("Failed to fetch news. Check your API key.")
        return

    articles = data["articles"]

    if not articles:
        print("No articles found for this topic.")
        return

    print("\n" + "=" * 50)
    print(f"  TOP NEWS — {topic.upper()}")
    print("=" * 50 + "\n")

    for i, article in enumerate(articles, 1):
        print(f"{i}. {article['title']}")
        print(f"   {article['description']}")
        print(f"   Source: {article['source']['name']}")
        print()

print("Welcome to News Fetcher!")
print("Get today's top news on any topic.\n")

while True:
    topic = input("Enter a topic (or 'quit' to exit): ").strip()

    if topic.lower() == "quit":
        print("Goodbye!")
        break

    if not topic:
        continue

    print(f"\nFetching news about '{topic}'...")
    fetch_news(topic)