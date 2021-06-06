# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask import request
from flask import abort
from flask_cors import CORS
from model import Movie_Caption

app=Flask(__name__)
CORS(app)


@app.route('/api/pull_cuptions',methods=['POST'])
def index():
    
    movie_id =  request.args['movie_id']
    # Movie_Caption.add_movie(movie_id)
    
    return jsonify({'message':movie_id})
   


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)

































