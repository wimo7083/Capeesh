import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify, abort, Response
from flask_sqlalchemy import SQLAlchemy
from models import db, pick_words, word_table, query_all_words

application = Flask(__name__)
application.config.from_object('config')
db.init_app(application)

# encode in rest_url, or post a body (html/ json) http post-> get a body
@application.route('/')
def main():
    return render_template('index.html')    
    
    
@application.route('/showSignUp')
def showSignUp():
    return render_template('start.html')
    
    
@application.route('/NewPlayer')
def new_Player():
    return render_template('Waiting_Response.html')
    #request echo to ask for name and grade level
    # get data from echo, try to make database. 
    # if return None (duplicate) then you ask for them to chose different nickname
    
@application.route('/fivewords/<int:user_level>')
def five_words(user_level):
    print('here are 5 words')
    return jsonify(results = pick_words(user_level))        
        
        
@application.route('/Continue')
def Continue():
    return render_template('Waiting_Response.html')
    # send request to echo for user name. 
    # look up person, if cannot find prompt again
    # if user not entered:
    #   new_player()
    
    
    
if __name__ == "__main__":
    app.run(debug= True)