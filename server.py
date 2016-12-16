from flask import Flask, request
from holiday_tweets import hashtag, get_html
import os

app = Flask(__name__)


@app.route('/')
def root():
    return open('static/twitter.html').read()


@app.route("/get_tweets/")
def get_tweets():
    tag = request.values.get('tag', 'cat')
    tweets = hashtag(tag, 50)
    s = """<link href="https://fonts.googleapis.com/css?family=Cabin+Sketch" rel="stylesheet">
    <link href='/static/twitter.css' rel='stylesheet'>
    <h2>#GotYourTweet</h2>
    <table>"""
    # s += '\n'.join(
    #     '<tr><td>{}</td></tr>'.format(get_html(t.id)) for t in tweets)
    x = '<tr>'  # initialize new string of table data
    for i in range(len(
            tweets)):  # iterate over length of the tweet list by index
        x += '<td>{}</td>'.format(
            get_html(tweets[i].id))  # tweets[i] is single tweet data
        if i % 3 == 2:
            x += '</tr><tr>'  # every three items closes row and opens new one
    x += '</tr>'  # closes table data string
    s += x  # concatenate table data with rest of html
    s += '</table>'
    return s


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
