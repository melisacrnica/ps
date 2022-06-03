import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('landingPage.html', name= 'Brandon Magaña', major = 'Software Engineering',profile_photo='static/img/logo.jpg', url=os.getenv('URL'))

@app.route('/about-me')
def about_me():
    return render_template('about-me.html', url=os.getenv('URL'))

@app.route('/contact-me')
def contact_me():
    return render_template('contact-me.html', url=os.getenv('URL'))

@app.route('/projects')
def projects():
    return render_template('projects.html', url=os.getenv('URL'))

@app.route('/education')
def education():
    return render_template('education.html', url=os.getenv('URL'))