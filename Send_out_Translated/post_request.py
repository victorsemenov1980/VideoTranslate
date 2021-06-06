# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask import request

from flask_cors import CORS
from model import Movie_Caption


app=Flask(__name__)
CORS(app)


@app.route('/api/get_cuptions',methods=['GET'])
def index():
    
    movie_id =  request.args['movie_id']
    
    if Movie_Caption.retrieve_translated(movie_id) is not None:
        return Movie_Caption.retrieve_translated(movie_id)
    else:
        return jsonify({'message':'video is not in db'})
   



if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0',port=8000)
































