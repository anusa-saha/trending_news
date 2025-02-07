import requests

def get_trending_news(api_key):
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google_news",
        "api_key": api_key,
        "q": "trending news",  
        "num": 10,
        "tbm": "nws"  
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        trending_news = []
        for article in data.get('news_results', [])[:10]: 
            news_item = {
                "title": article.get('title', 'No title'),
                "link": article.get('link', '#'),
                "source": article.get('source', 'Unknown'),
                "published_date": article.get('date', 'Unknown')
            }
            trending_news.append(news_item)
        
        return trending_news
    
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []

api_key = "dd6314030e1d1789cb3cdf6c3d797cb0b63f2ee1382182bcbe99ea4c59d3039d"
news = get_trending_news(api_key)
for item in news:
    print(item)