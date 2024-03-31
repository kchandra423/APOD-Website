import flask
from flask import Flask, redirect, Response

import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    raw_html = requests.get('https://apod.nasa.gov/apod/astropix.html').text
    tree = BeautifulSoup(raw_html, features='html.parser')
    img_link = (tree.find('img')).attrs['src']
    img_link = f'https://apod.nasa.gov/apod/{img_link}'
    data = requests.get(img_link).content
    # f = open('current.jpg', 'wb')
    # f.write(data)
    # f.close()
    # f"<img src = '{img_link}', alt = 'amongus', style='vertical-align:middle'>" \
    return  f"<img src = '{img_link}', alt = 'amongus', width = 100%, height = 100%, margin=0px>"

if __name__ == '__main__':
    app.run()
