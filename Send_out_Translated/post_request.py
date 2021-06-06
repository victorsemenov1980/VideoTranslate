# -*- coding: utf-8 -*-

from flask import Flask, jsonify, abort
from flask import request
import json
from flask_cors import CORS
from model import Movie_Caption


app=Flask(__name__)
CORS(app)

def get_paginated_list(results, url, start, limit):
    results=json.loads(results)
    start = int(start)
    limit = int(limit)
    count = len(results)
    if count < start or limit < 0:
        abort(404)
    # make response
    obj = {}
    obj['start'] = start
    obj['limit'] = limit
    obj['count'] = count
    # make URLs
    # make previous url
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
    # make next url
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    # finally extract result according to bounds
    obj['results'] = results[(start - 1):(start - 1 + limit)]
    return json.dumps(obj,indent=2, ensure_ascii=False)

@app.route('/api/get_cuptions',methods=['GET'])
def index():
    
    movie_id =  request.args['movie_id']
    start =  request.args['start']
    limit =  request.args['limit']
    url='/api/get_cuptions'
    if Movie_Caption.retrieve_translated(movie_id) is not None:
        results=Movie_Caption.retrieve_translated(movie_id)
        return get_paginated_list(results, url, start, limit)
    else:
        return jsonify({'message':'video is not in db'})
   



if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0',port=8000)





























