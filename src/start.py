from flask import Flask, redirect, url_for, request
import siteCrawler
from flask.json import jsonify



app = Flask(__name__)

@app.route('/crawl',methods = ['POST'])
def hello_admin():
    content = request.get_json(silent=True)
    url = content['url']
    retrivedData = siteCrawler.crawlURL(url)
    return jsonify(retrivedData)

if __name__ == '__main__':
   app.run(debug = True)