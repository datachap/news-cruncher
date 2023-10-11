import json
from newsFetcher import get_news_headlines
from newsScraperSummarizer import newsScraper
import htmlGenerator
import os

# Determine the full path to the templates folder
templates_folder = os.path.join(os.path.dirname(__file__), 'templates')

# Get the news list from the scraper
headlines = get_news_headlines()
finalizedNews = newsScraper(headlines)
with open ("data.json", "w") as f:
    json.dump(finalizedNews, f)

# Example usage: Provide the path to your data.json file
data_json_file = 'data.json'
html_code = htmlGenerator.json2Html(data_json_file)

with open(os.path.join(templates_folder, 'allNews.html'), 'w', encoding='utf-8') as file:
    file.write(html_code)
