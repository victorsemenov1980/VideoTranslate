#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 15:30:25 2021

@author: Viktor Semenov
"""

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
import json

# video_id='fhAw-IgoyMw'
# video_id='ZCdW4cWGqzg'

def pull_youtube_cuptions(video_id):
    try:
        formatter = JSONFormatter()
        cuptions=YouTubeTranscriptApi.get_transcript(video_id)
        
        #We get list of dicts as follows
        #{'text': 'to use', 'start': 684.56, 'duration': 3.519}
        
        # .format_transcript(transcript) turns the transcript into a JSON string.
        json_formatted = formatter.format_transcript(cuptions, indent=2)
        
        
        # Now we can write it out to a file.
        # with open('test_transcript.json', 'w', encoding='utf-8') as json_file:
        #     json_file.write(json_formatted)
        
        
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(['en'])
        translated_transcript = transcript.translate('ru')
        
        json_formatted_translated=json.dumps(translated_transcript.fetch(),indent=2, ensure_ascii=False,)
        
        return json_formatted, json_formatted_translated
    except Exception as e:
        print(e)
        
        return 0













