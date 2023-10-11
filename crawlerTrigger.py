import json
from newsFetcher import get_news_headlines
from newsScraperSummarizer import newsScraper
import htmlGenerator

# Get the news list from the scraper
headlines = get_news_headlines()
finalizedNews = newsScraper(headlines)
with open ("data.json", "w") as f:
    json.dump(finalizedNews, f)

# Example usage: Provide the path to your data.json file
data_json_file = 'data.json'
html_code = htmlGenerator.json2Html(data_json_file)

# Write the HTML code to a file
with open("allNews.html", "w", encoding='utf-8') as file:
    file.write(html_code)
    
