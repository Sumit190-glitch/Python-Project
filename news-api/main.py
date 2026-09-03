import requests 
Query = input("What type of news you are interested: ")
api = "ed63b21586134d0097947b4ffe0cf22d"
url = f"https://newsapi.org/v2/everything?q={Query}&from=2026-01-23&sortBy=publishedAt&apiKey={api}"

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n **************************** \n")
    
