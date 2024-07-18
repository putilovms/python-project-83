from flask import Flask, render_template, url_for
import os
from dotenv import load_dotenv
import logging

custom_time_format = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(
    level=logging.DEBUG,
    filename="page_analyzer.log",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt=custom_time_format
)

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def home_page():
    url = url_for('home_page')
    logging.debug(f"Страница загружена: {url}")
    return render_template('index.html')
