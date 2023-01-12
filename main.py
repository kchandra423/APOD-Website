import requests
import streamlit as st
from bs4 import BeautifulSoup

raw_html = requests.get('https://apod.nasa.gov/apod/astropix.html').text
tree = BeautifulSoup(raw_html, features='html.parser')
img_link = (tree.find('img')).attrs['src']
img_link = f'https://apod.nasa.gov/apod/{img_link}'
img_data = requests.get(img_link).content
with open('current_photo.jpg', 'wb') as handler:
    handler.write(img_data)
st.image('current_photo.jpg')
