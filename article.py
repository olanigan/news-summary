import requests
from newspaper import Article

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

session = requests.Session()

def get_article(article_url):
    try:
        response = session.get(article_url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            article = Article(article_url)
            article.download()
            article.parse()

            result = f"Title: {article.title}\nText: {article.text}"
            return result
        else:
            print(f"Failed to fetch article at {article_url}")
    except Exception as e:
        print(f"Error occurred while fetching article at {article_url}: {e}")

# article_url = "https://www.artificialintelligence-news.com/2022/01/25/meta-claims-new-ai-supercomputer-will-set-records/"
# print(get_article(article_url))