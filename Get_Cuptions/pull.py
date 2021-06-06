# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask import request
import requests
from flask_cors import CORS
from model import Movie_Caption


app=Flask(__name__)
CORS(app)

def check_video_url(video_id):
    checker_url = "https://www.youtube.com/oembed?url=http://www.youtube.com/watch?v="
    video_url = checker_url + video_id

    request = requests.get(video_url)

    return request.status_code == 200

@app.route('/api/pull_cuptions',methods=['POST'])
def index():
    
    movie_id =  request.args['movie_id']
    
    if check_video_url(movie_id)==False:
        return jsonify({'message':'wrong movie id'})
    else:
        if Movie_Caption.add_movie(movie_id)!=0:
            return jsonify({'Added to Db':movie_id})
        else:
            return jsonify({'message':'no subtitiles for this video'})
   


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)
































