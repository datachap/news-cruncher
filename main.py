from flask import Flask, render_template, request
import newsScraperSummarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/specific-crawler', methods=['POST'])
def singleNewsScraper():
    url = request.form.get('url')
    title, summary, content = newsScraperSummarizer.singleNewsScraper(url)
    return render_template('crawl.html', title=title, summary=summary, content=content)

@app.route('/newsCrawler', methods=['GET', 'POST'])
def newsCrawler():
    return render_template("allNews.html")

if __name__ == '__main__':
    app.run(debug=True)
