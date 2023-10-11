from flask import Flask, render_template, request
import newsScraperSummarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/specific-crawler', methods=['POST'])
def singleNewsScraper():
    url = request.form.get('url')
    urlLink, content, summary = newsScraperSummarizer.singleNewsScraper(url)
    return render_template('crawl.html', urlLink=urlLink, content=content, summary=summary)

@app.route('/newsCrawler', methods=['POST'])
def newsCrawler():
    return render_template("allNews.html")

if __name__ == '__main__':
    app.run(debug=True)
