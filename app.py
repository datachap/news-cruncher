import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, url_for
from transformers import AutoModelForSeq2SeqLM, BartTokenizer
import re
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from flask import Flask

app = Flask(__name__)

def summary_generate(text):
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
    tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

    max_length = 350  # Increase max_length for longer summaries
    inputs = tokenizer.encode("summarize: " + text, max_length=1024, return_tensors="pt", truncation=True)
    summary_ids = model.generate(inputs, max_length=max_length, min_length=150, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
# Create a list to store crawled data
links_data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the URL entered by the user
        url = request.form['url']

        try:
            # Fetch the webpage content
            response = requests.get(url)

            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the title and URL
            title = soup.title.string

            # Extract the page content
            content = soup.get_text()
            summary = summary_generate(content)

            links_data.append({'title': title, 'url': url, 'content': content, 'summary': summary})

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render_template('index.html', error_message=error_message)

    return render_template('index.html', links_data=links_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
