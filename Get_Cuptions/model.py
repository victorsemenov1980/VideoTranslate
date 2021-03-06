#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 15:49:15 2021

@author: Viktor Semenov
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, JSON, String
from youtube_api import pull_youtube_cuptions
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://<user>:<password>@localhost:5433/cuptions')

Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()
class Movie_Caption(Base):
    __tablename__='cuptions'
    id=Column(Integer,primary_key=True)
    movie_id = Column(String(50))
    transcript_original=Column(JSON)
    transcript_translated=Column(JSON)
    
    def add_movie(youtube_movie_id):
        
        processed=pull_youtube_cuptions(youtube_movie_id)
        if processed!=0:
            new_movie=Movie_Caption(movie_id=youtube_movie_id,transcript_original=processed[0], transcript_translated=processed[1])
            session.add(new_movie)
            session.commit()
            return None
        else:
            return 0
    
    def retrieve_translated(youtube_movie_id):
        return session.query(Movie_Caption).filter(Movie_Caption.movie_id==youtube_movie_id).first().transcript_translated
            
    
    def delete_movie(youtube_movie_id):
        movie=session.query(Movie_Caption).filter(Movie_Caption.movie_id==youtube_movie_id).first()
        session.delete(movie)
        session.commit()
        return None

# Base.metadata.create_all(engine)



# from sqlalchemy import inspect
# inspector = inspect(engine)

# for table_name in inspector.get_table_names():
#    for column in inspector.get_columns(table_name):
#        print("Column: %s" % column['name'])