import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import random
from app.Data_Loader import Data_Loader
load_dotenv()
app = Flask(__name__)


DATA = Data_Loader()    


@app.route('/')
def landing_page():
    return render_template('landingPage.html', data = DATA.landing_page_data, landing_page=True, url=os.getenv('URL'))

@app.route('/about-me')
def about_me():
    return render_template('about-me.html', data= DATA.about_me_data, url=os.getenv('URL'))

@app.route('/education-and-work-expirience')
def projects():
    return render_template('education-and-work-expirience.html', data = DATA.expiriences_data, url=os.getenv('URL'))

@app.route('/projects')
def education():
    return render_template('projects.html', data = DATA.projects_data, url=os.getenv('URL'))