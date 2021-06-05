#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 15:30:25 2021

@author: Viktor Semenov
"""

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

video_id='fhAw-IgoyMw'

cuptions=YouTubeTranscriptApi.get_transcript(video_id)
formatter = JSONFormatter()
# .format_transcript(transcript) turns the transcript into a JSON string.
json_formatted = formatter.format_transcript(cuptions, indent=2)


# Now we can write it out to a file.
with open('test_transcript.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_formatted)

#{'text': 'to use', 'start': 684.56, 'duration': 3.519}
transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
transcript = transcript_list.find_transcript(['en'])
translated_transcript = transcript.translate('ru')
# print(translated_transcript.fetch())