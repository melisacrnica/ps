import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

description = "I'm a second year college student majoring in Software Engineering, and I am aproduction Engineer Fellow at MLH this summer!"


@app.route('/')
def landing_page():
    return render_template('landingPage.html', name= 'Brandon Magaña', description = description,profile_photo='static/img/logo.jpg', landing_page=True, url=os.getenv('URL'))

@app.route('/about-me')
def about_me():
    return render_template('about-me.html', landing_page=False, url=os.getenv('URL'))

@app.route('/contact-me')
def contact_me():
    return render_template('contact-me.html', url=os.getenv('URL'))

@app.route('/projects')
def projects():
    return render_template('projects.html', url=os.getenv('URL'))

@app.route('/education')
def education():
    return render_template('education.html', url=os.getenv('URL'))