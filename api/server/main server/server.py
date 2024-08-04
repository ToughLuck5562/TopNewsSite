
# IMPORTS

import requests
import random
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, url_for, jsonify

# Setup

app = Flask(__name__, template_folder='../../client/client_stuff/templates', static_folder='../../client/client_stuff/static')

# API FUNCTIONS

def GetTopRequests():
    
    Articles = []
      
    try:

        BBCNEWSURL = 'https://www.bbc.com/news'
        
        BBCNEWSURLResponse = requests.get(BBCNEWSURL)
        
        BBCNEWSURLResponseHTML = BBCNEWSURLResponse.text
        
        Soup = BeautifulSoup(BBCNEWSURLResponseHTML, 'html.parser')
        
        TopArticles = Soup.find_all('h2', class_='sc-4fedabc7-3 zTZri')
    
        print(TopArticles)
        
        if TopArticles:
            
            for Article in TopArticles[:3]:
                
                ArticleHeadline = Article.text
                ArticleLink = Article.find_parent('a')['href']
                
                if ArticleLink.startswith('/'):
                    
                    ArticleLink = 'https://www.bbc.com' + BBCNEWSURL
                    
                Articles.append({'ArticleHeadline': ArticleHeadline, 'ArticleLink': ArticleLink, 'ArticleID': random.randint(999, 999999999)})
        
        print(Articles)
        
        return Articles
    
    except:
        
        return None
    
# MainPage

@app.route('/')
def mainREDIRECT():
    
    return redirect(url_for('main'))

@app.route('/main', methods=['POST', 'GET'])
def main():
    
    if request.method == "POST":
        
        return jsonify({'[WARNING]': 'YOU HAVE BEEN BLOCKED FROM ACCESSING THIS PAGE!'})
    
    elif request.method == "GET":
        
        return render_template('main/main.html')

# APIS 

@app.route('/get_top_news')
def getTopRequestsAPI():
    
    return jsonify(GetTopRequests())
# Startup

if __name__ == "__main__":
    
    app.run()